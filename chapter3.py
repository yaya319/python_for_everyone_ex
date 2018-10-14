# -*- coding: utf-8 -*-

#chapter 3
# ex1: ewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
hrs=input('Enter hours: ')
rate=input('Enter rate: ')
Pay=float(hrs)*float(rate)
print(Pay) 
# ex2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:
hrs=input('Enter hours: ')
rate=input('Enter rate: ')
try:
    fhrs = float(hrs)
    frate = float(rate)
    Pay = fhrs*frate
    print(Pay)
except:
    print('Please enter a number')

#Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. 
# If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
score=input('Enter score: ')
score=float(score)
try: 
    if score >= 0.9 and score < 1:
        print('A')
    elif score>= 0.8 and score < 0.9:
        print('B')
    elif score>= 0.7 and score < 0.8:
        print('C')
    elif score>= 0.6 and score < 0.7:
        print('D')
    elif score < 0.6:
        print('F')
except: 
    print('Bad score')