#!/usr/bin/env python
#
# Task: http://projecteuler.net/problem=2
# Fibonacci sequence
#
_upperLimit = 4000000

def getFibonacciSeq( _upperLimit ):
	a = 0
	i = 0
	array = [ 1, 2 ]

	while array[i]+array[i+1] < _upperLimit:
		array.append( array[i]+array[i+1] )
		i += 1

	return(array)

total = 0
for n in getFibonacciSeq( _upperLimit ):
	if n % 2 == 0:
		total += n

print total
