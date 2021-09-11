def whetherWant() -> bool:
	"""
	Function checks whther user want to play this game.

	Arguments:
	---------
		Function don't take arguments

	Returns:
	-------
		bool -> 'True' if user want to play this game. Otherwise function returns 'False'

	Execptions:
	----------
		If user input only 'Enter' or not only alphabetic symbols or anyway function don't be able
			to understand answer two times, then automatically go out the game.
	"""

	GREETING = """
	***********************************************
	*HI! THIS IS THE GAME 'Human Guessing Number!'*
	***********************************************
	"""
	print(GREETING.center(50)) #transfer the string into the center with a specific size
	print()
	whetherWant = input(("Do you want to play this game?([Y]es or N[o]): "))
	whetherWant = whetherWant.replace(" ", "").lower() #make the string lowercase and without white spaces
	if not whetherWant or not whetherWant.isalpha(): 
		#if user input only 'Enter' or input not contains only alphabetic symbols
		whetherWant = input("You must be Enter 'Y[es]' if you want to play or 'N[o]' if you don't want to play: ")

	elif whetherWant not in ("n", "not", "no", "y", "yes", "yeah", "yed"):
		whetherWant = input("I don't understand. Please Enter your answer angain (Y[es] or N[o]): ")

	if whetherWant in ("n", "not", "no"):
		return False
	elif whetherWant in ("y", "yes", "yeah", "yed", "ues", "ies", "ied", "oes"):
		return True




def randomNumberGenerator(fromWhere: int, toWhere:int) -> int:
	"""
	Function generates random number from specific range.

	Arguments:
	---------
		positional:
		----------
			fromWhere : int -> low border from where function must be generate random number
			fromTo    : int -> high border to where function must be generate random number

	Returns:
	-------
		int -> Random number from specific range.
	"""

	from random import randint
	randomNumber = randint(min(fromWhere, toWhere), max(fromWhere, toWhere))

	return randomNumber




def getNumber(anyInput : str = "") -> int:
	"""
	Function takes integer from user.

	Arguments:
	--------
		positional:
		----------
			Not positional arguments

		optional:
		--------
			anyInput : str -> Thats a input what function be show user time to taking integer.
							  It have a default value empty string
	"""

	num = input(anyInput)
	num = num.replace(" ", "") #delete all white spaces

	if not num.isdigit() and num.lower() not in ("x", "exit"):
		#if input doesn't contains only digits (0 - 9) or not 'x' or 'exit'
		return getNumber("You must be intput a integer of said range or 'X' for exit the game! : ")
	elif num.lower() in ("x", "exit"):
		return num.lower()
	return int(num)




def gameLogic(level = 0):
	"""
	This function contains all logic of the game.
		The function takes one optional argument 'level', which have a default value: '0'
		If 'level' greater than 4, or user input is in ('x', exit) then the function automatically returns 'None'
	"""

	if level > 4:
		return
	allLevels = [1, 2, 3, 4, 5] #all possible levels of this game
	#ranges from where the user must be guess number
	numberRanges = [(1, 10), (1, 20), (1, 30), (1, 40), (1, 50)]
	#generates random number from the appropriate domain for each level
	randomNumber = randomNumberGenerator(*numberRanges[level])

	guess = getNumber(f"Guess a number between range {numberRanges[level][0]} to {numberRanges[level][1]} (Or 'X' for Exit the game): ")

	if guess in ("x", "exit"): #if user want to exit the game
		print("\t------------------------------------------------------")
		print("\t**********THANKS A LOT FOR YOUR TIME. BYE!!!**********")
		print("\t------------------------------------------------------")
		return
	
	try:
		"""
		This part let us understand the user's input near or far from number,
		wich computer keeping in memory and respond for each level appropriately
		"""
		lowRange = numberRanges[level][1] // 5
		while guess != randomNumber:
			if  abs(guess - randomNumber) <= lowRange:
				print("You're very near from the number that I remember!!")
				print("You're can do it I know:):):)!!")
				print("Please try again!")

			elif abs(guess - randomNumber) <= lowRange * 2 + 1:
				print("You're already quite near from the number that I remember!!")
				print("Please try again!")

			elif abs(guess - randomNumber) <= lowRange * 3 + 1:
				print("Unfortunately you havn't guess number!(:(:")
				print("You're still quite far  from the number that I remember!")
				print("Please try again!")

			elif abs(guess - randomNumber) <= lowRange * 4 + 1:
				print("Unfortunately you havn't guess number!(:(:")
				print("You're so far from the number that I remember!")
				print("Please try again!")
				
			
			guess = getNumber(f"Guess a number between range {numberRanges[level][0]} to {numberRanges[level][1]} (Or 'X' for Exit the game): ")
			

		print("\t********************************")
		print("\t*GOOD GUESSED! CONGRATULATIONS!*")
		print("\t********************************")

		if level != 4: #if the user doesn't in the last level
			print("\t\tYOU HAVE PASSED THE NEXT LEVEL!!!")
			print("\t\t=================================")
			print(f"\t\t\tLEVEL {level + 2}")
		else:
			print("\t\tCONGRATULATIONS!!!! YOU WIN THIS GAME!!!!")

			#this part just printing the heart of stars if the user passed all levels
			s = ""
			for row in range(6):
				for col in range(7):
					if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0)\
					    or (row - col == 2) or (row + col == 8):
					    s += "*"
					else:
						s += " "
				s += "\n"
			print(s) #print the heart of stars

	except Exception as e:
		print("Sorry you're probably not typing something correctly. Please try again!")
		print(e)
		
	finally:
		level += 1
		return gameLogic(level)
		


	

def startGame():
	"""
	Function check whether user want to play this game and if the answer is 'yes',
		then called function 'gameLogic()'
	"""

	print("\nOK! Let's play!")
	print("--------------------------------------------------------------------------------------")
	print("Note:")
	print("\tI keeping in my memory a random integer and you must be guessing that number!")
	print("\tI will help you!")
	print("--------------------------------------------------------------------------------------\n")
	print("\t\t\tLEVEL 1\n")
	gameLogic()




def game():
	"""
	Function call 'whetherWant()' function and check whether user want to play this game.
	If the answer is 'Yes', then called function 'startGame()' thus starting the game, otherwise
	function printed "Thanks anyway. Bye-bye!" and automatically returns 'None'
	"""
	
	if not whetherWant(): #if user don't want to play
		print("Thanks anyway. Bye-bye!")
	else:
		startGame()


