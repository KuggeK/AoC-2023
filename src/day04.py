from utils import read_file_lines


def parse_card(line) -> tuple[list, list]:
    [winning, guess] = line.split('|')

    [_, winning] = winning.split(':')
    winning = [int(n) for n in winning.split()]

    guess = [int(n) for n in guess.split()]

    return winning, guess


def form_number_lookup(numbers):
    # Empty dict just for lookups
    return dict.fromkeys(numbers, 0)


def calculate_card_points(winning, guesses):
    win_lookup = form_number_lookup(winning)

    matches = []
    for guess in guesses:
        if win_lookup.get(guess) is not None:
            matches.append(guess)

    if len(matches) == 0:
        return 0

    points = 1
    for match in matches[1:]:
        points *= 2
    return points


def main():
    lines = read_file_lines('../puzzleinputs/input04.txt')

    cards = []
    for line in lines:
        card = parse_card(line)
        cards.append(card)

    total_points = 0
    for winning, guesses in cards:
        total_points += calculate_card_points(winning, guesses)

    print(total_points)

if __name__ == '__main__':
    main()
