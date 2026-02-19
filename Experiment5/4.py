n = int(input("Enter number of persons: "))
d = {}
for i in range(n):
    name = input("Enter name: ")
    city = input("Enter city: ")
    d[name] = city
print("\nNames:")
for i in d.keys():
    print(i)
print("\nCities:")
for i in d.values():
    print(i)
print("\nName and City:")
for i, j in d.items():
    print(i, "->", j)
count = {}
for city in d.values():
    count[city] = count.get(city, 0) + 1

print("\nStudents in each city:")
for city, num in count.items():
    print(city, ":", num)
