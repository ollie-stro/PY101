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
        float(number_str)
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

def calculator():

    prompt(data["language"][language]["welcome"])

    prompt(data["language"][language]["valid_num"])
    number1 = input()

    while invalid_number(number1):
        prompt(data["language"][language]["invalid_num_error"])
        number1 = input()

    prompt(data["language"][language]["valid_num_2"])
    number2 = input()

    while invalid_number(number2):
        prompt(data["language"][language]["invalid_num_error"])
        number2 = input()

    prompt(data["language"][language]["operation_choice"])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(data["language"][language]["invalid_operation"])
        operation = input()


    match operation:
        case '1':
            output = float(number1) + float(number2)
            prompt(f'{number1} + {number2} is: {output:.2f}')
        case '2':
            output = float(number1) - float(number2)
            prompt(f'{number1} - {number2} is: {output:.2f}')
        case '3':
            output = float(number1) * float(number2)
            prompt(f'{number1} * {number2} is: {output:.2f}')
        case '4':
            output = float(number1) / float(number2)
            prompt(f'{number1} / {number2} is: {output:.2f}')

    prompt(data["language"][language]["another_calc"])
    prompt(data["language"][language]["lang_pref"])
    while True:
        another_calc = input().upper()
        if another_calc == ('Y'):
            calculator()
            break
        elif another_calc == ('N'):
            prompt(data["language"][language]["thank_you"])
            break
        elif another_calc == ('L'):
            choose_lang()
            prompt(data["language"][language]["another_calc"])
            prompt(data["language"][language]["lang_pref"])
        else:
            prompt(data["language"][language]["valid_input_error"])

# START

choose_lang()
calculator()
