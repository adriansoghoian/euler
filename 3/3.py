# Answer = 6857
import math

number = 13195
divisors = [1]

def find_primes(number):
		for i in range(2, number):
				if number % i == 0:
						divisors.append(i)
		return divisors

print(find_primes(number))
