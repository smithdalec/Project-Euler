# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the 
# numbers from 1 to 20?
all_divisible = False
top_num = 20
i = top_num

while (all_divisible == False):
	nums = []
	for x in xrange(1,(top_num)):
		if i % x == 0:
			nums.append(True)
		else:
			nums.append(False)
	if (all(nums)):
		print i
		break
	i += top_num
	if i % 100000 == 0: print i

# Time: 154.753 seconds :(