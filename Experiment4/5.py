s = input("Enter a string: ")

s = s.lower()     
count = {}

for ch in s:
    if ch.isalpha():   
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

for key in sorted(count):
    print(key, ":", count[key])