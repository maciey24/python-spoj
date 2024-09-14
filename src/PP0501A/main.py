import fileinput
from collections import namedtuple
from sys import argv

from typing import List


class Io:
    class Input:
        @classmethod
        def read_lines_from_stdIn_or_file(cls, filename):
            return [line for line in fileinput.input(filename)]

        @classmethod
        def get_file_name(cls, argv):
            if len(argv) > 1:
                return argv[1]
            else:
                return None

    class Output:
        @classmethod
        def print_list_with_newLine(cls, list):
            for item in list:
                print(item)


# nonoptimal but very little logic
def nwd(first: int, second: int) -> int:
    i = first
    while i >= 1:
        if first % i == 0 and second % i == 0:
            return i
        i -= 1
    raise ArithmeticError("could not find nwd")


def process_input_line(line: str) -> int:
    first_num_as_string, second_num_as_string = line.split()
    nwd_val = nwd(int(first_num_as_string), int(second_num_as_string))
    return nwd_val


def process(lines: List[str]):
    lines_stripped = [line.strip() for line in lines]
    number_of_data_lines, *data = lines_stripped

    result = []
    for i in range(int(number_of_data_lines)):
        result.append(process_input_line(data[i]))

    Io.Output.print_list_with_newLine(result)


def main(filename):
    std_in_lines = Io.Input.read_lines_from_stdIn_or_file(filename)
    process(std_in_lines)


if __name__ == '__main__':
    filename = Io.Input.get_file_name(argv)
    main(filename)
