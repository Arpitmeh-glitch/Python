def sum_of_cubes(n):
    total = 0
    for i in range(1, n):
        total += i * i * i
    return total
print(sum_of_cubes(8))
#