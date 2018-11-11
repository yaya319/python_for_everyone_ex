# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 20:29:52 2018

@author: yaya319
"""


import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))

# Code: http://www.py4e.com/code3/xml2.py
# example
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_147077.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
print(len(counts))

lst = list()
total = 0

for i in counts:
    lst.append(i.text)

for it in lst:
    fit = float(it)
    total = total + fit
print('Total', total)



import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
    
import json
url='http://py4e-data.dr-chuck.net/comments_147078.json'
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()

info=json.loads(data)
comment=info['comments']
print('count:', len(comment))

tot=0

for i in range(0,50):
    te=int(comment[i]['count'])
    tot=tot+te
print('sum', tot)


#autograder 3

http://py4e-data.dr-chuck.net/json?


import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = 'Tarrant County College'
    #if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    #if not js or 'status' not in js or js['status'] != 'OK':
    #    print('==== Failure To Retrieve ====')
    #    print(data)
     #   continue

   # print(json.dumps(js, indent=4))

    print(js['results'][0]['place_id'] )
    
    
    
    # To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Raegan.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags

tags = soup('a')
tags=tags[0:18]
for tag in tags:
    print(tag.get('href', None))
    