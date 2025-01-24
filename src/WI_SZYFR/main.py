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
        def print_list_with_newLine(cls, list):
            for item in list:
                print(item, end="")

        @classmethod
        def print_list_with_newLine(cls, list):
            for item in list:
                print(item)


def encipher(text: str, key: str) -> str:
    key_len = len(key)
    result = ""
    for i in range(len(text)):
        char = text[i]
        key_index = i % key_len
        key_number = int(key[key_index])
        char_code = ord(char)
        new_char_code = (char_code + key_number) % 65 + 65
        new_char = chr(new_char_code)
        result += new_char
    return result


def decipher(text: str, key: str) -> str:
    key_len = len(key)
    result = ""
    for i in range(len(text)):
        char = text[i]
        key_index = i % key_len
        key_number = int(key[key_index])
        char_code = ord(char)
        new_char_code = (char_code - key_number) % 65 + 65
        new_char = chr(new_char_code)
        result += new_char
    return result


def process(lines: List[str]):
    lines_stripped = [line.strip() for line in lines]
    operation = lines_stripped[0]
    key = lines_stripped[1]
    text = lines_stripped[2]
    if operation == "SZYFRUJ":
        enciphered = encipher(text, key)
        print(enciphered)
    if operation == "DESZYFRUJ":
        deciphered = decipher(text, key)
        print(deciphered)


def main(filename):
    std_in_lines = Io.Input.read_lines_from_stdIn_or_file(filename)
    process(std_in_lines)


if __name__ == '__main__':
    filename = Io.Input.get_file_name(argv)
    main(filename)
