# -*- coding: utf-8 -*-
import random

#this is a fun guessing game where the computer comes up with a random number between 1 and 100.
#with each guess the computer will tell the user if their guess is too high or too low
def guess_the_number():
    number_to_guess = random.randint(1, 100)
    guess = input("Guess what number I am thinking of, between 1 and 100, inclusive. Please enter an integer for your guess: ")
    while not guess.isdigit() :
        guess = input("Invalid input. Please enter an integer for your guess: ")
    win = False
    while win is False:
        if int(guess)  == number_to_guess:
            print("You win!!")
            win = True
        elif int(guess) > number_to_guess:
            print("Your number is too high")
        else:
            print("Your number is too low")
        if win is True:
            input("Press enter to continue...")
        else:
            guess = input("Please enter your guess as an integer: ")
            while not guess.isdigit() :
                guess = input("Please enter your guess as an integer: ")