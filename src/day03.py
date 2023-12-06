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

    affected = list(filter(lambda coord: 0 <= coord[0] < lim_y and 0 <= coord[1] < lim_x, affected))

    # Remove possible duplicates
    return list(dict.fromkeys(affected))


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


def key_from_coord(y, x):
    return f"{y}-{x}"


def find_connected(numbers, lines):
    gears_and_parts = {}
    for number_info in numbers:
        num, line_y, s, e = number_info.values()
        adjacent = get_affected(s, e, line_y, len(lines), len(lines[0])-1)

        for (y, x) in adjacent:
            if lines[y][x] == '*':

                k = key_from_coord(y, x)
                if gears_and_parts.get(k) is None:
                    gears_and_parts[k] = []
                gears_and_parts[k].append(num)

    connected_parts = []
    for gear, part_nums in gears_and_parts.items():
        if len(part_nums) == 2:
            connected_parts.append((part_nums[0], part_nums[1]))

    return connected_parts


def main():
    lines = read_file_lines('../puzzleinputs/input03.txt')
    all_numbers = get_numbers(lines)

    # Star 1
    parts = find_parts(all_numbers, lines)
    print(sum(parts))

    # Star 2
    connected_parts = find_connected(all_numbers, lines)
    connected_multiplied = [p1 * p2 for (p1, p2) in connected_parts]
    print(sum(connected_multiplied))


if __name__ == '__main__':
    main()
