#!/usr/bin/env python3
from collections import defaultdict


def count_line(line):
    letters_distribution = defaultdict(int)
    for letter in line:
        letters_distribution[letter] += 1

    uniq_values = set(letters_distribution.values())
    has_2 = 1 if 2 in uniq_values else 0
    has_3 = 1 if 3 in uniq_values else 0

    return has_2, has_3


def main():
    file_name = 'input.txt'

    f = open(file_name)
    total_2 = total_3 = 0
    for line in (x.strip() for x in f):
        current_2, current_3 = count_line(line)
        total_2 += current_2
        total_3 += current_3

    checksum = total_2 * total_3

    print(checksum)


if __name__ == '__main__':
    main()
