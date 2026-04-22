from analysis import full_report
from add_meal import add_meal

while True:
    print("\n==== HEALTH TRACKER ====")
    print("1. Add Meal")
    print("2. Analyze Diet")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_meal()
    elif choice == "2":
        full_report()
    elif choice == "3":
        break
    else:
        print("Invalid choice")