
# MODULES

import random


# CONSTANTS

VALID_CHOICES = [ 'rock', 'paper', 'scissors', 'spock', 'lizard']
VALID_ABBREVIATIONS = ['r', 'p', 'sc', 'sp', 'l']

# FUNCTIONS

def prompt(message):
    print(f"==> {message}")

def display_options():
    nested_incrementer = 0

    for option in VALID_CHOICES:
        prompt(f'{option} ({VALID_ABBREVIATIONS[nested_incrementer]}),')
        nested_incrementer += 1

def choice_converter(choice):
    
    match choice:
        case 'r':
            choice = 'rock'
        case 'p':
            choice = 'paper'
        case 'sc':
            choice = 'scissors'
        case 'sp':
            choice = 'spock'
        case 'l':
            choice = 'lizard'  

def display_winner(choice, computer_choice):
   
    choice_converter(choice)

    if (choice == 'rock' and computer_choice  in ('scissors', 'lizard') or
        choice == 'paper' and computer_choice in ('rock', 'spock') or
        choice == 'scissors' and computer_choice in ('paper', 'lizard') or
        choice == 'spock' and computer_choice in ('rock', 'scissors') or
        choice == 'lizard' and computer_choice in ('paper', 'spock')):
        prompt('You win!\n')
    elif choice == computer_choice:
        prompt("It's a tie!\n")
    else:
        prompt("You lose!\n")

def rock_paper_scissors():
    while True:

        prompt('Welcome to Rock, Paper, Scissors, Lizard, Spock!\nPlease pick from the following:\n')
        display_options()

        choice = input()
        while choice not in (VALID_CHOICES) and choice not in (VALID_ABBREVIATIONS):
            prompt("That's not a valid choice! Try again")
            choice = input()

        computer_choice = random.choice(VALID_CHOICES)
        display_winner(choice, computer_choice)

        while True:
            prompt('Would you like to play again? (y/n)')
            play_again = input().lower()

            if play_again in ('y', 'n'):
                break
            else:
                prompt('You must enter a valid letter')
        
        if play_again == 'n':
            break


# START

rock_paper_scissors()

