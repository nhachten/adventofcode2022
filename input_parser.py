
def get_input(filename="input.txt"):
    with open(filename, 'r') as f:
        raw_lines = f.readlines()

    lines = []
    for raw_line in raw_lines:
        lines.append(raw_line.rstrip())

    return lines