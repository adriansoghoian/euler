# Project Euler problem 12: https://projecteuler.net/problem=12
# Triangle number n == (n - 1) + (n - 2) + ... + 1

import math


def triangle_number(n):
    total = 0

    for i in range(1, n + 1):
        total += i
        yield total


def factor(n):
    factors = []
    factor = 1
    composite = n
    limit = math.sqrt(n)

    while factor <= limit:
        if n % factor == 0:
            factors.append(factor)
            factors.append(composite / factor)
            composite /= factor

        factor += 1

    return factors


def check_num_factors(n):
    number = len(factor(n))
    return number


def run(num_factors):
    gen = triangle_number(1000000)
    while True:
        try:
            next = gen.next()
            if check_num_factors(next) > num_factors:
                return next
        except:
            break


if __name__ == "__main__":
    print run(500)
