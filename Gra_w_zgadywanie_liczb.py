from random import randint


def guessed_number():
    """
    Getting number from user until receiving guessed number.
    :return: number as int.
    """
    while True:
        try:
            return int(input("Guess the number: "))
        except ValueError:
            print("It's not a number!")


def guess_the_number():
    """
    Guessing the right number, same as chosen number on base of hints
    based on the value given from guessed_number function.
    :return:
    """
    chosen_number = randint(1, 100)
    guessed = False
    while not guessed:
        number_too_choose = guessed_number()
        if number_too_choose < chosen_number:
            print("Too small!")
        elif number_too_choose > chosen_number:
            print("To big!")
        elif number_too_choose == chosen_number:
            guessed = True
            print("you win!")


if __name__ == "__main__":
    guess_the_number()
