a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))
c=int(input("enter 3rd number: "))
if((a>b)&(a>c)):
    print(a)
elif((b>c)&(b>a)):
    print(b)
else:
    print(c)