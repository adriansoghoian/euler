# 2520 is the smallest number that can be divided 
# by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?

def get_reduced_divisors(lowerbound, upperbound):
	factors = list(range(lowerbound, upperbound + 1))
	output = []
	for i in range(len(factors) - 1):
		for j in range(i, len(factors)):
			if factors[j] % factors[i] == 0:
				output.append(factors[j])
	print set(output)

get_reduced_divisors(2, 20)