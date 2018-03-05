def booleanExpression():  # Camel Case: This is naming convention. Again, not required, but programmers appreciate it
    # True and False are key words so there is no need to declare it
    cal = int(input("Please enter a number: "))

    # Notice the syntax of the if statement
    for i in range(2, cal):
        if cal % 1 == 0:
            return True  # True is a key word... Boolean expressions are a type of data type
        else:
            return False


if __name__ == '__main__':
    print(booleanExpression())
