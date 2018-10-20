# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 21:16:08 2018

@author: yaya319
"""
# example
numlist = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)

# Code: http://www.py4e.com/code3/avelist.py

#ex4
import os
os.chdir("D:/learn/Python script/python for everyone/python_for_everyone_ex/")

fname = input("Enter file name: ")
fh = open(fname)
fread =fh.read()
lst = list()
words=fread.split()
for word in words:
    if word in lst:
        continue
    else:
        lst.append(word)
        lst.sort()
        lst
fh.close()
print(lst)

    
#ex5
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
     line = line.rstrip()
     if not line.startswith('From ') : continue
     words = line.split()
     count=count+1
     print(words[1])


print("There were", count, "lines in the file with From as the first word")
 


