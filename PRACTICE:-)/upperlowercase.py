char=input("enter a character: ")
if(char<='z'and char >='a'):
    print(char.upper())
elif(char<'a'or char>'A'):
    print("Enter a valid character.")
else:
    print(char.lower())