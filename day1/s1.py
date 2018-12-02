#!/usr/bin/env python3
file_name = 'day1/input.txt'
f = open(file_name)

answer = sum((int(x.strip()) for x in f))

print(answer)
