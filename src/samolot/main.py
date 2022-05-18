import fileinput
from sys import argv


class Input:
    @classmethod
    def read_lines_from_stdIn_or_file(cls, filename):
        lines = []
        for line in fileinput.input(filename):
            lines.append(line)
        return lines

    @classmethod
    def get_file_name(cls, argv):
        if len(argv) > 1:
            return argv[1]
        else:
            return None


def calculate_1times2_plus_3times4(numbers):
    return (numbers[0] * numbers[1]) + (numbers[2] * numbers[3])


def get_as_ints(numbers_as_strings):
    numbers = []
    for number in numbers_as_strings:
        numbers.append(int(number))
    return numbers


def process(lines):
    numbers_in_one_string = str(lines[0])
    numbers_as_strings = numbers_in_one_string.split()
    numbers = get_as_ints(numbers_as_strings)
    result = calculate_1times2_plus_3times4(numbers)
    print(result)


def main(filename):
    std_in_lines = Input.read_lines_from_stdIn_or_file(filename)
    process(std_in_lines)


if __name__ == '__main__':
    filename = Input.get_file_name(argv)
    main(filename)
