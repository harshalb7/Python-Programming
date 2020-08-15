import xlrd
fhand = xlrd.open_workbook('Practicl-2.xlsx')
sheet = fhand.sheet_by_index(0)
#print(sheet.nrows)
#print(sheet.ncols)

#no = input("1.Account\n2.borrower\n3.branch\n4.customer\n5.depositer\n6.loan")
fhand = open('account.txt','w')
for i in range (sheet.nrows):
	
	#print(sheet.cell_value(i,0))
	branch  = sheet.cell_value(i,2)
	acc_no  = sheet.cell_value(i,3)
	balance = (sheet.cell_value(i,4))
	write = "insert into Account VALUES ("+"'"+str(branch)+"'"+","+"'"+str(acc_no)+"'"+","+str(balance)+");"
	fhand.write(write)
	fhand.write("\n")
fhand.close()

fhand = open('borrower.txt','w')
for i in range (sheet.nrows):
	
	cust_name = sheet.cell_value(i,0)
	loan_no   = sheet.cell_value(i,5)
	if loan_no != 0.0:
		write = "insert into Borrower VALUES ("+"'"+str(loan_no)+"'"+","+"'"+str(cust_name)+");"
		fhand.write(write)
		fhand.write("\n")
fhand.close()

fhand = open('loan.txt','w')
for i in range (sheet.nrows):
	
	loan_no   = sheet.cell_value(i,5)
	branch  = sheet.cell_value(i,2)
	loan_amount = sheet.cell_value(i,6)
	if loan_no != 0.0:
		write =  "insert into Loan VALUES (" + "'"+str(loan_no)+"'" +","+ "'"+str(branch)+"'" +","+ str(loan_amount) +");"
		fhand.write(write)
		fhand.write("\n")

fhand.close()

fhand = open('branch.txt','w')
for i in range (sheet.nrows):
	
	branch  = sheet.cell_value(i,2)
	branch_city = 'Nashik'
	assets = sheet.cell_value(i,7)
	bval = sheet.cell_value(i,9)
	if bval != 0.0:
		write = "insert into branch VALUES (" + "'"+str(branch)+"'" +","+ "'"+branch_city+"'"+"," + str(assets) +");"
		fhand.write(write)
		fhand.write("\n")
fhand.close()

fhand = open('customer.txt','w')
for i in range (sheet.nrows):
	
	cust_name = sheet.cell_value(i,0)
	address= sheet.cell_value(i,1)
	cust_city = 'Nashik'
	write =  "insert into customer VALUES (" + "'"+str(cust_name)+"'" +","+ "'"+str(address)+"'" +","+ "'"+cust_city+"'"+");"
	fhand.write(write)
	fhand.write('\n')
fhand.close()

fhand = open('depositor.txt','w')
for i in range(sheet.nrows):
	
	cust_name = sheet.cell_value(i,0)
	acc_no  = sheet.cell_value(i,3)
	depositor = sheet.cell_value(i,8)
	if depositor != 0.0:
		write = "insert into depositor VALUES (" + "'"+str(cust_name)+"'" +","+ "'"+str(acc_no)+"'"+");"
		fhand.write(write)
		fhand.write('\n')
fhand.close()