from datetime import datetime
from food_data import food_data
from menu import mess_menu

def add_meal():
    days = list(mess_menu.keys())
    
    print("\nSelect Day:")
    for i, day in enumerate(days, 1):
        print(f"{i}. {day}")

    day_choice = int(input("Enter choice: ")) - 1
    day = days[day_choice]

    meals = list(mess_menu[day].keys())

    print("\nSelect Meal:")
    for i, meal in enumerate(meals, 1):
        print(f"{i}. {meal}")

    meal_choice = int(input("Enter choice: ")) - 1
    meal = meals[meal_choice]

    foods = mess_menu[day][meal]

    total_cal, total_protein, total_carbs = 0, 0, 0

    print("\n🍽️ Items:")
    for food in foods:
        if food in food_data:
            data = food_data[food]
            total_cal += data["calories"]
            total_protein += data["protein"]
            total_carbs += data["carbs"]
        else:
            print(f"⚠️ No data for {food}")

    print(f"\n🔥 Total Calories: {total_cal}")
    print(f"💪 Protein: {total_protein}")
    print(f"🍞 Carbs: {total_carbs}")

    today = datetime.now().date()

    with open("meals.csv", "a") as f:
        f.write(f"{today},{day},{meal},{total_cal},{total_protein},{total_carbs}\n")