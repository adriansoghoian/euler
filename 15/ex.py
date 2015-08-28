


def lattice_path(grid_size):
    count = 0
    steps_down_remaining = grid_size
    steps_right_remaining = grid_size


    def run_path(height, width):
        while True:
            if steps_down_remaining > 0:
                steps_down_remaining -= 1



        while steps_right_remaining > 0:
            steps_right_remaining -= 1



    return count


if __name__ == "__main__":
    print lattice_path(20, 20)