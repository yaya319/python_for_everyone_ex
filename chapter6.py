# -*- coding: utf-8 -*-

#chapter 6
#Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.
fruit = 'banana'
for char in fruit:
    print(char)
    
#Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.
    
word = 'banana'

def count(word,l):
    count = 0
    for letter in word:
        if letter == l:
            count = count + 1
    return(count)

#dir
stuff = 'Hello world'
type(stuff)
dir(stuff)
#strip
line = '  Here we go  '
line.strip()
line.startswith('Have')

#printf-style String Formatting
print('%(language)s has %(number)03d quote types.' %
{'language': "Python", "number": 2})

#Exercise 5: Take the following Python code that stores a string:

str = 'X-DSPAM-Confidence:0.8475'

num=float(str[str.find(':')+1:])

text = "X-DSPAM-Confidence:    0.8475";
print(float(text[text.find('0'):]))
