def count_characters(text):
    count = 0
    for ch in text:
        count += 1
    return count


def count_specific_character(text, target):
    count = 0
    for ch in text:
        if ch == target:
            count += 1
    return count


def character_exists(text, target):
    for ch in text:
        if ch == target:
            return True
    return False


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count


def count_digits(text):
    count = 0
    for ch in text:
        if ch.isdigit():
            count += 1
    return count


# Main execution
text = input("Enter a sentence: ")

print("Total characters:", count_characters(text))

target = input("Enter character to count: ")
print("Count of", target, ":", count_specific_character(text, target))

target = input("Enter character to search: ")
if character_exists(text, target):
    print("Character exists")
else:
    print("Character not found")

print("Total vowels:", count_vowels(text))
print("Total digits:", count_digits(text))