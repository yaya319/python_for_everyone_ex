# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 18:02:27 2018

@author:yaya319
"""

import os
os.chdir("D:/learn/Python script/python for everyone/python_for_everyone_ex/")

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
        # Search for lines that start with From and a character
# followed by a two digit number between 00 and 99 followed by ':'
# Then print the number if it is greater than zero
    x = re.findall('^From .* ([0-9][0-9]):', line)
    if len(x) > 0: print(x)
# Search for lines that start with 'Details: rev='
# followed by numbers and '.'
# Then print the number if it is greater than zero

    y = re.findall('^Details:.*rev=([0-9.]+)', line)
    if len(y) > 0: print(y)
    # Search for lines that start with 'X' followed by any
# non whitespace characters and ':' followed by a space
# and any number. The number can include a decimal.
# Then print the number if it is greater than zero.
    z = re.findall('^X\S*: ([0-9.]+)', line)
    if len(z) > 0: print(z)
     
     # Search for lines that have an at sign between characters
# The characters must be a letter or number
    b = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
    if len(b) > 0: print(b)

#ex1
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    t=re.findall('^Author',line)
    print(len(t))


# assignement

text=open('regex_sum_147043.txt')
tot=[]
for line in text:
    line = line.rstrip()
    t=re.findall('[0-9]+',line)
    
    if len(t)>0: print(t)
    tot=t+tot
    tot = [int(i) for i in tot]
print(sum(tot))

