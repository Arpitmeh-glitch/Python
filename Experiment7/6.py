try:
    with open("counter.txt", "r") as f:
        count = int(f.read())
except FileNotFoundError:
    count = 0
count += 1
with open("counter.txt", "w") as f:
    f.write(str(count))
    print("Program executed", count, "times")