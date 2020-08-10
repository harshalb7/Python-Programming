from datetime import datetime
import urllib.request, urllib.parse, urllib.error
import http
import requests
import string
import json

address = input('Enter Your City: ')

today = datetime.today()

#print Today's date
#print('Today date is: ', today)

timeNow = datetime.now()

#print Date and current time 
print('\nCurrent Time & Date is : ', timeNow)

api_key = 42
serviceurl = "http://py4e-data.dr-chuck.net/json?"

#address = 'nashik'
address = address.strip()

parms = dict()
parms["address"] = address
parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)

data = urllib.request.urlopen(url).read().decode()
js = json.loads(str(data))
lat = js["results"][0]["geometry"]["location"]["lat"]
lng = js["results"][0]["geometry"]["location"]["lng"]
where = js['results'][0]['formatted_address']
where = where.replace("'", "")

res = [i for i in range(len(where)) if where.startswith(',', i)]

City = where[:res[0]]
if len(res) > 1:
	State = where[res[0]+1:res[1]]
	Country = where[res[1]+1:]
else:
	Country = where[res[0]+1:]
print('\nlocation: ')
print('  City     : ', City.strip())
if len(res) > 1:
	print('  State    : ', State.strip())
print('  Country  : ', Country.strip())
print('  Latitude : ', lat)
print('  Longitude: ', lat,'\n')