#!/usr/bin/python

'''
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''

s1 = raw_input("Input a word: ")

s2 = s1[::-1] # reverse a string

if s1 == s2:
	print "{0} is a palindrome".format(s1)
else:
	print "{0} is a NOT a palindrome".format(s1)

