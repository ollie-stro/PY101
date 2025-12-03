print('Welcome to Calculator!') # Print the result to the terminal

number1 = int(input("What's the first number? "))   # Ask the user for the first number
number2 = int(input("What's the second number? "))  # Ask the user for the second number

print(f'{number1} {number2}')

operation = input('What operation would you like to peform?\n1) Add\n2) Subtract\n3) Multiply\n4) Divide\n') # Ask the user for an operation to perform

if operation == '1':                             # Perform the operation on the two numbers
    output = number1 + number2
    print(f'The result of {number1} + {number2} is {output}')
elif operation == '2':
    output = number1 - number2
    print(f'The result of {number1} - {number2} is {output}')
elif operation == '3':
    output = number1 * number2
    print(f'The result of {number1} * {number2} is {output}')
else:
    output = number1 / number2
    print(f'The result of {number1} / {number2} is {output}')