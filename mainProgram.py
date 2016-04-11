import powerFunction


base = powerFunction.float_input("Type a base number. ")
exponent = powerFunction.int_input("Type an exponent. ")

answer = powerFunction.power(base, exponent)
print("The answer is {}.".format(answer))