# Using Euclid's method for finding Pythagorean triplets: http://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples


def return_factor_tuples(n):
    """
    Returns a list of tupes of all the (x, y) factor combos for an integer n.
    """
    factors = []
    for i in range(1, int(n**(.5)) + 1):
        if n % i == 0:
            factors.append((i, n / i))

    return factors


def find_remaining_sides(known_side):
    """
    b = 2mn for a known / inputted b, where m and n are possible factor pairs.
    a = (m^2 - n^2) for the possible (m, n) combinations. 
    c = (m^2 + n^2) for the possible (m, n) combinations.
    """
    mn = known_side / 2
    mn_pairs = return_factor_tuples(mn)

    for each in mn_pairs:
        b = known_side
        a = abs(each[0]**2 - each[1]**2)
        c = abs(each[0]**2 + each[1]**2)
        if a + b + c == 1000:
            return True, [a, b, c]

    return False, None


def main():
    for i in range(3, 600):
        success, result = find_remaining_sides(i)
        if success:
            return result


if __name__ == "__main__":
    answer = main()
    print reduce(lambda x, y: x*y, answer)