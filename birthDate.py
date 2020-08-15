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
		if int(dd) < =0 or int(dd) > 29: # if in leap year feb has days greater than 29 and less than or equal 0
			return False             #return false
		else:
			return True             #else return true
	else:
		if int(dd) < =0 or int(dd) > 28:  # if in leap year feb has days greater than 29 and less than or equal 0
			return False            #return false
		else:
			return True             #else return true

def leapYear(yy, mm):
	if int(yy) % 4 == 0 and int(mm) == 2:      #on dividing year by 4 if remainder is zero then its leap year
		return True
	else:
		return False                  #else ordinary year

def getYear(): #defination of getYear function
	try:
		yy = input('Enter Year : ')    #enter value of year
		if not yy:
			raise Exception()      # enter value is empty then raise exception
	except:
		yy = '0'                       #set to invalid value 0

	return yy                              # return value of year

def getMonth(): #defination of getMonth function
	try:
		mm = input('Enter Month : ')   #enter value of Month
		if not mm:
			raise Exception()        # enter value is empty then raise exception
	except:
		mm = '0'                        #set to invalid value 0

	mm = str(int(mm))
	return mm                             #return value of month

def getDate(): #defination of getDate function
	try:
		dd = input('Enter Date : ')    #enter value of date
		if not dd:
			raise Exception()        # enter value is empty then raise exception
	except:
		dd = '0'                     #set to invalid value 0

	dd = str(int(dd))
	return dd                           #return value of date

def checkYear(yy):   #defination of CheckYear function 
	while ( int(yy) <= 999 or int(yy) >2999):             #run loop till enter year is not in between 1000 to 2999
		try:
			if int(yy) <= 999 or int(yy) >2999:
				print('Enter Year is Invalid..Re-Enter Year.')
				raise Exception()            #raise exception if year is not in between 1000 to 2999

		except:
			print('Year should be in between 1000 to 2999')
			yy = getYear()                      #re-enter correct year

	return yy                                           #return correct year
def checkMonth(yy, mm):    #defination of checkMonth function
	while ( int(mm) <=0 or int(mm) > 12 ):                #run loop till enter month is not in between 1 to 12
		print('')
		try:
			if int(mm) <=0 or int(mm) > 12:
				print('Enter Month is Invalid..Re-Enter Month.')
				raise Exception()           #raise exception if month is not in between 1 to 12
		except:
			print('Month should be in between 1 to 12')
			mm = getMonth()  #re-enter correct month
	return mm  #return correct month
def checkD(yy, mm, dd):    #defination of Checkdate function
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
