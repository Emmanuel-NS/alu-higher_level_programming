#!/usr/bin/python3
def add(a, b):
     result = 1
    if b < 0:
        for _ in range(-b):
            result /= a
    else:
        for _ in range(b):
            result *= a
    return result
