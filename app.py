from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from datetime import datetime
from database import get_connection, create_tables, seed_data
from recommendation import calculate_bmi, get_bmi_status, get_health_goal, calculate_calories, get_recommendations

app=Flask(__name__)
app.secret_key="change-this-secret-key-in-production"
create_tables(); seed_data()


def uid():
    return session.get("user_id")


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs) if uid() else redirect(url_for("login"))
    return wrapper


def user(conn):
    return conn.execute("SELECT * FROM users WHERE id=?", (uid(),)).fetchone()


def latest(conn):
    return conn.execute("""
        SELECT * FROM weight_history
        WHERE user_id=?
        ORDER BY measured_at DESC,id DESC LIMIT 1
    """, (uid(),)).fetchone()


def latest_food_recommendations(conn):
    row = conn.execute("""
        SELECT recommended_at
        FROM food_recommendation_history
        WHERE user_id=?
        ORDER BY recommended_at DESC,id DESC
        LIMIT 1
    """, (uid(),)).fetchone()

    if not row:
        return []

    return conn.execute("""
        SELECT meal_type AS meal, food_name, calories, protein, carbs, fats
        FROM food_recommendation_history
        WHERE user_id=? AND recommended_at=?
        ORDER BY CASE meal_type
            WHEN 'Breakfast' THEN 1
            WHEN 'Lunch' THEN 2
            WHEN 'Snacks' THEN 3
            WHEN 'Dinner' THEN 4
            ELSE 5 END
    """, (uid(), row["recommended_at"])).fetchall()


@app.route("/")
def index():
    return render_template("landing.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if uid():
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        username=request.form.get("username","").strip().lower()
        password=request.form.get("password","")
        name=request.form.get("name","").strip()
        gender=request.form.get("gender","Female")
        pref=request.form.get("food_preference","Veg")

        # Validate each field separately so the user gets the correct message.
        if not username or not name:
            flash("Enter valid username and name.","error")
            return render_template("register.html")

        if len(password) < 6:
            flash("Enter valid details. Password must contain at least 6 characters.","error")
            return render_template("register.html")

        try:
            age=int(request.form.get("age",""))
            height=float(request.form.get("height",""))
        except (TypeError, ValueError):
            flash("Enter valid details. age must be greater than 1 and height in (cm).","error")
            return render_template("register.html")

        if not (1 <= age <= 120 and 50 <= height <= 250):
            flash("Enter valid details. age must be greater than 1 and height in (cm).","error")
            return render_template("register.html")
        c=get_connection()
        if c.execute("SELECT id FROM users WHERE username=?",(username,)).fetchone():
            c.close(); flash("Username already exists.","error")
            return render_template("register.html")
        cur=c.execute("""INSERT INTO users(username,password_hash,name,age,gender,height,food_preference)
            VALUES(?,?,?,?,?,?,?)""",(username,generate_password_hash(password),name,age,gender,height,pref))
        c.commit(); new_id=cur.lastrowid; c.close()
        session.clear(); session["user_id"]=new_id; session["username"]=username
        return redirect(url_for("dashboard"))
    return render_template("register.html")


@app.route("/login",methods=["GET","POST"])
def login():
    if uid(): return redirect(url_for("dashboard"))
    if request.method=="POST":
        username=request.form.get("username","").strip().lower()
        password=request.form.get("password","")
        c=get_connection()
        u=c.execute("SELECT * FROM users WHERE username=?",(username,)).fetchone()
        c.close()
        if not u or not u["password_hash"] or not check_password_hash(u["password_hash"],password):
            flash("Invalid username or password.","error")
            return render_template("login.html")
        session.clear(); session["user_id"]=u["id"]; session["username"]=u["username"]
        return redirect(url_for("dashboard"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/dashboard")
@login_required
def dashboard():
    c=get_connection()
    u=user(c)
    l=latest(c)
    h=c.execute("""SELECT * FROM weight_history WHERE user_id=?
        ORDER BY measured_at DESC,id DESC LIMIT 30""",(uid(),)).fetchall()
    foods=latest_food_recommendations(c)
    c.close()
    return render_template("dashboard.html",user=u,latest=l,history=h,foods=foods)


@app.route("/weight")
@login_required
def weight_page():
    c=get_connection()
    u=user(c); l=latest(c)
    c.close()
    return render_template("weight.html",user=u,latest=l)


@app.route("/weight-history")
@login_required
def history_page():
    c=get_connection()
    rows=c.execute("""SELECT id,weight,bmi,bmi_status,health_goal,calories,source,measured_at
        FROM weight_history WHERE user_id=? ORDER BY measured_at DESC,id DESC""",(uid(),)).fetchall()
    c.close()
    return render_template("history.html",records=rows)


@app.route("/food-history")
@login_required
def food_history_page():
    c=get_connection()
    rows=c.execute("""
        SELECT recommended_at, meal_type, food_name, calories, protein, carbs, fats
        FROM food_recommendation_history
        WHERE user_id=?
        ORDER BY recommended_at DESC,id DESC
    """,(uid(),)).fetchall()
    c.close()
    return render_template("food_history.html",records=rows)


@app.post("/api/weight/save")
@login_required
def save_weight():
    try:
        p=request.get_json(silent=True) or request.form
        w=float(p.get("weight"))
        if not 20<=w<=300:
            raise ValueError

        c=get_connection()
        u=user(c)
        bmi=calculate_bmi(u["height"],w)
        status=get_bmi_status(bmi)
        goal=get_health_goal(bmi)
        calories=calculate_calories(u["age"],u["gender"],u["height"],w)
        at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cur=c.execute("""INSERT INTO weight_history
            (user_id,weight,bmi,bmi_status,health_goal,calories,source,measured_at)
            VALUES(?,?,?,?,?,?,?,?)""",
            (uid(),w,bmi,status,goal,calories,"Manual",at))
        weight_id=cur.lastrowid

        foods=get_recommendations(c,uid(),goal,u["food_preference"])

        for food in foods:
            c.execute("""INSERT INTO food_recommendation_history
                (user_id,weight_history_id,meal_type,food_name,calories,protein,carbs,fats,recommended_at)
                VALUES(?,?,?,?,?,?,?,?,?)""",
                (uid(),weight_id,food["meal"],food["food_name"],food["calories"],
                 food["protein"],food["carbs"],food["fats"],at))

        c.commit(); c.close()

        return jsonify(success=True,record={
            "id":weight_id,"weight":w,"bmi":bmi,"bmi_status":status,
            "health_goal":goal,"calories":calories,"source":"Manual","measured_at":at,
            "foods":foods
        })
    except (TypeError,ValueError):
        return jsonify(success=False,message="Enter a valid weight between 20 and 300 kg."),400


@app.get("/api/weight/history")
@login_required
def history_api():
    c=get_connection()
    rows=c.execute("""SELECT id,weight,bmi,bmi_status,health_goal,calories,source,measured_at
        FROM weight_history WHERE user_id=? ORDER BY measured_at ASC,id ASC""",(uid(),)).fetchall()
    c.close()
    return jsonify(success=True,history=[dict(x) for x in rows])


@app.get("/api/food-history")
@login_required
def food_history_api():
    c=get_connection()
    rows=c.execute("""
        SELECT recommended_at, meal_type, food_name, calories, protein, carbs, fats
        FROM food_recommendation_history
        WHERE user_id=?
        ORDER BY recommended_at DESC,id DESC
    """,(uid(),)).fetchall()
    c.close()
    return jsonify(success=True,history=[dict(x) for x in rows])


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
