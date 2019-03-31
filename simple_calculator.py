activate = True
user_choices=['Yes', 'y', 'No', 'n']

import math
print("A simple calculator")


def sum (m1, m2):
    return (m1 + m2)
def min (m1, m2):
    return (m1 - m2)
def multiple (m1, m2):
    return (m1 * m2)
def div (m1, m2):
    return (m1 / m2)
def square_root (m):
    return math.sqrt(m)
def square (m):
    return (m * m)
while True:
    operation = input("operations :\n 1: Addittion \n 2: Subtraction \n 3: Multiplication \n 4: Division \n 5: Squaroot \n 6: Square \n Choose an operation: \n")

    if operation == "1":
        m1 = int(input("Enter First Number: "))
        m2 = int(input("Enter Second Number: "))
        print("Answer : ", m1 + m2)
    elif operation == "2":
        m1 = int(input("Enter First Number: "))
        m2 = int(input("Enter Second Number: "))
        print("Answer : ", m1 - m2)
    elif operation == "3":
        m1 = int(input("Enter First Number: "))
        m2 = int(input("Enter Second Number: "))
        print("Answer : ", m1 * m2)
    elif operation == "4":
        m1 = int(input("Enter First Number: "))
        m2 = int(input("Enter Second Number: "))
        print("Answer : ", m1 / m2)
    elif operation == "5":
        m = int(input("Enter Number: "))
        print("Answer : ", math.sqrt(m))
    elif operation == "6":
        m = int(input("Enter Number: "))
        print("Answer : ", m * m)
    else:
        print("There is no such operation")


    user_input=input('Do you want to continue? ')

    if user_input.lower() == user_choices[0].lower() or user_input.lower==user_choices[1].lower():
        continue
    else:
        print('Thanks for using this Simple Calculator')
        activate=False
