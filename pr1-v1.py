#!/usr/bin/python
#
# Task: http://projecteuler.net/problem=1
#
number = 1000

def getMultiples( number, devisors ):
	i = 1
	multiplesList = []

	while i < number:
		if i % devisors == 0:
			multiplesList += [i]
		i += 1

	return set( multiplesList )

def getSum( array ):
	total = 0

	for i in array:
		total += i

	return total

totalList = set()
totalSum = 0

for devisor in [ 3, 5 ]:
	totalList = totalList | getMultiples( number, devisor )

print "Sum of multiples == " + str( getSum(totalList) )

