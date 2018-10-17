# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 20:25:56 2018

@author: Yapei
"""

import os
os.chdir("D:/learn/Python script/python for everyone/python_for_everyone_ex/")
#chapiter 7
# ex1
fhand = open('D:/learn/Python script/python for everyone/python_for_everyone_ex/mbox-short.txt')

for line in fhand:
    line = line.upper()
    print(line)
    
# ex2
fname = input("Enter file name: ")
fh = open(fname)
tot=0
count=0
for line in fh:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
        
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        sline=float(line[line.find('0'):])
        tot=tot+sline
        
print("Average spam confidence:", tot/count)