from collections import defaultdict


def calculate_bmi(height_cm, weight_kg):
    height_m = float(height_cm) / 100
    if height_m <= 0:
        raise ValueError("Invalid height")
    return round(float(weight_kg) / (height_m * height_m), 1)


def get_bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal Range"
    if bmi < 30:
        return "Overweight"
    return "Obesity Range"


def get_health_goal(bmi):
    if bmi < 18.5:
        return "Weight Gain"
    if bmi < 25:
        return "Maintain Weight"
    return "Weight Loss"


def calculate_calories(age, gender, height_cm, weight_kg):
    if str(gender).lower() == "male":
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    return round(bmr * 1.2)


def get_recommendations(conn, user_id, goal, preference, history_batches=3):
    """
    Returns one recommendation per meal type.
    Foods used in the user's recent recommendation batches are avoided first,
    so the dashboard rotates through the larger food list instead of repeating
    the same four meals every time.
    """
    preference = preference if preference in {"Veg", "Non-Veg"} else "Veg"
    meal_types = ["Breakfast", "Lunch", "Snacks", "Dinner"]

    recent = conn.execute("""
        SELECT DISTINCT food_name
        FROM food_recommendation_history
        WHERE user_id=?
          AND recommended_at IN (
              SELECT DISTINCT recommended_at
              FROM food_recommendation_history
              WHERE user_id=?
              ORDER BY recommended_at DESC
              LIMIT ?
          )
    """, (user_id, user_id, history_batches)).fetchall()
    recent_names = {r["food_name"] for r in recent}

    rows = conn.execute("""
        SELECT food_name, meal_type, calories, protein, carbs, fats, category
        FROM foods
        WHERE category=? OR (?='Non-Veg' AND category='Veg')
        ORDER BY id
    """, (preference, preference)).fetchall()

    by_meal = defaultdict(list)
    for row in rows:
        by_meal[row["meal_type"]].append(dict(row))

    # Goal preference: lower calorie foods for weight loss, higher calorie
    # foods for weight gain, middle range for maintenance.
    def distance(food):
        cal = food["calories"]
        if goal == "Weight Loss":
            target = 220
        elif goal == "Weight Gain":
            target = 380
        else:
            target = 300
        return abs(cal - target)

    result = []
    for meal in meal_types:
        candidates = by_meal.get(meal, [])
        fresh = [x for x in candidates if x["food_name"] not in recent_names]
        pool = fresh or candidates
        pool = sorted(pool, key=distance)

        if not pool:
            continue

        # Rotate through the complete available pool instead of only the
        # first few foods, while still sorting toward the current goal.
        batch_count = conn.execute("""
            SELECT COUNT(DISTINCT recommended_at) AS c
            FROM food_recommendation_history
            WHERE user_id=?
        """, (user_id,)).fetchone()["c"]

        index = batch_count % len(pool)
        food = pool[index]
        result.append({
            "meal": food["meal_type"],
            "food_name": food["food_name"],
            "calories": food["calories"],
            "protein": food["protein"],
            "carbs": food["carbs"],
            "fats": food["fats"],
        })

    return result
