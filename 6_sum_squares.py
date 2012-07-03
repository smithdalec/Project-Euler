# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first 
# ten natural numbers and the square of the sum is 3025  385 = 2640.
# Find the difference between the sum of the squares of the first 
# one hundred natural numbers and the square of the sum.
def sum_squares(n):
	squares = []
	for x in xrange(1,n):
		squares.append(pow(x, 2))
	return sum(squares)

def square_sums(n):
	sums = []
	for x in xrange(1,n):
		sums.append(x)
	return pow(sum(sums), 2)

n = 100
print square_sums(n+1) - sum_squares(n+1)

# completes in .0001 second