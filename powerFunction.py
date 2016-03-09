#Author: Jared Lefkort
#Date: 3/9/2016

def power(base, exponent):

	answer = base
	counter = 1
	while exponent > counter:
		counter += 1
		answer = answer * base

	return answer
	
base = int(input("Type a base number. "))
exponent = int(input("Type an exponent. "))

answer = power(base, exponent)

print("The answer is {}.".format(answer))