# Nutritional Food Recommendation System

A Flask + HTML + CSS + JavaScript + SQLite project for personalized nutrition tracking and food recommendations.

## Main flow

1. User opens the launch page.
2. User can choose **Home**, **Login** or **Register** from the top-right navigation.
3. After registration/login, the user can enter weight manually.
4. The system stores the weight in `weight_history`.
5. BMI, BMI status, health goal and approximate daily calories are calculated.
6. Food recommendations are generated from the user's food preference and health goal.
7. Every new weight entry creates a new recommendation history record.
8. Weight History and Food History are available from the dashboard.

## Food recommendation data

The project contains **30 Veg and 30 Non-Veg choices for each meal type**:

- Breakfast: 60 choices
- Lunch: 60 choices
- Snacks: 60 choices
- Dinner: 60 choices

That gives the application **240 food choices** in total. The recommendation engine rotates through the available choices and avoids foods used in the most recent recommendation batches when possible.

Nutrition values are approximate per serving for this project/demo and should not be treated as clinical nutrition advice.

## Run on Windows

```text
python -m venv venv
venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

Open:

```text
http://127.0.0.1:5000/
```

## Project pages

- `/` — Launch page
- `/login` — Login
- `/register` — Registration
- `/dashboard` — Personalized dashboard
- `/weight` — Manual weight entry
- `/weight-history` — Weight history
- `/food-history` — Food recommendation history

## Important

The BMI/calorie/recommendation logic is a project/demo implementation. It should not be treated as medical advice. For a production health product, use validated nutrition data and appropriate clinical review.
