# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def is_prime(num):
	for x in xrange(2,num):
		if (num % x == 0):
			return False
	return True

i = 2
primes = []
while True:
	if is_prime(i):
		primes.append(i)
	if len(primes) == 10001:
		print i
		break
	i +=1