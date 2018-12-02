#!/usr/bin/env python3


def compare_lines(line_one, line_two):
    # Assume same length
    diff = 0
    last_diff_position = 0
    for i in range(len(line_one)):
        letter_one = line_one[i]
        letter_two = line_two[i]
        if letter_one != letter_two:
            diff += 1
            last_diff_position = i
    return diff, last_diff_position


def main():
    file_name = 'input.txt'

    f = open(file_name)
    lines = [x.strip() for x in f]
    for line_one in lines:
        for line_two in lines:
            diff, last_diff_position = compare_lines(line_one, line_two)
            if diff == 1:
                answer = line_one[:last_diff_position] + line_two[last_diff_position + 1:]
                print(answer)
                return


if __name__ == '__main__':
    main()