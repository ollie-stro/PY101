#MODULES

import json

with open("mortgage_calculator.json", "r") as configfile:
    data = json.load(configfile)

# FUNCTIONS

def prompt(message):
    print(f'==> {message}')


def get():
    user_input = input('> ')
    print('')
    return user_input


def mortgage_calculator():

    prompt(data["welcome"])
    prompt(data["description"])


    prompt(data["loan_amount"])
    loan_amount = float(get())

    prompt(data["annual_percentage_rate"])
    annual_percentage_rate = float(get())

    prompt(data["loan_duration"])
    loan_duration = float(get())

    interest_rate_monthly = annual_percentage_rate / 100 / 12

    monthly_payment = loan_amount * (interest_rate_monthly / 
                                (1 - (1 + interest_rate_monthly) ** 
                                (-loan_duration)))
    
    yearly_payment = monthly_payment * 12
    total_payment = yearly_payment * (loan_duration / 12)

    print(data["separator"])
    prompt(f'{data["monthly_yearly_payment"]}{monthly_payment:.2f}, that is £{yearly_payment:.2f} per year!')
    prompt(f'{data["total_payment"]}{total_payment:.2f}')
    print(data["separator"])
    prompt(data["thank_you"])


# START

mortgage_calculator()
