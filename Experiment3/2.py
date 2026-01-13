import math
a=int(input("Enter a number to be checked: "))
p=len(str(a))
num=a
total=0
while(a>0):
    digit=a%10
a=a//10
total+=digit**p
if(num==total):
    print("Yes")
else:
    print("No")

print(total)