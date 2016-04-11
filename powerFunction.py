#Author: Jared Lefkort
#Date: 3/9/2016

def power(base, exponent):

	zero = "1"
	
	if exponent < 1:
		return zero
	
	if exponent == 1:
		return base
	
	
	result = (base) * power(base, exponent - 1)

	return result


#-----------------------------------------------------------------------------------------
	
def int_input(question):
	
	"""Asks the user for an int, and let them try again."""
	
	answer = input(question)
	
	try:
		#terminating case
		answer = int(answer)
		return answer
	
	except ValueError:
		return int_input("That was not an integer; try again. ")

def float_input(question):

	answer = input(question)
	
	try:
		answer = float(answer)
		return answer
	
	except ValueError:
		return float_input("That was not a float, try again. ")
#-----------------------------Main Program---------------------------


base = float_input("Type a base number. ")
exponent = int_input("Type an exponent. ")

if exponent == 0:
	answer = 1
	print("The answer is {}.".format(answer))

else:
	answer = power(base, exponent)
	print("The answer is {}.".format(answer))
	
