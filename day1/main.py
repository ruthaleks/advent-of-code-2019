#!/usr/bin/python3 

import sys

def calc_fuel(mass):
    x = (mass // 3) - 2
    if x < 0:
        return 0
    return x + calc_fuel(x)

def main(): 
    indata = tuple(map(int, sys.stdin.readlines()))

    res1 = sum(map(lambda x: x // 3 - 2, indata))
    res2 = sum(map(calc_fuel, indata))

    print(f"Part 1: {res1}")
    print(f"Part 2: {res2}")


if __name__ == "__main__":
    main()
