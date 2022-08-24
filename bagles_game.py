# -------------------------------------------------------------------------------
# Name:        Bagels Game
# Purpose:     Fun/Games
#
# Author:      rnicolescu
#
# Created:     24/08/2022
# Copyright:   (c) rnicolescu 2022
# Licence:     <your license here>
# ------------------------------------------------------------------------------
import random

print('''
    Bagels, a deductive logic game.

    I am thinking of a digit number. Try to guess what it is.
    Here are some clues:
    When I say:         That means:
    Pico        --->     One digit is correct but in the wrong position.
    Fermi       --->     One digit is correct and in the right position.
    Bagels      --->     No digit is correct.
    I have thought up a number.
    You have 10 guesses to get it.
    ''')
DIGITS = 3
LIFES = 10

def getsecretNum():
    number_list = list('0123456789')
    random.shuffle(number_list)
    secretNum = ''
    for i in range(DIGITS):
        secretNum += str(number_list[i])

    return secretNum

def getClues(guess,secretNum):

    if guess == secretNum:
        return 'Correct! You won!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append(('Fermi'))
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagles'
    else:
        clues.sort()
        return ' '.join(clues)


def main():
    game_is_on = True
    while game_is_on:
        
        secretNum = getsecretNum()

        print(f'I am guessing at a number...\nYou have {LIFES} guesses to get it')
        numGuesses = 1
        while numGuesses <= LIFES:
            guess = ''
            while len(guess) != DIGITS or not guess.isdecimal():
                print(f'Guess #{numGuesses}:')
                guess = input(">  ")
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > LIFES:
                print(f"You have no more guesses.\nThe answer was {secretNum}")

        question = input('You want to play again? (yes/no)').lower()
        if not question.startswith('y'):
            break


if __name__ == "__main__":
    main()