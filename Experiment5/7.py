tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = int(input("Enter choice: "))
    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == 2:
        print("\nYour Tasks:")
        if len(tasks) == 0:
            print("No tasks available")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])
    elif choice == 3:
        num = int(input("Enter task number to remove: "))
        if 0 < num <= len(tasks):
            removed = tasks.pop(num - 1)
            print("Removed task:", removed)
        else:
            print("Invalid task number!")
    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
