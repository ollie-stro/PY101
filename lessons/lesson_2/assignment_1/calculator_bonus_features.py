# MODULES

import json

with open("calculator_bonus_features.json", "r") as configfile:
    data = json.load(configfile)

# GLOBAL VARIABLES

language = ''


# FUNCTIONS

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False


def choose_lang():
    prompt('What is your preferred language、 English or Japanese? (1/2)')
    prompt('言語は何ですか、　英語か日本語？（１か２）')
    global language

    while True:
        lang_choice = input()
        if lang_choice == '1':
            language = 'en'
            break
        elif lang_choice == '2':
            language = 'jp'
            break
        else:
            prompt('Please select either 1 or 2!')
            prompt('１か２を選んでください！')
    print(language)

def calculator():

    prompt(data["language"][language]["welcome"])  #############

    prompt("What's the first number? ")
    number1 = input()

    while invalid_number(number1):
        prompt(data["language"][language]["invalid_num_error"]) #############
        number1 = input()

    prompt("What's the second number? ")
    number2 = input()

    while invalid_number(number2):
        prompt(data["language"][language]["invalid_num_error"]) ############
        number2 = input()

    prompt("""What operation would you like to peform?
1) Add\n2) Subtract\n3) Multiply\n4) Divide\n""")
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt('You must choose 1, 2, 3, or 4')
        operation = input()


    match operation:
        case '1':
            output = int(number1) + int(number2)
            prompt(f'The result of {number1} + {number2} is: {output}')
        case '2':
            output = int(number1) - int(number2)
            prompt(f'The result of {number1} - {number2} is: {output}')
        case '3':
            output = int(number1) * int(number2)
            prompt(f'The result of {number1} * {number2} is: {output}')
        case '4':
            output = int(number1) / int(number2)
            prompt(f'The result of {number1} / {number2} is: {output}')

    prompt(data["language"][language]["another_calc"])                            ##############

    while True:
        another_calc = input().upper()
        if another_calc == ('Y'):
            calculator()                                                # Nested calculator function call - NEEDS FIXING
        elif another_calc == ('N'):
            prompt(data["language"][language]["thank_you"])                     ##################
            break
        else:
            prompt('Please enter a valid input! (Y/N)')

# START

choose_lang()
calculator()
