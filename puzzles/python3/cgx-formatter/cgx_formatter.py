class CGXFormatter:
    def __init__(self):
        self.BASE_INDENT = 4
        self.inside_string = False
        self.total_indent = 0
        self.new_line = True
        self.nb_lines = 0

    def read_lines(self):
        self.nb_lines = int(input())
        for _ in range(self.nb_lines):
            line = input()
            for character in line:
                self.read_char(character)

    def read_char(self, character: str):
        if self.inside_string:
            if character == '\'':
                self.inside_string = False
            self.print_char(character)
        else:
            self.read_char_outside_string(character)

    def read_char_outside_string(self, character: str):
        if character == ' ' or character == '\t':
            return
        if character == '\'':
            self.inside_string = True
            self.print_char(character)
        elif character == '(':
            if not self.new_line:
                self.print_new_line()
            self.print_char(character)
            self.print_new_line()
            self.total_indent += self.BASE_INDENT
        elif character == ')':
            self.total_indent -= self.BASE_INDENT
            if not self.new_line:
                self.print_new_line()
            self.print_char(character)
        elif character == ';':
            self.print_char(character)
            self.print_new_line()
        else:
            self.print_char(character)

    def print_char(self, character: str):
        if self.new_line:
            for _ in range(self.total_indent):
                print(' ', end='')
            self.new_line = False
        print(character, end='')

    def print_new_line(self):
        print()
        self.new_line = True


if __name__ == "__main__":
    formatter = CGXFormatter()
    formatter.read_lines()
