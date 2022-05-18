import fileinput
from sys import argv

from typing import List


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


def first_letter_capital_in_each_word(line):
    result=''
    for i in range(len(line)):
        if i!=0 and line[i-1]==' ':
            result+=line[i].capitalize()
        else:
            result+=line[i]
    return result


def remove_spaces(words_capital):
    result=''
    for char in words_capital:
        if char == ' ':
            pass
        else:
            result+=char
    return result

def camel_case(line):
    words_capital = first_letter_capital_in_each_word(line)
    removed_spaces = remove_spaces(words_capital)
    return removed_spaces


def process(lines: List[str]):
    for line in lines:
        camel_case_string = camel_case(line)
        print(camel_case_string, end='')
    pass


def main(filename):
    std_in_lines = Io.Input.read_lines_from_stdIn_or_file(filename)
    process(std_in_lines)


if __name__ == '__main__':
    filename = Io.Input.get_file_name(argv)
    main(filename)
