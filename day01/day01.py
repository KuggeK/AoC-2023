import re
from utils import read_file_lines

NUMBER_STRINGS = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}

def only_digits(line):
    return re.findall("[0-9]", line, re.ASCII)


def get_number_star1(line):
    digits_in_line = only_digits(line)
    first, last = digits_in_line[0], digits_in_line[-1]
    # The digits are still strings so + will concatenate them
    return int(first + last)


def get_number_star2(line):
    # First replace the written numbers to digits but then it is the same
    # as the first star
    for num in NUMBER_STRINGS:
        line = line.replace(num, NUMBER_STRINGS[num])
    return get_number_star1(line)


def main():
    filename = 'input01.txt'
    lines = read_file_lines(filename)
    star1_digits = []
    star2_digits = []
    for line in lines:
        star1_digits.append(get_number_star1(line))
        star2_digits.append(get_number_star2(line))
    answer1 = sum(star1_digits)
    answer2 = sum(star2_digits)
    print(f"Answer for star 1: {answer1}")
    print(f"Answer for star 2: {answer2}")


if __name__ == '__main__':
    main()
