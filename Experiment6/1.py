def find_max_min(numbers):
    if len(numbers) == 0:
        raise ValueError("The sequence is empty")

    maximum = numbers[0]
    minimum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return maximum, minimum
xyz=[1,2,3,4,6]
print(find_max_min(xyz))