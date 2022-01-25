"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730475811"

five_letter_word: str = input("Enter a 5-character word: ") 
single_letter: str = input("Enter a single character: ")
count: int = 0 
print("Searching for " + single_letter + " in " + five_letter_word)

if len(five_letter_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
if len(single_letter) != 1:
    print("Error: Character must be a single character")
    exit()

if single_letter == five_letter_word[0]:
    print(single_letter + " found at index 0")
    count = count + 1
if single_letter == five_letter_word[1]:
    print(single_letter + " found at index 1")
    count = count + 1
if single_letter == five_letter_word[2]:
    print(single_letter + " found at index 2")
    count = count + 1
if single_letter == five_letter_word[3]:
    print(single_letter + " found at index 3")
    count = count + 1
if single_letter == five_letter_word[4]:
    print(single_letter + " found at index 4")
    count = count + 1

if count == 1:
    print("1 instance of " + single_letter + " found in " + five_letter_word)
if count == 0:
    print("No instances of " + single_letter + " found in " + five_letter_word)
if count >= 2:
    print(str(count) + " instances of " + single_letter + " found in " + five_letter_word)

print("thank you for interacting :)")