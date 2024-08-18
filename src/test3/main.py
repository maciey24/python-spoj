import fileinput
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


def process(lines: List[str]):
    results = []
    count_42_preceeded_by_some_other_number = 0
    for line in lines:
        if line.startswith("42") and results and results[-1] != '42':
            count_42_preceeded_by_some_other_number += 1
        results.append(line[0:2])
        if count_42_preceeded_by_some_other_number == 3:
            break

    Io.Output.print_list_with_newLine(results)


def main(filename):
    std_in_lines = Io.Input.read_lines_from_stdIn_or_file(filename)
    process(std_in_lines)


if __name__ == '__main__':
    filename = Io.Input.get_file_name(argv)
    main(filename)
