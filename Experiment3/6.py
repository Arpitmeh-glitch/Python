n=int(input("Enter the number: "))
sum=0
no=len(str(n))
for i in range (0,no):
    dig=n%10
    sum+=dig
    n=n//10
print(sum)