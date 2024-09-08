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


FunnySum = namedtuple('FunnySum', ['sum', 'number_of_adds'])


def is_palindrom(number: int) -> bool:
    number_str = str(number)
    length = len(number_str)
    for i in range(int(length / 2)):
        if number_str[i] != number_str[-i]:
            return False
    return True


def reversed_int(number: int) -> int:
    number_str = str(number)
    length = len(number_str)
    number_reversed_str = ''
    for i in range(1, length+1):
        number_reversed_str += number_str[-i]
    return int(number_reversed_str)


def funny_add(number: int) -> FunnySum:
    number_of_adds = 0
    sum = number
    number_with_original_digits = number
    number_with_reversed_digits = reversed_int(number)
    while number_with_reversed_digits != number_with_original_digits:
        sum = number_with_reversed_digits + number_with_original_digits
        number_with_original_digits = sum
        number_with_reversed_digits = reversed_int(number_with_original_digits)
        number_of_adds += 1
    return FunnySum(sum=sum, number_of_adds=number_of_adds)


def process(lines: List[str]):
    lines_stripped = [line.strip() for line in lines]
    number_of_data_lines, *data = lines_stripped

    result = []
    for i in range(int(number_of_data_lines)):
        result.append(funny_add(int(data[i])))

    result_str_lines = [f"{result.sum} {result.number_of_adds}" for result in result]
    Io.Output.print_list_with_newLine(result_str_lines)


def main(filename):
    std_in_lines = Io.Input.read_lines_from_stdIn_or_file(filename)
    process(std_in_lines)


if __name__ == '__main__':
    filename = Io.Input.get_file_name(argv)
    main(filename)
