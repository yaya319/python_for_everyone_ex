# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 13:14:46 2018

@author: Yapei
"""
#  exemple of chapter 5
count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
print('Count: ', count)

total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
print('Total: ', total)



largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)


#Exercise 1: Write a program which repeatedly reads numbers until the user enters "done".
# Once "done" is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
num=0
total=0.0

while True:
    sval = input('Enter numbers: ')
    if sval=='done':
        break
    try:
        fval=float(sval)
    except: 
        print("bad data")
        continue
    num=num+1
    total=total+fval
print(total,num, total/num)

#Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        n = int(num)
        xn = n
        mn = n
        if largest is None:
            largest = xn
        elif n > largest:
            largest = xn
            
        if smallest is None:
            smallest = mn
        elif n < smallest:
            smallest = mn
    except:
        print("Invalid input")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)