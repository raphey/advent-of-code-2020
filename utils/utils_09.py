import re


def regex(r_string):
    if 'parser' not in globals():
        global parser
        parser = re.compile(r_string)
    return parser


def translate(string, input_chars, output_chars):
    if 'trans_map' not in globals():
        global trans_map
        trans_map = str.maketrans(input_chars, output_chars)
    return string.translate(trans_map)


def get_regex_search(string, r_string):
    m = regex(r_string).search(string)
    return m.groups()


def get_regex_findall(string, r_string):
    return regex(r_string).findall(string)


def gen_raw_items(raw_input, split_token='\n'):
    for raw_item in raw_input.strip().split(split_token):
        yield raw_item.strip()


class GameConsole(object):
    def __init__(self, commands):
        self.commands = commands
        self.accumulator = 0
        self.i = 0
        self.visited = set()
        self.finished = False
        self.command_dict = {
            'acc': self.acc,
            'jmp': self.jmp,
            'nop': self.nop,
        }

    def acc(self, x):
        self.accumulator += x
        self.i += 1

    def jmp(self, x):
        self.i += x

    def nop(self, _):
        self.i += 1

    def should_terminate(self):
        return self.i in self.visited

    def execute_one_command(self):
        self.visited.add(self.i)
        command, amount = self.commands[self.i]
        self.command_dict[command](amount)

    def get_exit_code(self):
        return 0

    def execute(self):
        while not self.should_terminate():
            self.execute_one_command()
        return self.get_exit_code()


class TweakedGameConsole(GameConsole):
    def __init__(self, commands, tweak_j):
        super(TweakedGameConsole, self).__init__(commands)
        self.tweak_j = tweak_j

    def should_terminate(self):
        return self.i in self.visited or self.i >= len(self.commands)

    def execute_one_command(self):
        self.visited.add(self.i)
        command, amount = self.commands[self.i]
        if self.i == self.tweak_j:
            if command == 'jmp':
                command = 'nop'
            elif command == 'nop':
                command = 'jmp'
        self.command_dict[command](amount)

    def get_exit_code(self):
        return 0 if self.i >= len(self.commands) else 1
