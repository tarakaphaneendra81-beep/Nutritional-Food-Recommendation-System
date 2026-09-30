
import sqlite3
from pathlib import Path


# ============================================================
# DATABASE
# ============================================================

DB_NAME = Path(__file__).resolve().parent / "food.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


# ============================================================
# FOOD DATA
# 50 ITEMS PER CATEGORY
# ============================================================

FOOD_NAMES = {

    # ========================================================
    # BREAKFAST
    # ========================================================

    "Breakfast": {

        "Veg": [
            "Ragi Idli",
            "Oats Upma",
            "Vegetable Dosa",
            "Vegetable Poha",
            "Moong Dal Chilla",
            "Idli + Sambar",
            "Vegetable Upma",
            "Paneer Sandwich",
            "Besan Chilla",
            "Pesarattu",
            "Masala Oats",
            "Vegetable Uttapam",
            "Ragi Dosa",
            "Curd Poha",
            "Aval Upma",
            "Paneer Paratha",
            "Aloo Methi Paratha",
            "Mixed Dal Adai",
            "Vegetable Sevai",
            "Millet Upma",
            "Tomato Oats",
            "Spinach Chilla",
            "Corn Poha",
            "Peanut Poha",
            "Curd + Granola Bowl",
            "Fruit Oatmeal",
            "Vegetable Sandwich",
            "Paneer Bhurji Toast",
            "Sprouts Breakfast Bowl",
            "Ragi Porridge",
            "Vegetable Besan Toast",
            "Mixed Millet Dosa",
            "Moong Dal Idli",
            "Vegetable Rava Dosa",
            "Paneer Oats Bowl",
            "Spinach Oats Upma",
            "Carrot Peas Poha",
            "Vegetable Millet Dosa",
            "Curd Millet Bowl",
            "Moong Sprouts Bowl",
            "Vegetable Dal Chilla",
            "Paneer Vegetable Wrap",
            "Ragi Vegetable Upma",
            "Mixed Vegetable Chilla",
            "Broken Wheat Upma",
            "Vegetable Quinoa Upma",
            "Paneer Stuffed Dosa",
            "Moong Dal Pongal",
            "Vegetable Millet Pongal",
            "Healthy Paneer Toast"
        ],

        "Non-Veg": [
            "Boiled Eggs + Fruit",
            "Egg Omelette + Toast",
            "Egg Bhurji + Roti",
            "Chicken Sandwich",
            "Egg White Scramble",
            "Chicken Oats Bowl",
            "Egg Dosa",
            "Egg Uttapam",
            "Chicken Roti Roll",
            "Masala Egg Toast",
            "Chicken Poha",
            "Egg Poha",
            "Chicken Paratha Roll",
            "Egg Paratha",
            "Chicken Upma",
            "Egg Upma",
            "Chicken Porridge",
            "Egg Pesarattu",
            "Chicken Sandwich + Salad",
            "Egg Sandwich",
            "Chicken Ragi Dosa",
            "Egg Ragi Dosa",
            "Chicken Millet Bowl",
            "Egg Millet Bowl",
            "Chicken Chilla Wrap",
            "Egg Chilla Wrap",
            "Chicken Breakfast Bowl",
            "Egg + Avocado Toast",
            "Chicken Scramble Toast",
            "Egg Curry + Toast",
            "Chicken Vegetable Omelette",
            "Egg Oats Bowl",
            "Chicken Quinoa Breakfast Bowl",
            "Egg Spinach Toast",
            "Chicken Ragi Porridge",
            "Egg Vegetable Upma",
            "Chicken Millet Upma",
            "Egg Vegetable Poha",
            "Chicken Dosa Roll",
            "Egg Stuffed Paratha",
            "Chicken Paneer Wrap",
            "Egg and Sprouts Bowl",
            "Chicken Vegetable Sandwich",
            "Egg Masala Dosa",
            "Chicken Oats Chilla",
            "Egg Millet Upma",
            "Chicken Spinach Wrap",
            "Egg Quinoa Bowl",
            "Chicken Breakfast Wrap",
            "Egg Chicken Toast"
        ]
    },


    # ========================================================
    # LUNCH
    # ========================================================

    "Lunch": {

        "Veg": [
            "Brown Rice + Vegetable Curry",
            "Rice + Dal",
            "Rajma Rice",
            "Chole + Roti",
            "Vegetable Khichdi + Curd",
            "Paneer + Roti",
            "Sambar Rice + Vegetables",
            "Millet Rice + Dal",
            "Palak Dal + Rice",
            "Dal Tadka + Roti",
            "Vegetable Biryani + Raita",
            "Paneer Rice Bowl",
            "Chole Rice Bowl",
            "Rajma + Roti",
            "Moong Dal Rice",
            "Curd Rice + Vegetable Salad",
            "Lemon Rice + Dal",
            "Tomato Rice + Curd",
            "Vegetable Pulao + Raita",
            "Kadhi Rice",
            "Mixed Dal + Brown Rice",
            "Tofu Stir Fry + Rice",
            "Paneer Bhurji + Roti",
            "Methi Roti + Dal",
            "Vegetable Millet Khichdi",
            "Quinoa Vegetable Bowl",
            "Chickpea Salad Bowl",
            "Palak Paneer + Rice",
            "Vegetable Curry + Roti",
            "Soya Chunk Rice Bowl",
            "Vegetable Sambar + Brown Rice",
            "Paneer Tikka + Roti",
            "Mixed Vegetable Rice",
            "Dal Palak + Roti",
            "Vegetable Korma + Rice",
            "Tofu Curry + Roti",
            "Chickpea Pulao",
            "Vegetable Dal Khichdi",
            "Paneer Millet Bowl",
            "Rajma Brown Rice Bowl",
            "Moong Sprout Rice Bowl",
            "Vegetable Curd Rice",
            "Masoor Dal + Rice",
            "Chana Dal + Roti",
            "Vegetable Handi + Roti",
            "Tofu Rice Bowl",
            "Paneer Curry + Brown Rice",
            "Mixed Bean Salad Bowl",
            "Soya Keema + Roti",
            "Vegetable Quinoa Pulao"
        ],

        "Non-Veg": [
            "Grilled Chicken + Salad",
            "Chicken Rice Bowl",
            "Chicken Curry + Roti",
            "Fish Curry + Rice",
            "Egg Rice + Salad",
            "Chicken Biryani",
            "Chicken Tikka + Roti",
            "Fish + Brown Rice",
            "Egg Curry + Rice",
            "Chicken Dal Rice Bowl",
            "Chicken Keema + Roti",
            "Chicken Pulao",
            "Fish Fry + Rice",
            "Grilled Fish + Roti",
            "Chicken Kebab Bowl",
            "Chicken Tikka Rice Bowl",
            "Egg Bhurji + Rice",
            "Chicken Saag + Roti",
            "Chicken Pepper Fry + Rice",
            "Fish Tikka + Salad",
            "Chicken Curry + Brown Rice",
            "Egg Masala + Roti",
            "Chicken Stew + Rice",
            "Fish Curry + Roti",
            "Chicken Quinoa Bowl",
            "Egg Biryani + Raita",
            "Chicken Millet Bowl",
            "Chicken Korma + Roti",
            "Fish Rice Bowl",
            "Chicken Stir Fry + Brown Rice",
            "Chicken Palak + Rice",
            "Chicken Masala + Roti",
            "Fish Tikka Rice Bowl",
            "Egg Dal Rice Bowl",
            "Chicken Vegetable Bowl",
            "Chicken Saag Rice Bowl",
            "Fish Curry + Brown Rice",
            "Chicken Pepper Rice Bowl",
            "Egg Curry + Roti",
            "Chicken Quinoa Pulao",
            "Grilled Fish + Salad",
            "Chicken Tandoori + Roti",
            "Fish Masala + Rice",
            "Chicken Keema Rice Bowl",
            "Egg Fried Rice + Salad",
            "Chicken Vegetable Pulao",
            "Fish Millet Bowl",
            "Chicken Tikka Quinoa Bowl",
            "Egg Masala Rice Bowl",
            "Chicken Brown Rice Bowl"
        ]
    },


    # ========================================================
    # SNACKS
    # ========================================================

    "Snacks": {

        "Veg": [
            "Roasted Chickpeas",
            "Roasted Makhana",
            "Fruit Bowl",
            "Sprouts Salad",
            "Peanut Chaat",
            "Corn Chaat",
            "Vegetable Sandwich",
            "Paneer Tikka",
            "Cucumber Salad",
            "Carrot Salad",
            "Mixed Fruit Bowl",
            "Greek Yogurt + Fruit",
            "Roasted Peanuts",
            "Moong Sprouts Chaat",
            "Chana Chaat",
            "Boiled Corn",
            "Vegetable Soup",
            "Tomato Soup",
            "Buttermilk",
            "Curd Bowl",
            "Apple + Peanut Butter",
            "Banana + Peanut Butter",
            "Oats Energy Bowl",
            "Makhana Chaat",
            "Roasted Almonds",
            "Roasted Walnuts",
            "Fruit Yogurt Bowl",
            "Paneer Salad",
            "Tofu Salad",
            "Vegetable Cutlet",
            "Sweet Potato Chaat",
            "Boiled Sweet Corn",
            "Mixed Nuts",
            "Sprouts Sandwich",
            "Peanut Sundal",
            "Green Gram Salad",
            "Chickpea Salad",
            "Cucumber Curd Bowl",
            "Carrot Cucumber Salad",
            "Beetroot Salad",
            "Fruit Chaat",
            "Oats Chivda",
            "Roasted Dal",
            "Millet Snack Bowl",
            "Paneer Cubes",
            "Tofu Cubes",
            "Vegetable Wrap",
            "Healthy Poha Bowl",
            "Mini Idli + Chutney",
            "Ragi Cookies"
        ],

        "Non-Veg": [
            "Boiled Eggs",
            "Egg Salad",
            "Chicken Salad",
            "Chicken Sandwich",
            "Egg Sandwich",
            "Chicken Wrap",
            "Egg Chaat",
            "Chicken Tikka",
            "Grilled Chicken Bites",
            "Egg Bhurji",
            "Chicken Soup",
            "Chicken Clear Soup",
            "Egg Roll",
            "Chicken Roll",
            "Chicken Kebab",
            "Egg Toast",
            "Chicken Toast",
            "Egg + Fruit",
            "Chicken Salad Bowl",
            "Egg Salad Bowl",
            "Chicken Corn Salad",
            "Chicken Cucumber Salad",
            "Egg Sprouts Bowl",
            "Chicken Sprouts Bowl",
            "Egg Wrap",
            "Chicken Lettuce Wrap",
            "Chicken Oats Bowl",
            "Egg Oats Bowl",
            "Chicken Quinoa Salad",
            "Egg Quinoa Salad",
            "Grilled Chicken Cubes",
            "Chicken Tikka Salad",
            "Egg Vegetable Salad",
            "Chicken Vegetable Wrap",
            "Egg Vegetable Wrap",
            "Chicken Soup + Salad",
            "Egg Soup",
            "Chicken Peanut Salad",
            "Egg Peanut Salad",
            "Chicken Brown Rice Bowl",
            "Egg Brown Rice Bowl",
            "Chicken Millet Bowl",
            "Egg Millet Bowl",
            "Chicken Ragi Wrap",
            "Egg Ragi Wrap",
            "Chicken Paneer Wrap",
            "Egg Paneer Wrap",
            "Chicken Chaat",
            "Egg Masala Toast",
            "Chicken Protein Bowl"
        ]
    },


    # ========================================================
    # DINNER
    # ========================================================

    "Dinner": {

        "Veg": [
            "Vegetable Soup + Roti",
            "Paneer Curry + Roti",
            "Dal + Brown Rice",
            "Vegetable Khichdi",
            "Palak Paneer + Roti",
            "Tofu Stir Fry",
            "Vegetable Pulao",
            "Dal Tadka + Roti",
            "Mixed Vegetable Curry + Roti",
            "Paneer Bhurji + Roti",
            "Moong Dal Khichdi",
            "Vegetable Dalia",
            "Ragi Roti + Dal",
            "Vegetable Millet Bowl",
            "Paneer Tikka + Salad",
            "Tofu Curry + Rice",
            "Vegetable Quinoa Bowl",
            "Chole + Roti",
            "Rajma + Brown Rice",
            "Kadhi + Rice",
            "Palak Dal + Roti",
            "Mixed Dal + Roti",
            "Vegetable Stew",
            "Paneer Vegetable Bowl",
            "Soya Chunk Curry + Roti",
            "Vegetable Oats Khichdi",
            "Moong Dal + Brown Rice",
            "Chickpea Curry + Roti",
            "Methi Dal + Roti",
            "Vegetable Soup + Paneer",
            "Tofu Vegetable Bowl",
            "Paneer Millet Bowl",
            "Vegetable Ragi Dosa",
            "Mixed Vegetable Soup",
            "Spinach Dal + Rice",
            "Bottle Gourd Dal + Roti",
            "Lauki Khichdi",
            "Vegetable Barley Bowl",
            "Quinoa Dal Bowl",
            "Paneer Palak Bowl",
            "Soya Chunk Rice Bowl",
            "Vegetable Brown Rice Bowl",
            "Moong Sprout Khichdi",
            "Tofu Roti Wrap",
            "Paneer Roti Wrap",
            "Chana Dal + Brown Rice",
            "Vegetable Millet Khichdi",
            "Mixed Bean Curry + Roti",
            "Light Paneer Curry + Roti",
            "Vegetable Dalia Bowl"
        ],

        "Non-Veg": [
            "Grilled Chicken + Vegetables",
            "Chicken Curry + Roti",
            "Fish Curry + Rice",
            "Chicken Soup + Salad",
            "Chicken Tikka + Salad",
            "Grilled Fish + Vegetables",
            "Egg Curry + Roti",
            "Chicken Stir Fry",
            "Chicken Brown Rice Bowl",
            "Fish Brown Rice Bowl",
            "Chicken Quinoa Bowl",
            "Egg Vegetable Bowl",
            "Chicken Saag + Roti",
            "Fish Tikka + Salad",
            "Chicken Stew + Vegetables",
            "Chicken Millet Bowl",
            "Egg Bhurji + Roti",
            "Chicken Kebab + Salad",
            "Fish Curry + Roti",
            "Chicken Vegetable Soup",
            "Chicken Palak Bowl",
            "Chicken Pepper Fry + Roti",
            "Egg Masala + Roti",
            "Chicken Tikka Bowl",
            "Grilled Chicken Quinoa Bowl",
            "Fish Quinoa Bowl",
            "Chicken Dal Bowl",
            "Chicken Vegetable Rice",
            "Egg Brown Rice Bowl",
            "Chicken Oats Bowl",
            "Fish Millet Bowl",
            "Chicken Ragi Wrap",
            "Egg Ragi Wrap",
            "Chicken Lettuce Wrap",
            "Fish Vegetable Bowl",
            "Chicken Keema + Roti",
            "Chicken Korma + Roti",
            "Fish Masala + Rice",
            "Chicken Tandoori + Salad",
            "Chicken Spinach + Roti",
            "Egg Spinach Bowl",
            "Chicken Tomato Curry + Roti",
            "Fish Pepper Fry + Rice",
            "Chicken Mushroom Stir Fry",
            "Egg Vegetable Stir Fry",
            "Chicken Millet Roti Bowl",
            "Fish Brown Rice + Salad",
            "Chicken Quinoa Pulao",
            "Egg Protein Bowl",
            "Light Chicken Curry + Roti"
        ]
    }
}


# ============================================================
# CREATE TABLES
# ============================================================

def create_tables():

    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL DEFAULT '',
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            height REAL NOT NULL,
            food_preference TEXT NOT NULL DEFAULT 'Veg'
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS weight_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            weight REAL NOT NULL,
            bmi REAL NOT NULL,
            bmi_status TEXT NOT NULL,
            health_goal TEXT NOT NULL,
            calories INTEGER NOT NULL,
            source TEXT NOT NULL,
            measured_at TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS foods (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            food_name TEXT NOT NULL,
            meal_type TEXT NOT NULL,
            category TEXT NOT NULL,
            calories INTEGER NOT NULL,
            protein REAL NOT NULL,
            carbs REAL NOT NULL,
            fats REAL NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS food_recommendation_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            weight_history_id INTEGER,
            meal_type TEXT NOT NULL,
            food_name TEXT NOT NULL,
            calories INTEGER NOT NULL,
            protein REAL NOT NULL,
            carbs REAL NOT NULL,
            fats REAL NOT NULL,
            recommended_at TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(weight_history_id) REFERENCES weight_history(id)
        )
    """)

    # For older databases
    columns = [
        r[1]
        for r in conn.execute("PRAGMA table_info(users)").fetchall()
    ]

    if "password_hash" not in columns:
        conn.execute("""
            ALTER TABLE users
            ADD COLUMN password_hash TEXT NOT NULL DEFAULT ''
        """)

    conn.commit()
    conn.close()


# ============================================================
# NUTRITION DATA
# ============================================================

def nutrition_for(meal_type, category, index):

    base = {
        "Breakfast": 250,
        "Lunch": 360,
        "Snacks": 180,
        "Dinner": 300
    }[meal_type]

    category_bonus = 45 if category == "Non-Veg" else 0

    calorie = (
        base
        + category_bonus
        + ((index * 37) % 161)
        - 50
    )

    calorie = max(120, calorie)

    protein_base = {
        "Breakfast": 8,
        "Lunch": 12,
        "Snacks": 5,
        "Dinner": 10
    }[meal_type]

    protein = (
        protein_base
        + (index % 8)
        + (6 if category == "Non-Veg" else 0)
    )

    fats = round(
        4
        + ((index * 3) % 12)
        + (2 if category == "Non-Veg" else 0),
        1
    )

    carbs = round(
        max(
            8,
            (calorie - protein * 4 - fats * 9) / 4
        ),
        1
    )

    return (
        int(calorie),
        float(protein),
        carbs,
        fats
    )


# ============================================================
# SEED FOOD DATA
# ============================================================

def seed_data():

    conn = get_connection()

    for meal_type, categories in FOOD_NAMES.items():

        for category, names in categories.items():

            for index, food_name in enumerate(names):

                calories, protein, carbs, fats = nutrition_for(
                    meal_type,
                    category,
                    index
                )

                exists = conn.execute("""
                    SELECT id
                    FROM foods
                    WHERE food_name = ?
                    AND meal_type = ?
                    AND category = ?
                """, (
                    food_name,
                    meal_type,
                    category
                )).fetchone()

                if not exists:

                    conn.execute("""
                        INSERT INTO foods
                        (
                            food_name,
                            meal_type,
                            category,
                            calories,
                            protein,
                            carbs,
                            fats
                        )
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, (
                        food_name,
                        meal_type,
                        category,
                        calories,
                        protein,
                        carbs,
                        fats
                    ))

    conn.commit()
    conn.close()


# ============================================================
# INITIALIZE DATABASE
# ============================================================

def initialize_database():

    create_tables()
    seed_data()


# ============================================================
# RUN DIRECTLY
# ============================================================

if __name__ == "__main__":

    initialize_database()

    conn = get_connection()

    total = conn.execute("""
        SELECT COUNT(*) AS count
        FROM foods
    """).fetchone()["count"]

    print("Database initialized successfully.")
    print(f"Total food items: {total}")

    for meal_type in FOOD_NAMES:

        for category in ["Veg", "Non-Veg"]:

            count = conn.execute("""
                SELECT COUNT(*)
                FROM foods
                WHERE meal_type = ?
                AND category = ?
            """, (
                meal_type,
                category
            )).fetchone()[0]

            print(
                f"{meal_type} - {category}: {count}"
            )

    conn.close()

