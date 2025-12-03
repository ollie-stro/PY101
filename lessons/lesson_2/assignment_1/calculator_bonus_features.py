# FUNCTIONS

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

def calculator():
    prompt('Welcome to Calculator!')

    prompt("What's the first number? ")
    number1 = input()

    while invalid_number(number1):
        prompt("That doesn't seem like a valid number! Try again.")
        number1 = input()

    prompt("What's the second number? ")
    number2 = input()

    while invalid_number(number2):
        prompt("That doesn't seem like a valid number! Try again.")
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

    prompt('Would you like to perform another calculation? (Y/N)')
    
    while True:
        another_calc = input().upper()
        if another_calc == ('Y'):
            calculator()
        elif another_calc == ('N'):
            prompt('Thank you for using Calculator!')
            break
        else:
            prompt('Please enter a valid input! (Y/N)')

# START

calculator()
