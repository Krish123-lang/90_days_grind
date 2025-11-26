import sys


def sum(a,b):
    return a+b 


def difference(a,b):
    return a-b


def product(a,b):
    return a*b


def divison(a,b):
    return a/b

num1=float(input("Enter number a: "))
num2=float(input("Enter number b: "))

while True:
    print("**************************************************************************************************************")
    oper_input = input("""What operation do you want to perform?
        a. Addition
        b. Subtraction
        c. Multiplication
        d. Division
        e. Quit
        """)

    if oper_input == 'A'.lower():
        print(f'The sum of {num1} and {num2} is: {sum(num1, num2)}')

    elif oper_input == 'B'.lower():
        print(f'The difference of {num1} and {num2} is: {difference(num1, num2)}')

    elif oper_input == 'C'.lower():
        print(f'The product of {num1} and {num2} is: {product(num1, num2)}')

    elif oper_input == 'D'.lower():
        print(f'The division of {num1} and {num2} is: {divison(num1, num2)}')
        
    elif oper_input == 'E'.lower():
        print('Bye Bye!')
        sys.exit(0)

    else:
        print("Something went wrong!")