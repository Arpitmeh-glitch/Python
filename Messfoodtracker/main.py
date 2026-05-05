from analysis import full_report
from add_meal import add_meal

while True:
    print("\n==============================")
    print("   STUDENT DIET TRACKER")
    print("==============================")
    print("1. Add Meal")
    print("2. Analyze Diet")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        try:
            add_meal()
        except:
            print("Error while adding meal")

    elif choice == "2":
        try:
            full_report()
        except:
            print("Error while analyzing")

    elif choice == "3":
        print("Exiting")
        break

    else:
        print("Invalid choice")