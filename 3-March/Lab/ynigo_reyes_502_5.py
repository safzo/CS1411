# Miggy Reyes
# Texas Tech University
# CS 1411 - 502

from math import floor

def problem_1():
	# Takes the user's input as a string
	user_input = list(input("What is the string that you want to slice?: "))

	for index, value in enumerate(user_input):	# Enumerate is used to complete operation in O(n) time
		if index < 2:							# Prints out the first two letters by checking the index
			print(value, end="")
		elif index > len(user_input) - 3:		# Prints out the last two letters by checking if the index
			print(value, end="")				# is 3 less than the length of the string provided
	print()

def problem_2():
	n = int(input("Please provide n for problem 2: "))
	# Creates the first n x n array filled with .'s
	arrayOfN = [["."] * n] * n
	print("\nThis is the 1st array")
	prettyPrint(arrayOfN)

	if n % 2 == 0:	# Will round n to an odd number so that we are able to get
		n += 1		# get a valid middl0 row and column

	print("This is the second array")
	arrayOfNPlusOne = [["."] * n for i in range(n)]

	for row in range(n):				# Loops through the rows
		for col in range(n):			# Loops through the columns

			if row == col:
				arrayOfNPlusOne[row][col] = "*"
			elif row + col == n - 1:
				arrayOfNPlusOne[row][col] = "*"

			elif row == floor(n / 2):
				arrayOfNPlusOne[row][col] = "*"
			elif col == floor(n / 2):
				arrayOfNPlusOne[row][col] = "*"

	prettyPrint(arrayOfNPlusOne)


def prettyPrint(array):
	for row in array:
		print(" ".join(str(elem) for elem in row))

def problem_3():
    # This is the Caesar Encryption Problem

    # Takes the user's input
    # phrase is a string that will will be encoded
    # shiftValue is the amount of shifting needed
    phrase = input('What phrase would you like to encode?: ')

    # Input validation for shiftValue
    validChoice = False
    print('What is the shift value?: ', end="")
    while not validChoice:
        shiftValue = input('')

        if not shiftValue.isdigit():
            print('Please give an integer: ', end="")
        else:
            shiftValue = int(shiftValue)
            validChoice = True

    # This is where we will store the encoded characters
    encodedPhrase = []

    for character in phrase:

        # The Cyclic Shift
        #
        # We consider A and a to be 0. This is what we will base the cycle off of
        # We set them to 0 by subtracting the ASCII values of capital and lowercase letters
        # by 65 and 97, respectively. We apply the shift value and then take the
        # modulus of the sum so that if the letter is Z (#25) and we add 1, it will return
        # 0, which is the representation of A. We then add 65 or 97 depending on
        # whether or not it is capital or lowercase.
        if ord(character) >= 65 and ord(character) < 123:

            if ord(character) >= 65 and ord(character) < 97:
                ordChar = chr((((ord(character) - 65) + shiftValue) % 26) + 65)

            elif ord(character) >= 97 and ord(character) < 123:
                # It is lowercase
                ordChar = chr((((ord(character) - 97) + shiftValue) % 26) + 97)

            encodedPhrase.append(ordChar)

        else:
            # If the character is not a part of the alphabet
            encodedPhrase.append(character)

    print('The encoded word using a shift value of {} is... \n{}'.format(shiftValue, ''.join(encodedPhrase)))

def problem_4(listOfNumbers):

    # Base Case
    if not listOfNumbers:
        print()         # When we reach the end of the list, return nothing
        return

    else:
        print(listOfNumbers[-1], end=" ")   # Read the last element of the list
        del listOfNumbers[-1]               # Delete the last element
        return problem_4(listOfNumbers)     # Pass the new list recursively

def problem_5():

    # Configs for the game

    turn = "Player1"    # Determines who's turn it is
    totalStones = 100   # Number of stones needed to get picked up for game to end
    maxChoice = 5       # Max amount of stones a user can pick up at one time
    minChoice = 1       # Min amount of stones a user can pick up at one time

    print('This is a game of Picks and Stones!')

    gameProgress = True
    while gameProgress: # Game Loop

        # Keeps track of the current progress of the game
        print("\n{}, pick up some stones. You can pick between 1 and 5".format(turn))
        print("There are {} stones left in the game!".format(totalStones))


        validChoice = False             # This is our Choice Loop
        while not validChoice:          # We determine whether or not the user has
            userChoice = input('>> ')   # given a valid answer by checking if it is
                                        # an integer and between min and maxChoice
            if userChoice.isdigit():
                if int(userChoice) >= minChoice and int(userChoice) <= maxChoice and int(userChoice) <= totalStones:
                    validChoice = True
                else:
                    print("\nPlease input a value between {} and {} and less than the remaining amount if less than {} left.".format(minChoice, maxChoice, maxChoice))
            else:
                print('\nPlease input an integer.')

        totalStones -= int(userChoice)

        if totalStones == 0:    # When there are no more stones left...
            print("\n{}! You are the winner!".format(turn))
            break

        if turn == "Player1":   # This is what will change the player turns
            turn = "Player2"    # throughout the game
        elif turn == "Player2":
            turn = "Player1"


if __name__ == '__main__':
    # problem_1()
    # problem_2()
    # problem_3()

    # # Required input format:
    # # "1 2 4 6 7 0" without quotes, the 0 is required
    # listOfNumbers = list(map(str, (input("Give me a list of numbers: ").strip().split(' '))))
    # problem_4(listOfNumbers)

    problem_5()
