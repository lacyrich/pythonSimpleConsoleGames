# -*- coding: utf-8 -*-
import random

def rock_paper_scissors(): #determines computer's choice and asks user for their choice
    computer_rps_choice = random.randint(1,3)
    
    if computer_rps_choice == 1:
        computer = "rock"
    elif computer_rps_choice == 2:
        computer = "paper"
    else: 
        computer = "scissors"
    rps_choice = input("To play, please enter rock, paper, or scissors: ").lower()   
    while rps_choice != "rock" and rps_choice != "paper" and  rps_choice != "scissors" :
        rps_choice = input("Invalid input, please enter rock, paper, or scissors: ").lower()
    
    print("Player:" + rps_choice)
    print("vs")
    print("Computer:" + computer)
    if rps_choice == computer :
        print("The game is a Tie!!")
    #case where paper wins - determines if winner is player or computer  
    elif (rps_choice == "rock" or computer == "rock") and (rps_choice == "paper" or computer == "paper"):
        if rps_choice == "paper" :
            winner = "Player"
        else:
            winner = "Computer"
        paper()
        print("Paper beats rock, " + winner + " wins!!")
    #case where rock wins - determines if winner is player or computer  
    elif (rps_choice == "rock" or computer == "rock") and (rps_choice == "scissors" or computer == "scissors"):
        if rps_choice == "rock" :
            winner = "Player"
        else:
            winner = "Computer"
        rock()
        print("Rock beats scissors, " + winner + " wins!!")
    #case where scissors wins - determines if winner is player or computer   
    elif (rps_choice == "paper" or computer == "paper") and (rps_choice == "scissors" or computer == "scissors"):
        if rps_choice == "scissors" :
            winner = "Player"
        else:
            winner = "Computer"
        scissors()
        print("Scissors beats paper, " + winner + " wins!!")
              
    input("Press enter to continue...")
    
def rock():                 #ascii art for rock
    print("         ⣠⡴⠖⠒⠲⠶⢤⣄")
    print("     ⢀⡾⠁⠀⣀⠔⠁⠀⠀⠈⠙⠷⣤⠦⣤⡀")
    print("  ⣠⠞⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⠈⢿⡀⠀")
    print(" ⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠛⠛⠃⠸⡇⠈⣇")
    print("⣹⡷⠤⠤⠤⠄⠀⠀⠀⠀⢠⣤⡤⠶⠖⠛⠀⣿⠀⣿ ")
    print("⡟              ⣠⡤⠖⠋⢀⣿⣠⠏⠀")
    print("⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠁⠀")
    print("⠉⢿⡋⠉⠉⠁⠀⠀⠀⠀⠀⢀⣠⠾⠋⠀⠀⠀")
    print("⠀⠈⠛⠶⠦⠤⠤⠤⠶⠶⠛⠋⠁⠀")
def paper():                #ascii art for paper
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                            ⣠⡴⠖⠒⢶⣄⠀⠀⠀⠀⠀⠀⠀")
    print("                         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠋⠀⠀⠀⢀⡿⠀⠀⠀⠀⠀⠀⠀")
    print("                         ⢠⡶⠒⠳⠶⣄⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⣰⠏⠀⢀⣤⣤⣄⡀⠀⠀")
    print("                         ⠸⡇⠀⠀⠀⠘⣇⠀⠀⣠⡾⠁⠀⠀⠀⢀⣾⣣⡴⠚⠉⠀⠀⠈⠹⡆⠀")
    print("                         ⠀⢻⡄⠀⠀⠀⢻⣠⡾⠋⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀⠀⠀⢀⣠⡾⠃⠀")
    print("                        ⠀⠀⣿⠀⠀⠀⠘⠉⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⠀⠀⣠⠶⠋⠁⠀⠀⠀")
    print("                        ⠀⠀ ⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠁⠀⠀⠀⢀⣴⡿⠥⠶⠖⠛⠛⢶⡄")
    print("                      ⠀⠀⠀⢀⣰⡇⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⢀⣠⠼⠃")
    print("                   ⠀⠀⠀⠀⠀⣿⠉⣇⠀⡴⠟⠁⣠⡾⠃⠀⠀⠀⠀⠀⠈⠀⠀⠀⣀⣤⠶⠛⠉⠀⠀⠀")
    print("                       ⠀⠀⢻⡄⠹⣦⠀⠶⠛⢁⣠⡴⠀⠀⠀⠀⠀⠀⣠⡶⠛⠉⠀⠀⠀⠀⠀⠀⠀")
    print("                         ⠀⠻⣄⠈⢷⣄⠈⠉⠁⠀⠀⠀⢀⣠⡴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("                           ⠀⠉⠳⢤⣭⡿⠒⠶⠶⠒⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")  
def scissors():             #ascii art for scissors
    print("⠀⠀   ⢀⣠⣤⣀⣠⣤⠶⠶⠒⠶⠶⣤⣀")
    print("⠀⠀⢀⡴⠋⣠⠞⠋⠁⠀⠀⠀⠀⠙⣄⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⢀⡾⠁⣴⠋⠰⣤⣄⡀⠀⠀⠀⠀⠈⠳⢤⣼⣇⣀⣀")
    print("⠀⢸⠃⢰⠇⠰⢦⣄⡈⠉⠀      ⠈⠉⠉⠉⠛⠛⠓⠲⢦⣄")
    print("⠀⠸⣧⣿⠀⠻⣤⡈⠛⠳⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀")
    print("⠀⠈⠹⣆⠀⠈⠛⠂⠀⠀⠀⠀⠀⠀⠈⠐⠒⠒⠶⣶⣶⠶⠤⠤⣤⣠⡼⠃⠀⠀")
    print("⠀⠀⠀⠀⠹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠈⠻⣦⣀⠀⠀⠀⠀⠐⠲⠤⣤⣀⡀⠀⠀⠀⠀⠀⠉⢳⡄⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀  ⠀⠉⠛⠶⠤⠤⠤⠶⠞⠋⠉⠙⠳⢦⣄⡀⠀⠀⠀⡷⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠈⠙⠳⠦⠾⠃⠀⠀⠀⠀⠀")
