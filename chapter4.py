# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 21:52:07 2018


#Exercise 1: Run the program on your system and see what numbers you get. Run the program more than once and see what numbers you get.
import random
for i in range(10):
    x = random.random()
    print(x)
    
random.randint(5, 10)

#Exercise 2: Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get.
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

repeat_lyrics()

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

#Exercise 3: Move the function call back to the bottom and move the definition of print_lyrics after the definition of repeat_lyrics. What happens when you run this program?
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')



def repeat_lyrics():
    print_lyrics()
    repeat_lyrics()
    print_lyrics()
#Exercise 5: What will the following Python program print out?
def fred():
   print("Zap")

def jane():
   print("ABC")

jane()
fred()
jane()

#Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate)

def computepay(h, r):
   
    fhrs = float(h)
    frate = float(r)
    if fhrs> 40: 
        Pay = (fhrs-40)*frate*1.5 + 40*frate
        return Pay
    else :
        Pay =  fhrs*frate
        return Pay

hrs = input("Enter Hours:")
r=input('Enter rate: ')

p = computepay(hrs,r)

print("Pay",p)

#Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.
    
def computegrade(score):
    score=float(score)
    try: 
        if score >= 0.9 and score < 1:
            return print('A')
        elif score>= 0.8 and score < 0.9:
            return print('B')
        elif score>= 0.7 and score < 0.8:
            return print('C')
        elif score>= 0.6 and score < 0.7:
            return print('D')
        elif score < 0.6:
            return print('F')
    except: 
            return print('Bad score')
    
