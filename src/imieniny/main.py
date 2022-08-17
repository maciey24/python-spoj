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


def check_if_any_sweets_will_be_left(number_of_people_in_class: int, number_of_sweets: int):
    number_of_people_to_give_away_sweets = number_of_people_in_class - 1
    if number_of_people_to_give_away_sweets == 0:
        return True
    return (number_of_sweets % number_of_people_to_give_away_sweets) != 0


def calculate_result_string(number_of_people: int, number_of_sweets: int):
    if check_if_any_sweets_will_be_left(number_of_people, number_of_sweets):
        return "TAK"
    else:
        return "NIE"


def calculate_result(line: str):
    words = line.split()
    number_of_people:int = int(words[0])
    number_of_sweets:int = int(words[1])
    return calculate_result_string(number_of_people, number_of_sweets)


def check(lines_to_process: List[str]):
    results = []
    for line in lines_to_process:
        results.append(calculate_result(line))
    return results


def process(lines: List[str]):
    number_of_cases = int(lines[0])
    lines_to_process = lines[1:1+number_of_cases]
    results = check(lines_to_process)
    Io.Output.print_list_with_newLine(results)


def main(filename):
    std_in_lines = Io.Input.read_lines_from_stdIn_or_file(filename)
    process(std_in_lines)


if __name__ == '__main__':
    filename = Io.Input.get_file_name(argv)
    main(filename)
