import fileinput
from sys import argv


class Io:
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

    class Output:
        @classmethod
        def print_list_with_newLine(cls, list):
            for item in list:
                print(item)


def process(lines):
    # todo write code here:
    pass


def main(filename):
    std_in_lines = Io.Input.read_lines_from_stdIn_or_file(filename)
    process(std_in_lines)


if __name__ == '__main__':
    filename = Io.Input.get_file_name(argv)
    main(filename)
