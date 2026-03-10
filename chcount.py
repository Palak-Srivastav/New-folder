#program to count characters in a sentence

text = input("Enter a sentence: ")

count = 0
for ch in text:
    count += 1

print("Total characters:", count)

#program to find a character in sentence

target = input("Enter character to count: ")

count = 0
for ch in text:
    if ch == target:
        count += 1

print("Count of", target, ":", count)

#code to seaerh particular character 

target = input("Enter character to search: ")

found = False

for ch in text:
    if ch == target:
        found = True
        break

if found:
    print("Character exists")
else:
    print("Character not found")

#code to count no. of vowels


vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Total vowels:", count)

#code to count spaces

count = 0

for ch in text:
    if ch.isdigit():
        count += 1

print("Total digits:", count)