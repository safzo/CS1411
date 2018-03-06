# Miggy Reyes
# Texas Tech University
# CS 1411 - 502

def problem_1(stringVariable):
    if len(stringVariable) % 2 == 1: changeLengthBy = 1  # If the length of the string is odd,
    													 # reduce the length of the secondHalf by 1
    													 # and have the first have get the middle char

    else: changeLengthBy = 0                             # If the length of the string is even,
    													 # slice the string normally

    firstHalf = stringVariable[:(len(stringVariable) // 2) + changeLengthBy]    # increases the length of the string if odd
    secondHalf = stringVariable[(len(stringVariable) // 2) + changeLengthBy:]   # only read the last half of the string

    print(secondHalf, end="")      # Print the secondHalf
    print(firstHalf)               # Print the firstHalf

def problem_2(stringVar):
    listStringVar = list(stringVar)   # Creates a list out of the string we pass to the function
    del listStringVar[1::2]           # Deletes all of the odd indices in that list
    print("".join(listStringVar))     # Joins the list back together with the nothing in between the elements

def problem_3(testWord):

    answers = dict()                    # Creates a dictionary that will store
    									# our answers

    for i in testWord:                  # Checks to see if the letter has been recorded before and adds to the counter
        if i in answers.keys():         # If the letter has not been recorded, we will start counting from 1
            answers[i] += 1
        elif i not in answers.keys():
            answers[i] = 1

    for answer in answers.keys():       # Prints out in the requested format
        print(str(answers[answer]) + " times " + answer)

def problem_4():
    correct = True           # Error handling without a try statement
    while correct:   		 # Until the user gives 10 numbers with spaces in between
        print("Format: number1 space number2 space ... etc. \n")   # Display formatting

		# Gets the user's input as a list of numbers.
		# I used map because I needed all of the inputs to be integers
		# I used strip and split as a way for the user to easily input 10 numbers (HackerRank Style)
		# I had the input turned into a list
		# I sorted the list so that I Only have to go through the list once
        listOfNumbers = sorted(list(map(int, (input("Give me a list of 10 numbers: ").strip().split(' ')))))


        if len(listOfNumbers) == 10: break						# If the user gave 10 numbers in the correct format, move on
        elif len(listOfNumbers) != 10:							# Ask the user to try again if they did not
            print("You did not give a list of 10 numbers")
            continue

    print(listOfNumbers[0])		# Print the number in the first index of the sorted list (smallest value)
    print(listOfNumbers[-1])	# Print the number at the end of the sorted list (largest value)
    print(sum(listOfNumbers))	# Print out the sum of the sorted list using the sum function

def problem_5():

	# Gets the user's input as a list of numbers.
	# I used map because I needed all of the inputs to be integers
	# I used strip and split as a way for the user to easily input numbers (HackerRank Style)
	# I had the input turned into a list

	# Sample Input format: "1 3 5 6 7" without the commas
	listOfNumbers = list(map(int, (input("Give me a list of numbers: ").strip().split(' '))))

	for index, value in enumerate(listOfNumbers):
		if index == 0:                                          # Skip the first index since there is nothing to compare it to
			continue                                            # This is also to avoid index errors comparing to later iterations
		elif listOfNumbers[index] > listOfNumbers[index - 1]:   # Compare the current iteration to the previous one
			print(value)


def problem_6():
	answers = dict()                    # Creates a dictionary that will store our answers

    # Gets the user's input as a list of numbers.
	# I used map because I needed all of the inputs to be integers
	# I used strip and split as a way for the user to easily input numbers (HackerRank Style)
	# I had the input turned into a list

	# Sample Input format: "1 3 5 6 7" without the commas
	listOfNumbers = list(map(int, (input("Give me a list of numbers: ").strip().split(' '))))

	for i in listOfNumbers:             # Checks to see if the number has been recorded before and adds to the counter
		if i in answers.keys():         # If the number has not been recorded, we will start counting from 1
			answers[i] += 1
		elif i not in answers.keys():
			answers[i] = 1

	for answer in answers.keys():       # Prints out in the requested format
		if answers[answer] == 1:        # Answer is a certain key, while answers is the dictionary
			print(answer)

if __name__ == '__main__':

    testWord = "Hello World"

    problem_1(testWord)
    problem_1(testWord)
    problem_2(testWord)
    problem_3(testWord)
    problem_4()
    problem_5()
    problem_6()
