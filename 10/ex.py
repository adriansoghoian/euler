

def generate_primes(upper_bound):
    primes = [2]
    target = 3

    while target < upper_bound:
        prime = True
        
        for each in primes:
            if target % each == 0:
                prime = False
                break 

        if prime:
            primes.append(target)
        target += 2

    return sum(primes)


if __name__ == "__main__":

    print generate_primes(2000000)

