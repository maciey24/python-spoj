import fileinput


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