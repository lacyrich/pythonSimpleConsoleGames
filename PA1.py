# -*- coding: utf-8 -*-    
"""
Created on Sun Sep  3 15:42:51 2023

@author: lacyr
"""
#Each game is in its own py file 
#Bonus: ascii art for rock paper scissors game, a second currency calculator, and an extra game

import rockPaperScissors
import currencyCalculator
import drawShapes
import guessTheNumber


def main():                     #main menu - calls all the games
    display_menu()
    menu_choice = input('Enter your choice: ')
    while menu_choice != "5":
        if menu_choice == "1":
            rockPaperScissors.rock_paper_scissors()
        elif menu_choice == "2":
            drawShapes.draw_shapes()
        elif menu_choice == "3":
            currencyCalculator.currency_calculator()
        elif menu_choice == "4":
            guessTheNumber.guess_the_number()
        else: 
            print("Please enter a valid menu choice")
        display_menu()
        menu_choice = input('Enter your choice: ')

def display_menu() :                #shows menu options to user when called

    print("1. Play Rock, Paper, Scissors")
    print("2. Draw Shapes")
    print("3. Currency Calculator")
    print("4. Guess the Number")
    print("5. Exit")

 
main()
