
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

    prompt('Please pick from the following:\n')

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

    return choice

def display_winner(choice, computer_choice, player_score, computer_score):

    choice = choice_converter(choice)
    prompt(f"You chose {choice}, computer chose {computer_choice}")

    if player_wins(choice, computer_choice):
        prompt('You win!\n')
        player_score += 1



    elif player_wins(choice, computer_choice) is None:
        prompt("It's a tie!\n")

    else:
        prompt("You lose!\n")
        computer_score += 1

    return player_score, computer_score

def player_wins(choice, computer_choice):

    if (choice == 'rock' and computer_choice  in ('scissors', 'lizard') or
        choice == 'paper' and computer_choice in ('rock', 'spock') or
        choice == 'scissors' and computer_choice in ('paper', 'lizard') or
        choice == 'spock' and computer_choice in ('rock', 'scissors') or
        choice == 'lizard' and computer_choice in ('paper', 'spock')):
        return True
    elif choice == computer_choice:
        return None
    else:
        return False

def display_scores(player_score, computer_score, game_over):

    if player_score == 3:
        prompt(f'Your score: {player_score}')
        prompt(f'Computer score: {computer_score}\n')
        prompt('You won! Computer has lost.')

        game_over = True
        return game_over

    elif computer_score == 3:
        prompt(f'Your score: {player_score}')
        prompt(f'Computer score: {computer_score}\n')
        prompt('Computer won! You have lost.')

        game_over = True
        return game_over

    else:
        prompt(f'Your score: {player_score}')
        prompt(f'Computer score: {computer_score}\n')
        return game_over

def rock_paper_scissors():

    run_game = True
    game_over = False

    player_score = 0
    computer_score = 0

    prompt('Welcome to Rock, Paper, Scissors, Lizard, Spock!\n')

    while run_game is True:

        display_options()

        choice = input()
        while choice not in (VALID_CHOICES) and choice not in (VALID_ABBREVIATIONS):
            prompt("That's not a valid choice! Try again")
            choice = input()

        computer_choice = random.choice(VALID_CHOICES)

        player_score, computer_score = display_winner(choice, computer_choice,
                                                       player_score, computer_score)

        game_over = display_scores(player_score, computer_score, game_over)

        while game_over is True:
            prompt('Would you like to play again? (y/n)')
            play_again = input().lower()

            if play_again == 'n':
                run_game = False
                game_over = False
                prompt('Thank you for playing rock, paper, scissors, lizard, spock!')

            elif play_again == 'y':
                player_score = 0
                computer_score = 0
                game_over = False
                break

            else:
                prompt('You must enter a valid letter')


# START

rock_paper_scissors()
