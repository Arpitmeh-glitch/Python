n=int(input("Enter the number: "))
num=n
sum=0
no=len(str(n))
for i in range (0,no):
    dig=n%10
    sum=(sum*10)+dig
    n=n//10
    if(sum==num):
        print("THE number is a palindrome.")
    else:
        print("The number is not a palindrome.")