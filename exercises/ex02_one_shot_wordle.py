"""One Shot Wordle Exercise."""

__author__ = "730475811"

secret_word: str = "python"
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

# this loops makes sure the character of guess and secret word are the same.
while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0 
final_answer: str = ""
# loop for checking the indices and responding with colored boxes 
while i < len(secret_word):
    if guess[i] == secret_word[i]:
        final_answer += GREEN_BOX
    else:
        idx: int = 0
        found_character = False 
        while idx < len(secret_word):
            if secret_word[idx] == guess[i]:
                found_character = True
            idx = idx + 1
        if found_character:
            final_answer += YELLOW_BOX
        else:
            final_answer += WHITE_BOX
    i = i + 1

print(final_answer)

if guess == secret_word:
    print("Woo! you got it!")
else:
    print("Not quite. Play again soon!")