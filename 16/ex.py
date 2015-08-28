from numba import jit



def calculate_total():
    return 2 ** 1000


def run():
    running_sum = 0
    total = calculate_total()

    total_string = str(total)
    for char in total_string:
        running_sum += int(char)

    return running_sum


print run()