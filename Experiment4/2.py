Count=0
str1=input("Enter a string: ")
str1=str1.upper()
print(str1)
for ch in str1:
    if(ch=='A')|(ch=='E')|(ch=='I')|(ch=='O')|(ch=='U'):
        count+=1
print(count)