def concatination(string1, string2):
	print ("Concatination        : ", string1+string2)

def capitalizeStr(string1):
	print ("Capitalize           : ", string1.capitalize())

def lowerCase(string1):
	print ("Lower String         : ",string1.lower())

def upperCase(string1):
	print ("Upper String         : ",string1.upper())

def lenof(string1, string2):
	print("Length of 1st String : ", len(string1))
	print("Length of 2nd String : ", len(string2))

def indexod(string1, string2):
	print("Found String",string2,"at position:", string1.index(string2, 0, len(string1)))

def findstr(string1, string2):
	print("Found String",string2,"at position:",string1.find(string2, 0, len(string1)))



string1 = input('Enter 1st String: ')
string2 = input('Enter 2nd String: ')

concatination(string1, string2)
capitalizeStr(string1)
lowerCase(string1)
upperCase(string1)
lenof(string1, string2)
indexod(string1, string2)
findstr(string1, string2)
