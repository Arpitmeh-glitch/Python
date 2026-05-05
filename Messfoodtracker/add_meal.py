from datetime import datetime
from food_data import food_data
from menu import mess_menu
import csv

def add_meal():
    try:
        print("\n1. Use Mess Menu")
        print("2. Add Custom Meal")

        choice = input("Enter choice: ")

        total_cal = 0
        total_protein = 0
        total_carbs = 0

        if choice == "1":
            days = list(mess_menu.keys())

            print("\nSelect Day:")
            for i in range(len(days)):
                print(i + 1, days[i])

            day_index = int(input("Enter choice: ")) - 1
            day = days[day_index]

            meals = list(mess_menu[day].keys())

            print("\nSelect Meal:")
            for i in range(len(meals)):
                print(i + 1, meals[i])

            meal_index = int(input("Enter choice: ")) - 1
            meal = meals[meal_index]

            foods = mess_menu[day][meal]

            print("\nItems:")
            for food in foods:
                if food in food_data:
                    data = food_data[food]
                    total_cal += data["calories"]
                    total_protein += data["protein"]
                    total_carbs += data["carbs"]
                else:
                    print("No data for", food)

        elif choice == "2":
            day = input("Enter day: ")
            meal = input("Enter meal type: ")

            count = int(input("How many items: "))

            for i in range(count):
                name = input("Name: ")
                cal = float(input("Calories: "))
                protein = float(input("Protein: "))
                carbs = float(input("Carbs: "))

                total_cal += cal
                total_protein += protein
                total_carbs += carbs

        else:
            print("Invalid choice")
            return

        print("\nCalories:", total_cal)
        print("Protein:", total_protein)
        print("Carbs:", total_carbs)

        today = datetime.now().date()

        try:
            file = open("meals.csv", "a", newline="")
            writer = csv.writer(file)
            writer.writerow([today, day, meal, total_cal, total_protein, total_carbs])
            file.close()
            print("Saved")
        except:
            print("Error saving data")

    except:
        print("Invalid input")