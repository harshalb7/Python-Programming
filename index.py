import sqlite3
import re
import zlib

try:
    import dateutil.parser as parser
except:
    pass

conn1 = sqlite3.connect('CoronCases.sqlite')
cur1 = conn1.cursor()


cur1.execute('SELECT id FROM COVID_19') 
id_res = cur1.fetchall() 
cur1.execute('SELECT Country FROM COVID_19') 
country_res = cur1.fetchall() 
cur1.execute('SELECT Total_Cases FROM COVID_19')
TotalCases_res = cur1.fetchall() 
cur1.execute('SELECT New_Cases FROM COVID_19')
NewCases_res = cur1.fetchall() 
cur1.execute('SELECT Total_Deaths FROM COVID_19')
totalDeath_res = cur1.fetchall() 
cur1.execute('SELECT New_Deaths FROM COVID_19')
NewDeath_res = cur1.fetchall() 
cur1.execute('SELECT Total_Recover FROM COVID_19 ')
TotalRecover_res = cur1.fetchall() 
cur1.execute('SELECT New_Recovered FROM COVID_19 ')
NewRecover_res = cur1.fetchall() 
cur1.execute('SELECT Active_Cases FROM COVID_19')
ActiveCases_res = cur1.fetchall() 
cur1.execute('SELECT Serious_Cases FROM COVID_19')
SeriousCases_res = cur1.fetchall() 
cur1.execute('SELECT Case_PerM FROM COVID_19 ')
CasePerM_res = cur1.fetchall() 
cur1.execute('SELECT Death_PerM FROM COVID_19')
DeathPerM_res = cur1.fetchall() 
cur1.execute('SELECT Total_Tests FROM COVID_19')
Totaltest_res = cur1.fetchall() 
cur1.execute('SELECT Test_PerM FROM COVID_19')
TestPerM_res = cur1.fetchall() 
cur1.execute('SELECT Population FROM COVID_19')
Population_res = cur1.fetchall() 
cur1.execute('SELECT Continent FROM COVID_19')
Continent_res = cur1.fetchall() 
max1 = 0
for Continent_res1 in id_res:
	Continent_res1 = (int) (Continent_res1[0])
	if max1 < Continent_res1: max1 = Continent_res1
#print(max1)

conn1.commit()    
cur1.close()


conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

cur.executescript('''
	DROP TABLE IF EXISTS COVID_19;
	DROP TABLE IF EXISTS Country;
	DROP TABLE IF EXISTS Continent;

	CREATE TABLE COVID_19 (
		id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		Country_id INTEGER,
		Total_Cases INTEGER,
		New_Cases INTEGER,
		Total_Deaths INTEGER,
		New_Deaths INTEGER,
		Total_Recover INTEGER,
		New_Recovered INTEGER, 
    	Active_Cases INTEGER,
    	Serious_Cases INTEGER,
    	Case_PerM INTEGER,
    	Death_PerM INTEGER, 
    	Total_Tests INTEGER,  
    	Test_PerM INTEGER, 
    	Population INTEGER, 
    	Continent_id TEXT );

	CREATE TABLE Country (
		id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		country TEXT UNIQUE );

	CREATE TABLE Continent (
		id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		continent TEXT UNIQUE );''')


for i in range(max1):
	cur.execute('''INSERT OR IGNORE INTO Country (country) VALUES (?)''',(country_res[i][0],))
	cur.execute('SELECT id FROM Country WHERE Country=?',(country_res[i][0],))
	Country_id = cur.fetchone()[0]

	cur.execute('''INSERT OR IGNORE INTO Continent (continent) VALUES (?)''',(Continent_res[i][0],))
	cur.execute('SELECT id FROM Continent WHERE Continent=?',(Continent_res[i][0],))
	Continent_id = cur.fetchone()[0]

	cur.execute('''INSERT OR IGNORE INTO COVID_19 (id , Country_id, Total_Cases , New_Cases , Total_Deaths , New_Deaths ,Total_Recover ,New_Recovered, Active_Cases , Serious_Cases, Case_PerM , Death_PerM, Total_Tests,  
        Test_PerM, Population, Continent_id ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(id_res[i][0], Country_id,TotalCases_res[i][0], NewCases_res[i][0], totalDeath_res[i][0],
        	NewDeath_res[i][0], TotalRecover_res[i][0], NewRecover_res[i][0], ActiveCases_res[i][0], SeriousCases_res[i][0], CasePerM_res[i][0], DeathPerM_res[i][0], Totaltest_res[i][0],
        	TestPerM_res[i][0], Population_res[i][0], Continent_id))

conn.commit()
cur.close()