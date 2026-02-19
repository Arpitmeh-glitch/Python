n = int(input("Enter number of movies: "))
movies = {}
for i in range(n):
    name = input("Movie name: ")
    year = int(input("Year: "))
    director = input("Director: ")
    cost = int(input("Cost: "))
    collection = int(input("Collection: "))
    
    movies[name] = [year, director, cost, collection]
print("\nAll Movie Details:")
for name in movies:
    print(name, movies[name])
print("\nMovies before 2015:")
for name in movies:
    if movies[name][0] < 2015:
        print(name)
print("\nProfitable Movies:")
for name in movies:
    if movies[name][3] > movies[name][2]:
        print(name)
d = input("\nEnter director name: ")
print("Movies by", d, ":")
for name in movies:
    if movies[name][1] == d:
        print(name)
