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

PAWN_CHAR = '#'
EMPTY_CHAR = '.'

def calculate_pawn_count_per_row(data: str, m: int):
    pawn_counts = []
    for i in range(m):
        count = data[i].count(PAWN_CHAR)
        pawn_counts.append(count)
    return pawn_counts


def calculate_pawn_count_per_file(data: str, n: int):
    pawn_counts = []
    for i in range(n):
        file_string = [line[i] for line in data]
        count = file_string.count(PAWN_CHAR)
        pawn_counts.append(count)
    return pawn_counts


def process(lines: List[str]):
    lines_stripped = [line.strip() for line in lines]
    table_dimensions, *data = lines_stripped
    m, n = [int(number) for number in str(table_dimensions).split()]
    pawn_count_per_row = calculate_pawn_count_per_row(data, m)
    pawn_count_per_file = calculate_pawn_count_per_file(data, n)
    max_found_so_far = 0
    for x in range(m):
        for y in range(n):
            if data[x][y] == EMPTY_CHAR:
#                 calculate sum of file count and row count:
                number_of_pawns_attacked = pawn_count_per_row[x] + pawn_count_per_file[y]
                if number_of_pawns_attacked > max_found_so_far:
                    max_found_so_far=number_of_pawns_attacked
    print(max_found_so_far)

def main(filename):
    std_in_lines = Io.Input.read_lines_from_stdIn_or_file(filename)
    process(std_in_lines)


if __name__ == '__main__':
    filename = Io.Input.get_file_name(argv)
    main(filename)
