#!/usr/bin/env python3
file_name = 'day1/input.txt'
f = open(file_name)

frequency = 0
seen = {frequency}

changes = [int(x.strip()) for x in f]
changes_count = len(changes)
position = 0


while True:
    change = changes[position]
    position = (position + 1) % changes_count
    frequency += change
    if frequency in seen:
        print(frequency)
        break
    seen.add(frequency)
