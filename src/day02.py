from collections import namedtuple
from utils import read_file_lines

GAME_CONF = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def count_game(line: str):
    [id, sets] = line.split(':')
    id = id.split()[-1]
    game = {'id': id, 'red': 0, 'green': 0, 'blue': 0}

    sets = sets.split(';')
    for set in sets:
        cubes = set.split(',')
        for cube in cubes:
            [amount, color] = cube.split()
            amount = int(amount)

            if game[color] < amount:
                game[color] = amount

    return game


def count_game_power(game):
    amounts = []
    for key, value in game.items():
        if key != 'id':
            amounts.append(value)

    power = 1
    for amount in amounts:
        power *= amount
    return power

def main():
    lines = read_file_lines('../puzzleinputs/input02.txt')
    valid_games = []
    game_powers = []
    for line in lines:
        game_valid = True
        game = count_game(line)

        power = count_game_power(game)
        game_powers.append(power)

        for color in GAME_CONF:
            if (GAME_CONF[color]) < game[color]:
                game_valid = False
                break
        if game_valid:
            valid_games.append(int(game['id']))

    print('Sum:', sum(valid_games))
    print('Power:', sum(game_powers))


if __name__ == '__main__':
    main()