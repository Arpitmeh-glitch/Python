b=int(input("input the coeff of x: "))
a=int(input("input the coeff of x^2: "))
c=int(input("input the coeff of c: "))
d=(b*b)-(4*(a*c))
if(d>0):
    print("the equation has real roots")
elif(d==0):
    print("the equation has two equal roots")
else:
    print("the equation has imaginary roots")