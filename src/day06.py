from utils import read_file_lines


def parse_line(line):
    [_, parsed] = line.split(':')
    return [int(p) for p in parsed.split()]


def main():
    [times, distances] = read_file_lines('../puzzleinputs/input06.txt')
    times = parse_line(times)
    distances = parse_line(distances)

    # Star 1
    answer = 1
    for time, distance in zip(times, distances):
        winning_outcomes = calculate_winning_outcomes(time, distance)
        answer *= len(winning_outcomes)
    print('Star 1:', answer)

    # Star 2
    time = int(''.join([str(time) for time in times]))
    record_dist = int(''.join(str(distance) for distance in distances))

    # Binary search
    left = 0
    right = len(range(1, time-1))

    # find left bound
    left_bound = -1
    while left <= right:
        mid = (left + right) // 2
        mid_dist = calculate_dist(mid, time)
        if record_dist < mid_dist:
            right = mid - 1
            left_bound = mid
        elif record_dist > mid_dist:
            left = mid + 1
        else:
            left_bound = mid + 1
            break

    left = left_bound + 1
    right = len(range(1, time - 1))

    # find right bound
    right_bound = -1
    while left <= right:
        mid = (left + right) // 2
        mid_dist = calculate_dist(mid, time)
        if record_dist > mid_dist:
            right = mid - 1
        elif record_dist < mid_dist:
            left = mid + 1
            right_bound = mid + 1
        else:
            right_bound = mid
            break

    print('Star 2:', right_bound - left_bound)


def calculate_dist(time_pressed, total_time):
    return time_pressed * (total_time - time_pressed)


def calculate_winning_outcomes(time, record_dist):
    outcomes = []
    for time_pressed in range(1, time-1):
        dist = calculate_dist(time_pressed, time)
        if dist > record_dist:
            outcomes.append(time_pressed)
    return outcomes


if __name__ == '__main__':
    main()
