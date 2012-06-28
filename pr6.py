#!/usr/bin/env python
#
# Task: http://projecteuler.net/problem=6
#
# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the 
# square of the sum is 3025  385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and 
# the square of the sum.
#
# * Result = 25164150

def sqrt( n ):
	return n*n

def getSumOfSquares( x, y ):
	result = 0

	for n in range( x, y ):
		result += sqrt( n )

	return( result )

squareOfSum = sqrt( sum( range( 1, 101 ) ) )
sumOfSquares = getSumOfSquares( 1, 101 )

print "(squareOfSum=%d) - (sumOfSquares=%d) == %d" % ( squareOfSum, sumOfSquares, ( squareOfSum - sumOfSquares ) )

