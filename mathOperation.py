def addtion(num1, num2):
	return num1 + num2

def subtraction(num1, num2):
	return num1 - num2

def multiplication(num1, num2):
	return num1 * num2

def division(num1, num2):
	if num2 != 0:
		return num1/num2
	else:
		print("Divide by Zero Error")

#print("Enter Numbers: ")
num1 = float(input(" Number 1: "))

num2 = float(input(" Number 2: "))

print(" Addition is      : ",addtion(num1, num2))
print(" Subtraction is   : ",subtraction(num1, num2))
print(" Multiplication is: ",multiplication(num1, num2))
print(" Division is      : ",division(num1, num2))