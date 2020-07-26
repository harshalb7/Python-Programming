import sqlite3
import ssl
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from urllib.request import Request
import array

try:
    import dateutil.paeser as parser
except:
    pass
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('CoronCases.sqlite')
cur = conn.cursor()

baseurl = 'https://www.worldometers.info/coronavirus/'

cur.execute('''CREATE TABLE IF NOT EXISTS COVID_19
    (id INTEGER UNIQUE, Country TEXT, Total_Cases INTEGER, New_Cases INTEGER, Total_Deaths INTEGER, New_Deaths INTEGER,Total_Recover INTEGER, New_Recovered INTEGER, 
    Active_Cases INTEGER, Serious_Cases INTEGER, Case_PerM INTEGER, Death_PerM INTEGER, 
    Total_Tests INTEGER,  Test_PerM INTEGER, Population INTEGER, Continent TEXT )''')

html = urlopen(Request('https://www.worldometers.info/coronavirus/', headers={'User-Agent': 'Mozilla/5.0'})).read().decode()
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table')
th = table.find_all('th')
tbody = table.find('tbody')
rows = tbody.find_all('tr')

print(th)
for row1 in rows[8:]:
    cols = row1.find_all('td')

    t = []
    count = 0
    for col in cols:
        t1=col.text.strip()
        if len(t1) < 1 or t1 == 'N/A':
            t1 = 0
        t.append(t1)
        count = count + 1

    cur.execute('SELECT id FROM COVID_19 WHERE id=?',(t[0],))
    cur.execute('SELECT Country FROM COVID_19 WHERE Country=?',(t[1],))
    cur.execute('SELECT Total_Cases FROM COVID_19 WHERE Total_Cases=?',(t[2],))
    cur.execute('SELECT New_Cases FROM COVID_19 WHERE New_Cases=?',(t[3],))
    cur.execute('SELECT Total_Deaths FROM COVID_19 WHERE Total_Deaths=?',(t[4],))
    cur.execute('SELECT New_Deaths FROM COVID_19 WHERE New_Deaths=?',(t[5],))
    cur.execute('SELECT Total_Recover FROM COVID_19 WHERE Total_Recover=?',(t[6],))
    cur.execute('SELECT New_Recovered FROM COVID_19 WHERE New_Recovered=?',(t[7],))
    cur.execute('SELECT Active_Cases FROM COVID_19 WHERE Active_Cases=?',(t[8],))
    cur.execute('SELECT Serious_Cases FROM COVID_19 WHERE Serious_Cases=?',(t[9],))
    cur.execute('SELECT Case_PerM FROM COVID_19 WHERE Case_PerM=?',(t[10],))
    cur.execute('SELECT Death_PerM FROM COVID_19 WHERE Death_PerM=?',(t[11],))
    cur.execute('SELECT Total_Tests FROM COVID_19 WHERE Total_Tests=?',(t[12],))
    cur.execute('SELECT Test_PerM FROM COVID_19 WHERE Test_PerM=?',(t[13],))
    cur.execute('SELECT Population FROM COVID_19 WHERE Population=?',(t[14],))
    cur.execute('SELECT Continent FROM COVID_19 WHERE Continent=?',(t[15],))

    cur.execute('''INSERT OR IGNORE INTO COVID_19 (id , Country, Total_Cases , New_Cases , Total_Deaths , New_Deaths ,Total_Recover ,New_Recovered, Active_Cases , Serious_Cases, Case_PerM , Death_PerM, Total_Tests,  
        Test_PerM, Population, Continent ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(t[0],t[1],t[2],t[3],t[4],t[5],t[6],t[7],t[8],t[9],t[10],t[11],t[12],t[13],t[14],t[15]))

conn.commit()    
cur.close()