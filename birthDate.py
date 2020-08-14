def birthDate():

	yy = getYear() #call for function to get year
	yy = checkYear(yy) #check given enter year correct or not 

	mm = getMonth() #call for function to get Month
	mm = checkMonth(yy,mm) #check given enter Month correct or not
	
	dd = getDate() #call for function to get Date
	dd = checkD(yy, mm, dd) #check given enter Date correct or not
	
	if int (mm) < 10:
		mm = '0'+ mm
	if int (dd) < 10:
		dd = '0'+ dd
	date = dd+'-'+mm+'-'+yy #to print in correct format
	print('Date: ',date)

def checkDate(dd, mm, yy):
	if int(mm) % 2 == 1:
		if int(dd) < =0 or int (dd) >31:  # if date is greater than 31 or less than 0 or 0 return false
			return False              
		else:				 #else return true
			return True
	else:
		if int(dd) < =0 or int (dd) >30: # if date is greater than 30 or less than 0 or 0 return false
			return False
		else:
			return True            #else return true

def checkLeap(yy, mm, dd):
	if leapYear(yy, mm) is True:
		if int(dd) < =0 or int(dd) > 29:
			return False
		else:
			return True
	else:
		if int(dd) < =0 or int(dd) > 28:
			return False
		else:
			return True

def leapYear(yy, mm):
	if int(yy) % 4 == 0 and int(mm) == 2:
		return True
	else:
		return False

def getYear():
	try:
		yy = input('Enter Year : ')
		if not yy:
			raise Exception()
	except:
		yy = '0'

	return yy

def getMonth():
	try:
		mm = input('Enter Month : ')
		if not mm:
			raise Exception()
	except:
		mm = '0'

	mm = str(int(mm))
	return mm

def getDate():
	try:
		dd = input('Enter Date : ')
		if not dd:
			raise Exception()
	except:
		dd = '0'

	dd = str(int(dd))
	return dd

def checkYear(yy):
	while ( int(yy) <= 999 or int(yy) >2999):
		try:
			if int(yy) <= 999 or int(yy) >2999:
				print('Enter Year is Invalid..Re-Enter Year.')
				raise Exception() 

		except:
			print('Year should be in between 1000 to 2999')
			yy = getYear()

	return yy
def checkMonth(yy, mm):
	while ( int(mm) <=0 or int(mm) > 12 ):
		print('')
		try:
			if int(mm) <=0 or int(mm) > 12:
				print('Enter Month is Invalid..Re-Enter Month.')
				raise Exception() 
		except:
			print('Month should be in between 1 to 12')
			mm = getMonth()
	return mm
def checkD(yy, mm, dd):
	while ( checkLeap(yy, mm, dd) is False or checkDate(dd, mm, yy) is False ):
		print('')
		try:
			if int(mm) != 2:
				if checkDate(dd, mm, yy) is False:
					print('Enter Date is Invalid..Re-Enter Date.')
					raise Exception()
				else:
					break
			else:
				if checkLeap(yy, mm, dd) is False:
					print('Enter Date is Invalid..Re-Enter Date.')
					raise Exception()
				else:
					if checkLeap(yy, mm, dd) is False:
						print('Invalid Date ..Leap Year...Re-Enter Date.') 
						raise Exception()
					else:
						break
		except:
			print('Enter Correct Date')
			dd = getDate()
	return dd

birthDate() #call for function
