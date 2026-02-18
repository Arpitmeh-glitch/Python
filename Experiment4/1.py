str=input("Enter a string with small and capital letters: ")
count=0
for ch in str:
    if(ch<'a'):
        count+=1
print(count)