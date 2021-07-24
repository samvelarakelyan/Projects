def getAnswer(inp : str = "", num : int = None):
	"""
	This function get answer from user.

	Arguments:
	---------
		optional:
		--------
			inp : str -> Text which will be show user when getting input. Default value is ""
			num : int -> Number which will be show user when getting input. Default value is None


	Returns:
	-------
		bool -> 'True' if user's answer is positive otherwise 'False'


	Exceptions:
	-----------
		If the function can't understand the user's input two times then automatically returns 'None'
	"""

	answer = input(inp + " Y[es] or N[o]: ")
	answer = answer.replace(" ", "").lower() #make the string lowercase and without white spaces
	if not answer or not answer.isalpha(): 
		#if user input only 'Enter' or input not contains only alphabetic symbols
		if not num is None:
			answer = input(f"You must be Enter 'Y[es]' if your number is {num} or 'N[o]' otherwise: ")
		else:
			answer = input("You must be Enter 'Y[es]' if you want to play or 'N[o]' if you don't want to play: ")

	elif answer not in ("n", "not", "no", "y", "yes", "yeah", "yed"):
		answer = input("I don't understand. Please Enter your answer angain (Y[es] or N[o]): ")

	if answer in ("n", "not", "no"):
		return False
	elif answer in ("y", "yes", "yeah", "yed", "ues", "ies", "ied", "oes"):
		return True





def checkRange(currentNumRange: tuple, currentLevel: int):
	"""
	Function changes range dependent users answers.
	"""

	lowerNumber, higherNumber = currentNumRange[0], currentNumRange[1]
	mid = (higherNumber + lowerNumber) // 2
	ans = getAnswer(f"Does your number is greater than {mid}?", mid)

	if ans:
		lowerNumber = mid
	else:
		higherNumber = mid


	return (lowerNumber, higherNumber)





def gameLogic(level = 0):
	"""
	This function contains all logic of the game.
	The function takes one optional argument 'level', which have a default value: '0'
	If 'level' greater than 4, or user's answer the question 'OK: Do You want to continue this game? Am I waiting for you?'
	is 'N[o]', then the function automatically returns 'None'
	"""

	allLevels = [0, 1, 2, 3, 4] #all possible levels of this game
	#ranges where the user must choose a number from the appropriate domain for each level
	numberRanges = [(1, 500), (1, 1000), (1, 1500), (1, 2000), (1, 2500)] 
	if level > 4:
		return
	currentRange = numberRanges[level]
	
	print("\t\t\t***********************************************")
	print(f"\t\t\tKEEP IN YOUR MIND NUMBER FROM RANGE {currentRange[0]} to {currentRange[1]}!")
	print("\t\t\t***********************************************")
	ready = getAnswer("Are you ready?")
	print("\n")
	if ready:
		lowerNumber, higherNumber = numberRanges[level][0], numberRanges[level][1]
		rightAnswer = False
		while (higherNumber > numberRanges[level][0] or higherNumber < numberRanges[level][1]) and not rightAnswer:
			mid = (higherNumber + lowerNumber) // 2
			ans = getAnswer(f"Does your number is {mid}?", mid)
			if ans:
				rightAnswer = True
			else:
				currentNumRange = lowerNumber, higherNumber
				lowerNumber, higherNumber = checkRange(currentNumRange, level)

		if level < 4:
			print("\t\t===========================================")
			print("\t\tOK! Let's make it a little more complicated")
			print("\t\t===========================================")
			level += 1
			gameLogic(level)
		else:
			print("\n\t\t\t***************************************************")
			print("\t\t\tEND OF GAME!")
			print("\t\t\tI hope you made sure that I can guess any number!!")
			print("\t\t\t******************************************************")

	else: #don't ready
		whetherWannaContinue = getAnswer("OK: Do You want to continue this game? Am I waiting for you?")
		if not whetherWannaContinue:
			print("OK! Good bye!")
			return
		else:
			alreadyReady = False
			while not alreadyReady:
				print("If you will be ready please Enter Y[es]")
				alreadyReady = getAnswer("Are you ready?")
			gameLogic(level)






def startGame():
	"""
	Function check whether user want to play this game and if the answer is 'yes',
		then called function 'gameLogic()'
	"""

	print("\nOK! Let's play!")
	print("--------------------------------------------------------------------------------------")
	print("Note:")
	print("\tNow you must be kept in your mind a random integer from specific range and I must be guessing that number!")
	print("\tIf you answer honestly all of my questions I certainly will guess that number!")
	print("--------------------------------------------------------------------------------------\n")
	gameLogic()






def game():
	"""
	Function call 'getAnswer()' function with 'Do you want to play this game?([Y]es or N[o]): ' 
	parameter and check whether user want to play this game.
	If the answer is 'Yes', then called function 'startGame()' thus starting the game, otherwise
	function printed "Thanks anyway. Bye-bye!" and automatically returns 'None'
	"""
	
	if not getAnswer("Do you want to play this game?"): #if user don't want to play
		print("Thanks anyway. Bye-bye!")
	else:
		startGame()
