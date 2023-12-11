from utils import read_file_lines
import re


def parse_card(line) -> tuple[int, list, list]:
    [winning, guess] = line.split('|')

    [number, winning] = winning.split(':')

    [number] = re.findall("[0-9]+", number)

    winning = [int(n) for n in winning.split()]

    guess = [int(n) for n in guess.split()]

    return int(number), winning, guess


def form_number_lookup(numbers):
    # Empty dict just for lookups
    return dict.fromkeys(numbers, 0)


def calculate_card_points(winning, guesses):
    matches = get_matches(winning, guesses)

    if len(matches) == 0:
        return 0

    points = 1
    for match in matches[1:]:
        points *= 2
    return points


def get_matches(winning, guesses):
    win_lookup = form_number_lookup(winning)
    matches = []
    for guess in guesses:
        if win_lookup.get(guess) is not None:
            matches.append(guess)
    return matches


def convert_card_format(cards):
    card_stats = {num: {
        'number': num,
        'points': calculate_card_points(w, g),
        'amount': 1,
        'matches': int(len(get_matches(w, g)))
    } for num, w, g in cards}
    return card_stats


def calculate_card_amounts(card_stats):
    for card in card_stats:
        number, points, amount, matches = card_stats.get(card).values()

        for i in range(number+1, number+matches+1):
            c2 = card_stats.get(i)
            if c2 is None:
                break
            c2['amount'] += amount
    return card_stats


def main():
    lines = read_file_lines('../puzzleinputs/input04.txt')

    cards = []
    for line in lines:
        card = parse_card(line)
        cards.append(card)

    # Calculate points for Star 1
    total_points = 0
    for _, winning, guesses in cards:
        points = calculate_card_points(winning, guesses)
        total_points += points
    print(total_points)

    # Convert card format for Star 2
    card_stats = convert_card_format(cards)
    calculate_card_amounts(card_stats)

    total_cards = 0
    for card in card_stats.values():
        total_cards += card['amount']
    print(total_cards)


if __name__ == '__main__':
    main()
