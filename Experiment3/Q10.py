# 1. Write a Python program to print the following pattern using for loop.

for i in range (1,6):
    for j in range(1,6-i):
        print(j,end="")
    for j in range(1-i):
        print(" ",end="")
    for j in range(1-i):
        print("*",end="")
    for j in range(6-i-1,0,-1):
        print(j,end="")
print()