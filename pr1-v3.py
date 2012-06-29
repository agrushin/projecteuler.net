#!/usr/bin/python
#
# Task: http://projecteuler.net/problem=1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
# 
# Result - 233168
#
_number = 1000
_devisors = [ 3, 5 ]

def getSumOfMultiples( number, devisors ):
	multiplesSum = 0

	for i in range( 1, number ):
		for n in devisors:
			if i % n == 0:
				multiplesSum += i
				break

	return multiplesSum

print "Sum of multiples == %d " % getSumOfMultiples( _number, _devisors )
