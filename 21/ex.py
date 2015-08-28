from datetime import datetime
import math


def proper_divisors(n):
    divisors = {1: True}
    upper_bound = int(math.sqrt(n) + 1)

    for i in xrange(2, upper_bound):
        if n % i == 0:
            divisors[i] = True
            divisors[n / i] = True

    return divisors.keys()


def run(n):
    number_divisor_pairs = {}
    amicable_numbers = []
    total_sum = 0

    iteration_range = xrange(1, n)
    for i in iteration_range:
        sum_divisors = sum(proper_divisors(i))
        number_divisor_pairs[i] = sum_divisors

    for key, value in number_divisor_pairs.iteritems():
        try:
            if number_divisor_pairs[value] == key and key != value:
                amicable_numbers += [key, value]
        except KeyError:
            pass

    return sum(set(amicable_numbers))


if __name__ == "__main__":

    start = datetime.now()
    print run(10000)
    print datetime.now() - start
