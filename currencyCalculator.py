# -*- coding: utf-8 -*-

import math

# Gives user two options for type of currency calculator, then calls the appropriate calculator into effect
def currency_calculator() :
    print("1. Dollars to currency - breaks dollar amount down into dollars, quarters, dimes, nickels, and pennies") 
    print("2. Currency to dollars - enter number of dollars, quarters, dimes, nickels, and pennies and get total amount of money")
    calculator = input("Enter your choice: ")
    while calculator !="1" and calculator != "2": #makes sure that user enters a valid option
        print("1. Dollars to currency - breaks dollar amount down into dollars, quarters, dimes, nickels, and pennies ")
        print("2. Currency to dollars - enter number of dollars, quarters, dimes, nickels, and pennies and get total amount of money")
        calculator = input("Enter your choice: ")
    if calculator == "1":
        dollars_to_currency()
    else:
        currency_to_dollars()

# This is the calculator for the assignment. It takes a dollar amount with cents and tells you how many dollars, quarters, nickels, dimes, and pennies there are
def dollars_to_currency() : 
    while True:
        dollar_amount = input("Please enter an amount of money greater than 0, example: 5.66: ")
        try:
            dollar_amount = float(dollar_amount)
            if dollar_amount > 0:
                break
            else:
                print("Invalid input. The amount must be greater than 0")
        except ValueError:
            print("Invalid input. The amount must be a numeric value")
    cents_left = dollar_amount%1                        
    dollars = math.floor(dollar_amount - cents_left) #gets dollars
    cents_left = round(cents_left, 2)
    if cents_left*100 >= 25:                            #gets all coins if there is at least one quarter
        quarters = math.floor((cents_left * 100)/25)
        cents_left = (cents_left * 100)%25
        if cents_left >= 10:
            print(cents_left)
            dimes = math.floor(cents_left/10)
            cents_left = cents_left%10
        else:
            dimes = 0
        if cents_left >= 5:
            nickels = math.floor(cents_left/5)
            cents_left = cents_left%5
        else:
            nickels = 0
        if cents_left >= 1:
            pennies = math.floor(cents_left/1)
            cents_left = cents_left%1
        else:
            pennies = 0
    elif cents_left*100 >= 10:                  #if no quarters, gets all remaining coins starting with dimes
        quarters = 0
        dimes = math.floor(cents_left/10)
        cents_left = cents_left%10
        if cents_left >= 5:
            nickels = math.floor(cents_left/5)
            cents_left = cents_left%5
        else:
            nickels = 0
        if cents_left >= 1:
            pennies = math.floor(cents_left/1)
            cents_left = cents_left%1
        else:
            pennies = 0
    elif cents_left*100 >= 5:                   #if no dimes or quarters, gets all remaining coins starting with nickels
        quarters = 0
        dimes = 0
        nickels = math.floor(cents_left/5)
        cents_left = cents_left%5
        if cents_left >= 1:
            pennies = math.floor(cents_left/1)
            cents_left = cents_left%1
        else:
            pennies = 0
    elif cents_left*100 >= 1:                   #if no nickels, dimes, or quarters, gets pennies
        quarters = 0
        dimes = 0
        nickels = 0
        pennies = math.floor((cents_left * 100)/1)
        cents_left = (cents_left * 100)%1
    else:                                       #if no coins, sets all coins to 0
        quarters = 0
        dimes = 0
        nickels = 0
        pennies = 0
    print(f"Dollars: {dollars}")            #displays currency
    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels {nickels}")
    print(f"Pennies: {pennies}")
    input("Press enter to continue...")  
       
#This is a bonus calculator that allows a user to enter how many dollars, quarters, dimes, nickels, and pennies they have and be given how much money they have total
def currency_to_dollars():
    dollars = input("Enter the number of dollars you have as an integer: ") 
    while not dollars.isdigit():
        dollars = input("Invalid input. Enter the number of dollars you have as an integer: ") 
    quarters = input("Enter the number of quarters you have as an integer: ")
    while not quarters.isdigit():
        quarters = input("Invalid input. Enter the number of quarters you have as an integer: ") 
    dimes = input("Enter the number of dimes you have as an integer: ")
    while not dimes.isdigit():
        dimes = input("Invalid input. Enter the number of dimes you have as an integer: ") 
    nickels = input("Enter the number of nickels you have as an integer: ") 
    while not nickels.isdigit():
        nickels = input("Invalid input. Enter the number of nickels you have as an integer: ")
    pennies = input("Enter the number of pennies you have as an integer: ")
    while not pennies.isdigit():
        pennies = input("Invalid input. Enter the number of pennies you have as an integer: ")
    dollars = int(dollars)*100
    quarters = int(quarters)*25
    dimes= int(dimes)*10
    nickels = int(nickels)*5
    pennies = int(pennies)
    total_dollars = (dollars+quarters+dimes+nickels+pennies)/100
    print(f"Total Dollars: {total_dollars}")        #displays total dollar amount
    input("Press enter to continue...")
    

