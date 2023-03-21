#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = [0, 1]
    i = 2
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print(sequence)
    else:
        while i < length:
            new_num = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
            sequence.append(new_num)
            i += 1
        print(sequence)
