# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 21:38:04 2018

@author: yaya319
"""

import os
os.chdir("D:/learn/Python script/python for everyone/python_for_everyone_ex/")

#exemple
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)

# Code: http://www.py4e.com/code3/count1.py

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])
    
# example  
import string
string.punctuation

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)

# Code: http://www.py4e.com/code3/count2.py

# ex2

fname = input("Enter file name: ")

fh = open(fname)
ad = dict()
for line in fh:
     line = line.rstrip()
     if line.startswith('From '): 
         words = line.split()
         ma = words[2]
         ad[ma] = ad.get(ma, 0) + 1
print(ad)
       
#ex3       
       
fname = input("Enter file name: ")

fh = open(fname)
ad = dict()
for line in fh:
     line = line.rstrip()
     if line.startswith('From '): 
         words = line.split()
         ma = words[1]
         ad[ma] = ad.get(ma, 0) + 1
print(max([(value,key) for (key,value) in ad.items()]))

# ex4
fname = input("Enter file name: ")

fh = open(fname)
ad = dict()
for line in fh:
     line = line.rstrip()
     if line.startswith('From '): 
         words = line.split()
         ma = words[1]
         ad[ma] = ad.get(ma, 0) + 1
         mma=max([(value,key) for (key,value) in ad.items()])
print(mma[1],mma[0])


