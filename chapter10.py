# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 23:12:48 2018

@author: Yaya319
"""

txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))

t.sort(reverse=True)

res = list()
for length, word in t:
    res.append(word)

print(res)

# Code: http://www.py4e.com/code3/soft.py


import string
fhand = open('romeo-full.txt')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)

# Code: http://www.py4e.com/code3/count3.py
    
#Ex1*
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

#ex2

fname = input("Enter file name: ")
    
fh = open(fname)
ch = dict()
for line in fh:
     line = line.rstrip()
     if line.startswith('From '): 
         words = line.split()
         hh = words[5][0:2]
         ch[hh] = ch.get(hh, 0) + 1
# Sort the dictionary by value
lst = list()
for key, val in list(ch.items()):
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)