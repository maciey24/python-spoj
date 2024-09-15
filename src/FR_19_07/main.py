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


strings_to_be_removed = [":)", ":(", ";)", ":D", ":P", "xD", ":>", "<3"]


def process_input_line(line: str) -> str:
    result = line
    for emoticon in strings_to_be_removed:
        result = result.replace(emoticon, "")
    return result


def process(lines: List[str]):
    lines_stripped = [line.strip() for line in lines]
    number_of_data_lines, *data = lines_stripped
    number_of_data_lines = str(int(number_of_data_lines) * 2)

    result = []
    for i in range(1, int(number_of_data_lines), 2):
        result.append(process_input_line(data[i]))

    Io.Output.print_list_with_newLine(result)


def main(filename):
    std_in_lines = Io.Input.read_lines_from_stdIn_or_file(filename)
    process(std_in_lines)


if __name__ == '__main__':
    filename = Io.Input.get_file_name(argv)
    main(filename)
