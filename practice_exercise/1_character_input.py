#!/usr/bin/python

'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''

import datetime

name = raw_input("Enter your name: ")
age = int(input("Enter age: "))

year = datetime.datetime.today().year + (100 - age)
msg = "\nHello %s, in %d you will become 100 years" % (name, year)

print msg

cnt = int(input("\nHow many times you want to repeat this message: "))

print msg * cnt
print "\n"

