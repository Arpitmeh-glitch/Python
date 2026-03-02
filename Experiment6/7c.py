def add_numbers(*nums):
    total = 0
    for n in nums:
        total += n
    print("Sum:", total)

add_numbers(1, 2, 3)
add_numbers(5, 10, 15, 20)