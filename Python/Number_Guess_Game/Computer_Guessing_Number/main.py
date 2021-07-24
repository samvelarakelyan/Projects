"""
***************************
*This program has been run*
***************************

	Processor -> 'AMD A6'

	Platform  -> 'LINUX, Kernel verssion 5.11.0-16-generic'

	OS        -> 'Unbuntu 21.04'


This program is written only in python.
Don't use non-standard libraries.
"""


from computer_guess import game



if __name__ == "__main__":
	
	GREETING = """
	**************************************************
	*HI! THIS IS THE GAME 'Computer Guessing Number!'*
	**************************************************
	"""
	print(GREETING.center(50)) #transfer the string into the center with a specific size
	print()
	game()
