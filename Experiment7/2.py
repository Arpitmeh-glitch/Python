with open("numbers.txt", "w") as f:
    f.write("45\n")
    f.write("120\n")
    f.write("300\n")
    f.write("80\n")
    f.write("150\n")
with open("numbers.txt", "r") as f:
    numbers = [int(i) for i in f.read().split()]
    max_number = max(numbers)
    average = sum(numbers) / len(numbers)
    count_greater_100 = sum(1 for i in numbers if i > 100)
print("Maximum number:", max_number)
print("Average:", average)
print("Numbers greater than 100:", count_greater_100)