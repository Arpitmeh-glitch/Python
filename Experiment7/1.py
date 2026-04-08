with open("name.txt", "w") as f:
    f.write("Arpit\n")
    f.write("Ujwal\n")
    f.write("Ishita\n")
    f.write("Om\n")
    f.write("Ankit\n")

with open("name.txt", "r") as f:
    names = f.read().splitlines()

count_names = len(names)
print("Total names:", count_names)

vowels = "AEIOUaeiou"
vowel_count = sum(1 for name in names if name[0] in vowels)
print("Names starting with vowel:", vowel_count)

longest_name = max(names, key=len)
print("Longest name:", longest_name)