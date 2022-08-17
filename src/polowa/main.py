from sys import argv

from input import Input


def get_half(line):
    length = len(line)
    half_length = int(length / 2)
    line_half = line[:half_length]
    return line_half


def get_first_halves_of_elements(lines):
    halves = []
    for line in lines:
        halves.append(get_half(line))
    return halves


def get_first_halves_of_elements_from_2nd(lines):
    lines_to_process = lines[1:]
    return get_first_halves_of_elements(lines_to_process)


def print_list_with_newLine(list):
    for item in list:
        print(item)


def process(lines):
    halves = get_first_halves_of_elements_from_2nd(lines)
    print_list_with_newLine(halves)


def main(filename):
    input_lines = Input.read_lines_from_stdIn_or_file(filename)
    process(input_lines)


if __name__ == '__main__':
    filename = Input.get_file_name(argv)
    main(filename)
