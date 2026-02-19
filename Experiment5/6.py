contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All")
    print("6. Exit")

    choice = int(input("Enter choice: "))
    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone
        print("Contact added!")
    elif choice == 2:
        name = input("Enter name to search: ")
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found!")
    elif choice == 3:
        name = input("Enter name to update: ")
        if name in contacts:
            phone = input("Enter new phone: ")
            contacts[name] = phone
            print("Updated successfully!")
        else:
            print("Contact not found!")
    elif choice == 4:
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Deleted successfully!")
        else:
            print("Contact not found!")
    elif choice == 5:
        print("\nAll Contacts:")
        for name, phone in contacts.items():
            print(name, "->", phone)
    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
