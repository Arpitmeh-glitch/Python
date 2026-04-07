n = int(input("Enter number of values: "))

tup = ()

for i in range(n):
    x = float(input("Enter value: "))
    tup = tup + (x,)   

avg = sum(tup) / n

print("Tuple:", tup)
print("Average:", avg)