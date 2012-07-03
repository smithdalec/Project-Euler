# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

def is_prime(num):
	for x in xrange(2,num):
		if (num % x == 0):
			return False
	return True

bignum = 600851475143
start = int(math.floor(math.sqrt(bignum)))
for x in xrange(start,1,-1):
	if (bignum % x == 0) and is_prime(x):
		print x
		break

# Executes in 0.152 seconds