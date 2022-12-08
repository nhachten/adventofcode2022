import sys

sys.path.append("../../AoC2022")

from input_parser import get_input


class Directory:

    def __init__(self, name, parent):
        print("creating dir with name : {}".format(name))
        self.name = name
        self.parent = parent 
        self.subnodes = {}

    def add_file_or_dir(self, node):
        self.subnodes[node.name] = node

    def get_dir_size(self, path='', memo={}):
        size = 0

        if self.name != '/':
            fullpath = path + self.name + '/'
        else:
            fullpath = '/'

        print("name: {}".format(self.name))
        print("path: {}".format(path))
        print("fullpath: {}".format(fullpath))

        for n in self.subnodes.values():
            if type(n) is File:
                size += n.size
            elif type(n) is Directory:
                size += n.get_dir_size(fullpath, memo)

        memo[fullpath] = size
        return size

    def tree(self, ident=' '):
        print("{}{}".format(ident, self.name))
        for n in self.subnodes.values():
            n.tree(ident + ' '*2)


class File:

    def __init__(self, name, size):
        print("creating file with name : {}".format(name))
        self.name = name
        self.size = int(size)

    def tree(self, ident=''):
        print("{}{}".format(ident, self.name))

class Terminal:

    def __init__(self):
        self.pwd = Directory("/", None)
        self.root = self.pwd

    def process_cmd(self, cmd, cmd_output):
        cmd_parts = cmd.split(' ')

        if cmd_parts[0] == 'cd':
            dest_dir = cmd_parts[1]
            if dest_dir == "/":
                self.pwd = self.root
            elif dest_dir == "..":
                self.pwd = self.pwd.parent
            else:
                try:
                    self.pwd = self.pwd.subnodes[dest_dir]
                except:
                    print("{} directory does not exist, can't move there".format(dest_dir))
        elif cmd_parts[0] == 'ls':
            for listing in cmd_output:
                listing_parts = listing.split(' ')
                if listing_parts[0] == 'dir':
                    self.pwd.add_file_or_dir(Directory(listing_parts[1], self.pwd))
                else:
                    self.pwd.add_file_or_dir(File(listing_parts[1], listing_parts[0]))

def main(input_lines):
    term = Terminal()

    cmd = '$ start'
    cmd_output = []
    for line in input_lines:
        # begin parsing new command
        if line[0] == '$':
            # process the current command, skipping '$ '
            term.process_cmd(cmd[2:], cmd_output)
            cmd = line
            cmd_output = []
        else:
            cmd_output.append(line)

    # send last command
    term.process_cmd(cmd.split(' ')[1], cmd_output)

    term.root.tree()
    dir_sizes = {}
    current_in_use = term.root.get_dir_size(memo=dir_sizes)
    print(dir_sizes)

    answer = 0
    for k, v in dir_sizes.items():
        if v < 100000:
            print("k: {}".format(k))
            print("v: {}".format(v))
            answer += v

    i# part 1
    print(answer)

    total_space = 70000000
    needed_space = 30000000

    print("current in use: {}".format(current_in_use))
    leftover_space = total_space - current_in_use
    print("current left: {}".format(leftover_space))
    need_to_free = needed_space - leftover_space
    print("need to free: {}".format(need_to_free))

    sizes = list(dir_sizes.values())
    sizes.sort()
    print(sizes)

    # part 2
    for s in sizes:
        if s > need_to_free:
            print(s)
            break


if __name__ == "__main__":
    input_lines = get_input()
    main(input_lines)