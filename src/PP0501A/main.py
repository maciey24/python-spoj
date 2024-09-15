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


class PrimeSupplier:
    def __init__(self):
        self.prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

    @classmethod
    def is_prime(cls, i: int) -> bool:
        for j in range(3, int(i/2)+1, 2):
            if i % j == 0:
                return False
        return True

    def get(self, index: int) -> int:
        if index >= len(self.prime_numbers):
            self.extend_array(index)
        return self.prime_numbers[index]

    def extend_array(self, index: int):
        current_length = len(self.prime_numbers)
        current_max_prime = self.prime_numbers[current_length - 1]
        for i in range(current_max_prime + 2, 1000000, 2):
            if self.is_prime(i):
                self.prime_numbers.append(i)
                if len(self.prime_numbers) - 1 == index:
                    return

    def size(self):
        return len(self.prime_numbers)


prime_numbers = PrimeSupplier()


# todo :
# not working for big numbers like first=101*5, second = 101*6
def nwd(first: int, second: int) -> int:
    i = 0
    common_prime_factors = []
    while i < first and i < second:
        prime = prime_numbers.get(i)
        if first % prime == 0 and second % prime == 0:
            common_prime_factors.append(prime)
            first = int(first / prime)
            second = int(second / prime)
        else:
            i += 1

    result = 1
    for c in common_prime_factors:
        result *= c
    return result


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
