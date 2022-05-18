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


def find_shorter_length(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if len1 < len2:
        return len1
    return len2


def stringmerge_strings(strings):
    result = ""
    str1 = strings[0]
    str2 = strings[1]
    length = find_shorter_length(str1, str2)
    for i in range(length):
        result += str1[i]
        result += str2[i]
    return result


def stringmerge_string(line):
    strings = str(line).split()
    return stringmerge_strings(strings)


def stringmerge_list(lines):
    merged = []
    for line in lines:
        merged.append(stringmerge_string(line))
    return merged


def process(lines):
    lines_to_process = lines[1:]
    merged = stringmerge_list(lines_to_process)
    Io.Output.print_list_with_newLine(merged)


def main(filename):
    std_in_lines = Io.Input.read_lines_from_stdIn_or_file(filename)
    process(std_in_lines)


if __name__ == '__main__':
    filename = Io.Input.get_file_name(argv)
    main(filename)
