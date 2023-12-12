from utils import read_file_lines
import re


def run_value_through_maps(value, initial_category, destination_category, maps):
    current_category = initial_category

    while current_category != destination_category:
        # Find the map corresponding to the current category
        current_map = next(m for m in maps if m['source'] == current_category)

        # Check the conversion ranges for the current map
        for r in current_map.get('ranges'):
            source_range = range(r['src_start'], r['src_start'] + r['range'])

            # If a conversion map is found, convert the value according to it
            if value in source_range:
                value = r['dest_start'] + value - r['src_start']
                break

        # Conversion can continue to the next category
        current_category = current_map['destination']

    return value


def main():
    lines = read_file_lines('../puzzleinputs/input05.txt')
    lines = [line.strip() for line in lines]

    # Parse the seeds out into a list
    [_, seeds] = lines[0].split(':')
    seeds = [int(seed) for seed in seeds.split()]

    # Get the starting indexes of each map
    pattern = re.compile(r"\b\w+(-to-)\w+\s(map:)")
    map_start_indexes = []
    for i, line in enumerate(lines):
        if pattern.match(line):
            map_start_indexes.append(i)

    # Form the maps
    maps = []
    for i, map_start in enumerate(map_start_indexes):
        [name, _] = lines[map_start].split()
        [source, _, destination] = name.split('-')
        conv_map = {
            'source': source,
            'destination': destination,
        }
        # If not last map
        if i != len(map_start_indexes)-1:
            conv_map['lines'] = lines[map_start + 1:map_start_indexes[i + 1] - 1]
        else:
            conv_map['lines'] = lines[map_start+1:]

        maps.append(conv_map)

    # Form the conversion ranges from each line in the maps
    for m in maps:
        m['ranges'] = []
        for line in m.get('lines'):
            [d, s, r] = line.split()
            m['ranges'].append({
                'dest_start': int(d),
                'src_start': int(s),
                'range': int(r)
            })
        # The raw lines are no longer really needed after this processing
        m.pop('lines')

    # Input all seeds through the maps
    locations = []
    for seed in seeds:
        locations.append(run_value_through_maps(seed, 'seed', 'location', maps))

    print('Star 1:', min(locations))
    

if __name__ == '__main__':
    main()
