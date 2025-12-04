
# FUNCTIONS

def prompt(message):
    print(f'==> {message}')


def mortgage_calculator():

    prompt('What was your total loan amount? ')
    loan_amount = float(input())

    prompt('What is your annual percentage rate? (APR) ')
    annual_perctage_rate = float(input())

    prompt('What is your loan duration in months? ')
    loan_duration = float(input())

    interest_rate_monthly = annual_perctage_rate / 100 / 12

    monthly_payment = loan_amount * (interest_rate_monthly / 
                                (1 - (1 + interest_rate_monthly) ** 
                                (-loan_duration)))
    
    yearly_payment = monthly_payment * 12
    total_payment = yearly_payment * (loan_duration / 12)

    prompt(f'Your monthly payment comes out to: {monthly_payment:.2f}, that is {yearly_payment:.2f} per year!')
    prompt(f'Your total payment is {total_payment:.2f}')


# START

mortgage_calculator()