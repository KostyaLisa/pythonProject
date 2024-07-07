import tkinter as tk
from random import random

from Aulas.Solulion.ExampeleGraphic import result_label


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

            result_label.config(text=f"Результат: {guessesTaken}")

        except ValueError:
            print("Please enter a number")



root = tk.Tk()
root.title("Guess Number")

# Создание и размещение виджетов


root.mainloop()

