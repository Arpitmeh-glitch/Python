from datetime import datetime
from food_data import food_data
from menu import mess_menu
import csv
def add_meal():
    print("\n1. Use Mess Menu")
    print("2. Add Custom Meal")

    choice = input("Enter choice: ")

    total_cal, total_protein, total_carbs = 0, 0, 0

    
    if choice == "1":
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

        print("\n Items:")
        for food in foods:
            if food in food_data:
                data = food_data[food]
                total_cal += data["calories"]
                total_protein += data["protein"]
                total_carbs += data["carbs"]
            else:
                print(f"No data for {food}")

   
    elif choice == "2":
        day = input("Enter day (e.g., monday): ")
        meal = input("Enter meal type (breakfast/lunch/snacks/dinner): ")

        num_items = int(input("How many items in your meal? "))

        print("\nEnter nutritional values per item:")

        for i in range(num_items):
            print(f"\nItem {i+1}:")
            name = input("Name: ")

            cal = float(input("Calories: "))
            protein = float(input("Protein: "))
            carbs = float(input("Carbs: "))

            total_cal += cal
            total_protein += protein
            total_carbs += carbs
    else:
        print(" Invalid choice")
        return

    
    print(f"\n Total Calories: {total_cal}")
    print(f" Protein: {total_protein}")
    print(f" Carbs: {total_carbs}")

    today = datetime.now().date()

   
    
    with open("meals.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([today, day, meal, total_cal, total_protein, total_carbs])

    print(" Meal saved successfully!")