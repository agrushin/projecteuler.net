#!/usr/bin/env python
#
# Task: http://projecteuler.net/problem=5
#
# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all 
# of the numbers from 1 to 20?
#
# * Result: 232792560 (took 7m)
#
_devisorMin = 1 
_devisorMax = 20
_maxLimit = 999999999

arr = []
success = False
i = 1

while i <= _maxLimit:
	k = 1
	while k <= _devisorMax:
		if i % k != 0:
			 break
		if k == 20:
			print i
			success = True
			break
		k += 1
	if success == True:
		break
	i += 1
