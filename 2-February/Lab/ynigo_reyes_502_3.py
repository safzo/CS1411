import math
import random


def problem_1a():

    # This is the number triangle part
    n = 5  # 5 rows
    for i in range(1, n + 1):  # range is not inclusive so we need to add 1
        print()  # We need to make sure the next row is printed in the next line
        for j in range(1, i + 1):  # range is not inclusive... plus one
            # We put end so that the next j won't print on the next line
            print(j, end="")
    print('\n')

    # This is the star pyramid part


def problem_1b():
    n = 5  # of rows
    for i in range(1, n + 1):  # Create this many rows
        print(i * " ", end="")  # Print this many spaces
        if i == 5:
            print("*")
        elif i < 5:
            for j in range(0, n - i):  # prints out the amount of stars
                print("*", end="")  # print j amount of stars
            print(" ", end="")
            for k in range(0, n - i):
                print("*", end="")

        print()


def problem_2():
    ask_again = True  # allows the loop to run for the first time
    response = ""  # declare

    while ask_again is True:  # program loop
        print(
            """\nWhat would you like to do?\n
            1) Add\n
            2) Subtract\n
            3) Multiply\n
            4) Divide\n
            Type quit if you want to quit
            """)  # The options that the user sees
        response = input(">> ").upper(
        )  # Takes the response and saves it in response

        quit_statements = ["QUIT", "Q"]  # valid quit statements
        valid_options = ["1", "2", "3", "4"] + quit_statements  # valid options

        if response not in valid_options:  # if the user gives an invalid response
            print("Please input a valid option")
            continue

        elif response not in quit_statements:  # takes the user's input
            first_number = int(
                input("What number would you like to use? \n>> "))
            second_number = int(
                input("What is the next number you would like to use? \n>> "))
        elif response in quit_statements:  # if the user wants to quit...
            ask_again = False
            continue  # will close loop and end program with ask_again equalling false

        # These are the options for the use. These functions take the numbers
        # given and passes them on to their functions
        if response == "1":
            add(first_number, second_number)
        elif response == "2":
            subtract(first_number, second_number)
        elif response == "3":
            multiply(first_number, second_number)
        elif response == "4":
            divide(first_number, second_number)


def add(x, y):
    print(x + y)


def subtract(x, y):
    print(x - y)


def multiply(x, y):
    print(x * y)


def divide(x, y):
    print(x / y)


def problem_3a():
    ask_again = True
    while ask_again is True:
        # Same ask_again technique used above
        print("Give an integer")
        user_input = input(">> ")  # Gets the user's input
        if user_input.isdigit() is True:  # Checks to see if it is an integer
            # saves the return of the prime function
            result = prime(user_input)
            print(result)
        else:
            # If the user input is not an integer...
            print("That is not an integer")


def problem_3b():
    for number in range(1, 101):  # tests 1 to 100
        result = prime(number)
        if result is True:  # Displays only the prime numbers
            print("{} is a prime number".format(number))


def prime(integer):
    """This function is the algorithm we use to determine a prime number"""
    integer = int(integer)

    if integer <= 0:
        return "This is a negative number or 0"

    # If the integer cannot be divided by these numbers and are not these numbers
    # themselves, they are prime
    elif integer % 2 == 0 and integer != 2:
        return False
    elif integer % 3 == 0 and integer != 3:
        return False
    elif integer % 5 == 0 and integer != 5:
        return False
    elif integer % 7 == 0 and integer != 7:
        return False
    else:
        return True


def main_problem_4():
    print("The degreees function will convert radians(float) into degrees(float)")
    print("The hypot function takes in two numbers and find the hypotenuse of them")
    print("The ciel function takes a float and rounds it down to the nearest integer")
    print("The ciel function takes a or float and rounds it up to the nearest integer\n")

    user_input = float(input(("Give number>> ")))  # Casts the user's input to a float
    user_input_2 = ""  # Declate

    print("This is the radians in degrees: {}".format(math.degrees(user_input)))
    user_input_2 = float(input("hypot requries two numbers. What is the second number?: "))
    print("This is the hypotenuse of two sides of the triangle: {}".format(math.hypot(user_input, user_input_2)))
    print("The ceil for your first number is {}".format(math.ceil(user_input)))
    print("The floor for your first number is {}".format(math.floor(user_input)))


def problem_5():
    user_number = float(input("What number would you like the computer to guess?: "))
    correct = False
    tries = 0  # Declare
    a = 0  # Bottom of guessing range
    b = 100  # Top of guessing range

    while not correct:
        guess = random.randint(a, b)
        print("My guess is {}! Is that too 1)high or too 2)low or is it 3)correct?".format(guess))
        user_input = input(">> ")
        if user_input == "1":
            b = guess
        elif user_input == "2":
            a = guess
        elif user_input == "3":
            print("Your number is {}!!".format(guess))
            correct = True
        else:
            print("Please pick a valid option... Picking new number")

        tries += 1

    print("This took me {} tries".format(tries))


if __name__ == '__main__':
    # problem_1a()
    problem_1b()
    # problem_2()
    # problem_3a()
    # problem_3b()
    # main_problem_4()
    # problem_5()
