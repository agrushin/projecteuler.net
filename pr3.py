#!/usr/bin/env python
#
# Task: http://projecteuler.net/problem=3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#
_number = 600851475143

def getPrimeFactors( number ):
	n = 2
	k = 1
	arr = []

	while n <= number:
		if number % n == 0:
			number /= n
			arr.append(n)
		n += 1

	return( arr )

print max(getPrimeFactors( _number ))
