"""An example of conditional (if-else) statements."""

SECRET: int = 3
print("I am thinking of a value between 1-5, what is it?")
guess: int = int(input("what is your guess? "))
if guess == SECRET:
    print("you guessed it correctly!!!")
    print("have a wonderful day!")
else: 
    print("sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("you guessed too high")
    else:
        print("you guessed to low!")
    print("try running the program again")

print("Game over") 