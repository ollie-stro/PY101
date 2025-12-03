def prompt(message):
    print(f'==> {message}')

prompt('Welcome to Calculator!')

prompt("What's the first number? ")
number1 = int(input())

prompt("What's the second number? ")
number2 = int(input())


prompt('What operation would you like to peform?\n1) Add\n2) Subtract\n3) Multiply\n4) Divide\n')
operation = input()
match operation:
    case '1':
        output = number1 + number2
        prompt(f'The result of {number1} + {number2} is {output}')
    case '2':
        output = number1 - number2
        prompt(f'The result of {number1} - {number2} is {output}')
    case '3':
        output = number1 * number2
        prompt(f'The result of {number1} * {number2} is {output}')
    case '4':
        output = number1 / number2
        prompt(f'The result of {number1} / {number2} is {output}')