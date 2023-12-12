def read_file_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()
