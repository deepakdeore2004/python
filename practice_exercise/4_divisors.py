#!/usr/bin/python

num = int(input("Please enter a number: "))

x = range(2,num)

for element in x:
	if num % element == 0:
		print "{0} is divisor of {1}".format(element, num)


