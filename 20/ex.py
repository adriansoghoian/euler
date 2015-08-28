from numba import jit


def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

@jit
def sum_digits(n):
    string = str(n)
    total = 0
    for char in string:
        total += int(char)

    return total

print sum_digits(factorial(100))