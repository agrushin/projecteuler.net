#!/usr/bin/env python
#
# Task: http://projecteuler.net/problem=4
#
# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
_minLimit = 100
_maxLimit = 999

def isPalindromic( number ):
	a = number
	b = 0

	while a:
		b = b * 10 + a % 10
		if number == b:
			return( True )
		a /= 10

	return( False )

i = _minLimit
k = _minLimit
arr = []

while i <= _maxLimit:
	k = _minLimit

	while k <= _maxLimit:
		if isPalindromic(i*k):
			arr.append(i*k)
		k += 1
	i += 1

print "Largest palindrome made from the product of two 3-digit numbers == %d" % max( arr )
