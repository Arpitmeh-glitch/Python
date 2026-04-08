try:
    filename = input("Enter file name: ")
    with open(filename, "r") as f:
        data = f.read()
        print("File Content:")
        print(data)
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: You don't have permission to access this file.")
except IsADirectoryError:
    print("Error: You entered a directory name instead of a file.")
except Exception as e:
    print("Some other error occurred:", e)