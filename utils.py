def read_file_lines(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    return lines