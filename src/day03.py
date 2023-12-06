from utils import read_file_lines
import re

"""
Number dict format:
{
    'num': int,
    'coords': list(tuple(y,x))
}
"""


def get_number_indexes_from_line(line: str):
    nums = [m.span() for m in re.finditer('[0-9]+', line)]
    return nums


def get_num_from_span(start, end, line: str):
    num = "".join([c for c in line[start:end]])
    return int(num)


def get_affected(start, end, y, lim_y, lim_x):
    affected = [(y, start-1), (y-1, start-1), (y+1, start-1)]
    affected += [(y, end), (y-1, end), (y+1, end)]

    for x in range(start, end+1):
        affected += [(y+1, x), (y-1, x)]

    affected = filter(lambda coord: 0 <= coord[0] < lim_y and 0 <= coord[1] < lim_x, affected)
    return list(affected)


def find_parts(numbers, lines):
    parts = []
    for dic in numbers:
        num, y_coord, start, end = dic.values()
        affected = get_affected(start, end, y_coord, len(lines), len(lines[0])-1)

        for (y, x) in affected:
            aff = lines[y][x]

            if not aff.isnumeric() and aff != '.':
                parts.append(num)
                break

    return parts


def get_numbers(lines):
    all_numbers = []
    for y in range(len(lines)):
        number_spans = get_number_indexes_from_line(lines[y])
        line_numbers = [(get_num_from_span(s, e, lines[y]), (s, e)) for (s, e) in number_spans]

        for (num, (start, end)) in line_numbers:
            all_numbers.append({
                'num': num,
                'y': y,
                'start': start,
                'end': end
            })
    return all_numbers


def main():
    lines = read_file_lines('../puzzleinputs/input03.txt')
    all_numbers = get_numbers(lines)
    parts = find_parts(all_numbers, lines)
    print(sum(parts))


if __name__ == '__main__':
    main()