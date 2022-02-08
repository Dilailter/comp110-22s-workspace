"""Wordle but in VScode."""

__author__ = "730475811"


def contains_char(guess: str, single_chr: str) -> bool:
    """Finding the single character in the guess."""
    assert len(single_chr) == 1
    idx: int = 0
    while idx < len(guess):
        if guess[idx] == single_chr:
            return True
        idx = idx + 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Checking for indices to determine placement of emojies."""
    assert len(guess) == len(secret)
    i: int = 0
    final_answer: str = ""
    while i < len(secret):
        if guess[i] == secret[i]:
            final_answer += GREEN_BOX
        else:
            if contains_char(secret, guess[i]):
                final_answer += YELLOW_BOX
            else:
                final_answer += WHITE_BOX
        i = i + 1
    return final_answer


def input_guess(expected_length: int) -> str:
    """To prompt the user for the correct amount of characters."""
    secret = expected_length
    guess: str = input(f"Enter a {secret} character word: ")
    while len(guess) != secret:
        guess = input(f"That wasn't {secret} chars! try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn_number: int = 1
    won: bool = False
    while turn_number < 7 and won is not True:
        print(f"=== Turn {turn_number}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        turn_number = turn_number + 1
        if secret == guess:
            won = True
    if won:
        print(f"You won in {turn_number - 1}/6 turns!")
    else: 
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()