# Answer = 6857
import math

number = 13195
divisors = []

def find_primes(number):
		for i in range(2, number):
				if number % i == 0:
						find_primes(number / i)
		divisors.append(number)
		return divisors[0]

print(find_primes(number))

