#!/usr/bin/python
#
# Task: http://projecteuler.net/problem=1
#
_number = 1000
_devisors = [ 3, 5 ]

def getMultiples( number, devisors ):
	i = 1
	multiplesList = []

	while i < number:
		for n in devisors:
			if i % n == 0:
				multiplesList += [i]
		i += 1

	return set( multiplesList )

print "Sum of multiples == " + str( sum( getMultiples( _number, _devisors ) ) )

