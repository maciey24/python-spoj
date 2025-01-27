import fileinput
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
        def print_list(cls, list):
            for item in list:
                print(item, end="")

        @classmethod
        def print_list_with_newLine(cls, list):
            for item in list:
                print(item)


_EMPTY_CHAR = '.'


def process(lines: List[str]) -> List[str]:
    lines_stripped = [line.strip() for line in lines]
    result = []
    n = int(lines_stripped[0])
    s = lines_stripped[1]
    middle_index = int(n / 2 + 1)
    number_of_levels = middle_index + 1
    for i in range(1, number_of_levels):
        empty_chars = int(((n - i * 2) / 2) + 1) * _EMPTY_CHAR
        result_line = f"{empty_chars}{s[middle_index - i: middle_index + i - 1]}{empty_chars}"
        result.append(result_line)
    return result


def main(filename):
    std_in_lines = Io.Input.read_lines_from_stdIn_or_file(filename)
    result = process(std_in_lines)
    Io.Output.print_list_with_newLine(result)


if __name__ == '__main__':
    filename = Io.Input.get_file_name(argv)
    main(filename)
