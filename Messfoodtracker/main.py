from analysis import full_report
from add_meal import add_meal
from add_meal import remove_meal

while True:
    print("\n//======================================//")
    print("//   ARPIT'S STUDENT DIET TRACKER      //")
    print("//======================================//")
    print("1. Add Meal")
    print("2. Analyze Diet")
    print("3. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        try:
            add_meal()
        except Exception as e:
            print(f"Error while adding meal: {e}")

    elif choice == "2":
        try:
            full_report()
        except Exception as e:
            print(f"Error during analysis: {e}")
    elif choice == "4":
        remove_meal()

    elif choice == "3":
        print("Exiting... Stay healthy!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")