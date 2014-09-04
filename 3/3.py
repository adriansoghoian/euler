# Answer = 6857

number = 600851475143

def find_primes(number):
		i = 2
		while i * i < number:
				while number % i == 0:
						number = number / i
				i += 1
		return number


print find_primes(number)

