import random


def guess_the_number():
    numberToGuess = random.randint(1, 100)
    guessesTaken = 0

    print("Guess a number between 1 and 100")

    while True:
        try:
            userGuess = int(input("Guess a number between 1 and 100: "))
            guessesTaken += 1

            if userGuess < numberToGuess:
                print("Too low")
            elif userGuess > numberToGuess:
                print("Too high")
            else:
                print("Congratulation,you guessed the number")
                break
        except ValueError:
            print("Please enter a number")


if __name__ == "__main__":
    guess_the_number()
