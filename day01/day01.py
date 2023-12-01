import re
from utils import read_file_lines


def get_number(line):
    digits_in_line = re.findall("[0-9]", line, re.ASCII)
    first, last = digits_in_line[0], digits_in_line[-1]
    # The digits are still strings so + will concatenate them
    return int(first + last)


def main():
    filename = 'input01.txt'
    lines = read_file_lines(filename)
    digits = []
    for line in lines:
        digits.append(get_number(line))
    answer = sum(digits)
    print(answer)


if __name__ == '__main__':
    main()
