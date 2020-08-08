
class studentInfo:

	def __init__(self,rollNo,name,gender,std,PRN,phoneNo,homeTown):
		self.rollNo  = rollNo
		self.name    = name
		self.gender  = gender
		self.std     = std
		self.PRN     = PRN
		self.phoneNo = phoneNo
		self.homeTown= homeTown

	def getinfo(self,rollNo,name,gender,std,PRN,phoneNo,homeTown ):
		ob = studentInfo(rollNo,name,gender,std,PRN,phoneNo,homeTown)
		data.append(ob)

	def displayDate(self,ob):
		print(' ',ob.rollNo,'\t',ob.name,'\t',ob.gender,'\t',ob.std,'\t',ob.PRN,'\t',ob.phoneNo,'\t',ob.homeTown)


no = input('\nEnter Number of Data: ')
data = []
x = studentInfo('','','','','','','')
for obj in range(int(no)):
	rollNo   = input('Enter Roll No  : ')
	name     = input('Enter Name     : ')
	gender   = input('Enter Gender   : ')
	std      = input('Enter Standard : ')
	PRN      = input('Enter PRN No   : ')
	phoneNo  = input('Enter Phone No : ')
	homeTown = input('Enter Home Town: ')
	x.getinfo(rollNo,name,gender,std,PRN,phoneNo,homeTown)

print('rollNo\tname\tgender\tstd\tPRN\tphoneNo\thomeTown')
for i in range( data.__len__()):
	x.displayDate(data[i])		