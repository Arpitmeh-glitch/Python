with open("city.txt", "w") as f:
    f.write("Dehradun 5.78 308.20\n")
    f.write("Delhi 190 1484\n")
    f.write("Mumbai 200 603\n")
    f.write("Chandigarh 11 114\n")
    f.write("Shimla 2.5 35\n")
with open("city.txt", "r") as f:
    lines = f.readlines()
    total_area = 0
print("All City Details:")
for line in lines:
    city, population, area = line.split()
    population = float(population)
    area = float(area)
    print(city, population, area)
if population > 10:
    print("City with population >10 Lakhs:", city)
    total_area += area
    print("Total Area of all cities:", total_area)