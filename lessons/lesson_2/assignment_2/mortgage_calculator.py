#MODULES

import json

with open("mortgage_calculator.json", "r") as configfile:
    data = json.load(configfile)

# FUNCTIONS

def prompt(message):
    print(f'==> {message}')


def get():
    user_input = input('> ' )
    print('')
    return user_input

def invalid_float(number_str):
    try:
        float(number_str)
        if number_str == '0':
            prompt(data["invalid_num_error_0"])
            return True
    except ValueError:
        return True

    return False


def prompt_for_number(key):
    prompt(data[key])
    number = get().strip()

    while invalid_float(number):
        prompt(data["invalid_num_error"])
        number = get().strip()

    return float(number)


def mortgage_calculator():

    prompt(data["welcome"])
    prompt(data["description"])


    loan_amount = prompt_for_number("loan_amount")
    annual_percentage_rate = prompt_for_number("annual_percentage_rate")
    loan_duration = prompt_for_number("loan_duration")


    interest_rate_monthly = annual_percentage_rate / 100 / 12
    month_pay = loan_amount * (interest_rate_monthly /
                                (1 - (1 + interest_rate_monthly) **
                                (-loan_duration)))
    year_pay = month_pay * 12
    total_payment = year_pay * (loan_duration / 12)


    print(data["separator"])
    prompt(f'{data["monthly_yearly_payment"]}{month_pay:.2f}, that is £{year_pay:.2f} per year!')
    prompt(f'{data["total_payment"]}{total_payment:.2f}')
    print(data["separator"])
    prompt(data["thank_you"])


# START

mortgage_calculator()
