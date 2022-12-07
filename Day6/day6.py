import sys

sys.path.append("../../AoC2022")

from input_parser import get_input

def partN(stream, num_distinct_chars=4):
    for i in range(num_distinct_chars,len(stream)):
        sub_stream = stream[i-num_distinct_chars:i]
        # a set removes duplicates, so if the len is the same that means no dups
        if len(set(sub_stream)) == len(sub_stream):
            # i is the number of characters 
            return i

    return None

def main(input_lines, num_distinct_chars):
    stream = input_lines[0]

    result = partN(stream, num_distinct_chars)
    print(result)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        num_distinct_chars = int(sys.argv[1])
    else:
        num_distinct_chars = 4

    input_lines = get_input()
    main(input_lines, num_distinct_chars)