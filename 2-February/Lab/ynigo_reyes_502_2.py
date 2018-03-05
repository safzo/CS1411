# Miggy Reyes
# Texas Tech University
# CS 1411 - 502
# 2/8/2018
import math
import random


def problem_1():
	print("Problem 1")

	a = 20    # This is a representation of our classroom
	b = 21
	c = 22

	# This is the list of the classrooms' student count 
	# so that I can run it through the for loop
	number_of_students = [a, b, c]

	# We need to instantiate "total" so that we have a starting point
	# when adding all of the desks together. We start adding from 0
	total = 0

	# Loops through the number of students in the classrooms
	for i in number_of_students:
		answer = math.ceil(i/2)
		print("For a classroom of {} kids, we need {} desks.".format(i, answer))
		# Adds each required number of desk into the "total" variable
		# to be printed once the loop has finished
		total += answer

	# Displays the final count
	print("In total we need {} desks for all three classrooms".format(total))


def problem_2():
	print("Problem 2")

	test_1 = 2000  # This is the representation of our years
	test_2 = 2012
	test_3 = 2100

	# This is the list of years that we will run through the for loop
	year = [test_1, test_2, test_3]

	# The for loop to test our years to see if they are leap years
	for i in year:
		# This is the 2nd bullet point on the question
		if (i % 400) == 0:
			print("{} is a leap year".format(i))
		# This is the 1st bullet point in the equation
		elif (i % 4) == 0 and (i % 100) != 0:
			print("{} is a leap year".format(i))
		# This is the default, since most years are not leap years
		else:
			print("{} is not a leap year".format(i))


def problem_3():
	# This generates a different number between 0 and 100 every time the program
	# is ran and the print statement will simply say what is being tested
	test_grades = math.ceil(random.randint(0, 100))
	print("The grade we are testing is {}".format(test_grades))

	# The grade is above a 60, we will determine what the letter grade is
	if test_grades >= 60:
		# These parameters are based on the question
		print("{} is a passing grade".format(test_grades))
		if test_grades >= 90 and test_grades <= 100:
			print("{} is an A".format(test_grades))
		elif test_grades >= 80 and test_grades < 90:
			print("{} is a B".format(test_grades))
		elif test_grades >= 70 and test_grades < 80:
			print("{} is a C".format(test_grades))
		elif test_grades >= 60 and test_grades < 70:
			print("{} is a D".format(test_grades))
		else:
			print("{} is a F".format(test_grades))
	# if it is bellow a 60, then we will only say that it is a failing grade
	else:
		print("{} is a failing grade, therefor it is a F.".format(test_grades))


def problem_4():
	# This is a list of denominators
	denominators = list(range(2, 11))
	list_of_fractions = []

	for i in denominators:
		# Adds the results of dividing by i to a list, ready to print
		list_of_fractions.append(1/i)

	# This will print out the answers
	print("This is the list the decimal equivalents for 1/2 to 1/10")
	print(list_of_fractions)


def problem_5():
	ask_again = True
	# This loop will keep running until the ask_again variable holds True
	while ask_again: # Takes the user input as an integer
		try:
			user_input = int(input("Give me a number that is divisible by 2: "))
			if user_input % 2 == 0:
				print("Congratz! You are a smart human being.")
				# We break the loop by saying that ask_again is False
				ask_again = False
			elif user_input % 2 != 0:
				# Since we are not changing the value of
				# ask_again, it will keep asking again
				print("WRONG! That's not divisible by two")

		except ValueError:
			print("That is not an integer...")


def problem_6():
	print("Welcome to the numbers guessing game!")
	# This will generate the random integer between 1 and 9
	random_number = random.randint(1, 9)
	user_input = "foobar"

	# Will break loop when the user's input is exit
	while user_input != "exit":
		user_input = (input("What number would you like to guess between 1 and 9: "))
		if user_input.isdigit():
			# Checks to see if the user input is a digit, and then runs the logic
			if int(user_input) == random_number:
				# Correct answer
				print("Congrats! You guessed {}, which is the correct answer.".format(random_number))
			elif int(user_input) > random_number:
				# Too high of a guess
				print("Too High!")
			elif int(user_input) < random_number:
				# Too low of a guess
				print("Too Low")
		else:
			if user_input == "exit":
				# Breaks the loop
				pass
			else:
				print("Please input a valid option")


if __name__ == "__main__":
	problem_1()
	problem_2()
	problem_3()
	problem_4()
	problem_5()
	problem_6()
