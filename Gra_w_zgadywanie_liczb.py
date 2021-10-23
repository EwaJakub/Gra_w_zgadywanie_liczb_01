import random

def guessed_number():
    while True:
        try:
            guessed_number = int(input("Guess the number: "))
            return guessed_number
        except ValueError:
            print("It's not a number!")

chosen_number = random.choice(range(1, 101))

def guess_the_number():
    number_too_choose = guessed_number()
    if number_too_choose < chosen_number:
        print("Too small!")
        guess_the_number()
    elif number_too_choose > chosen_number:
        print("To big!")
        guess_the_number()
    elif number_too_choose == chosen_number:
        print("You Win!")


if __name__ == "__main__":
 guess_the_number()