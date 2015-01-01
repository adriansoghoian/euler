
def is_prime(num, plist):
    for p in plist:
        if num % p == 0:
            return False
    return True


def find_nth_prime(n):
    primes = [2]
    num_primes = 1
    target = 3
    while num_primes < n:
        if is_prime(target, primes):
            primes.append(target)
            num_primes += 1
            print target
        target += 1
    return primes[-1]


if __name__ == "__main__":
    print find_nth_prime(10001)