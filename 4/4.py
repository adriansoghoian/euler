# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def check_palindromic(num):
	num = str(num)
	if len(num) %2 != 0:
		num = num[:len(num)/2] + num[len(num) / 2 + 1:]
	i = 0
	while i < len(num) / 2:
		if num[i] != num[i*(-1) - 1]:
			return False
		else:
			i += 1
	return True

num1 = 100
highest = 0
while num1 < 1000:
	num2 = 100
	while num2 < 1000:
		if check_palindromic(num1*num2):
			if num1*num2 > highest:
				highest = num1*num2
		num2 += 1
	num1 += 1

print highest
