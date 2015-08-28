from numba import jit
from datetime import datetime

@jit
def collatz_sequence(number):
    count = 0
    while True:
        if number == 1: return count

        if number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1

        count += 1


def run():
    best = (1,1) # (start, length of collaz sequence)

    for i in xrange(1, 1000001):
        next = (i, collatz_sequence(i))

        if next[1] > best[1]: 
            best = next

    return best[0]


if __name__ == "__main__":
    start = datetime.now()
    print run()
    print datetime.now() - start
