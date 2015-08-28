

def read_input_file(file):
    for line in open(file, 'rb').readlines():
        yield int(line.rstrip())
        

def calculate():
    line_generator = read_input_file('input.txt')
    running_sum = 0

    while True:
        try:
            next = line_generator.next()
            running_sum += next
        except Exception as e:
            print str(running_sum)[:10]
            break



if __name__ == "__main__":
    calculate()