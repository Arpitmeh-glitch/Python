gender=input("enter your gender(M/F):")
gender=gender.lower()
if(gender=='m'):
    bonus=5
else:
    bonus=10
sal=int(input("Enter your salary:"))
if(sal<0):
    print("Enter valid salary.")
if (sal<25000):
    bonus=bonus+2
salbonus=((bonus/100)*sal)
print("Bonus:",salbonus)
asd=sal
absd=sal+salbonus
print("Total Salary:",asd)
print("Total salary after bonus:",absd)