#!/usr/bin/python3

import sys


def check_criteria(p):
    if len(p) != 6:
        return "Not a six-digit number"
    prev = -1
    adj = False
    for i in p:
        if int(i) == prev: 
            adj = True
        if prev > int(i):
            return "Found a decreasing pair"
        prev = int(i)
    if adj:
        return "ok"
    return "No double"

def check_doubles(p):
    p = tuple(map(int,p))
    for idx, num in enumerate(p):
        if idx > 0:
            if num == p[idx-1]: 
                if idx == 1 and p[idx+1] != num:
                    return "ok"
                if idx == 5 and p[idx-2] != num:
                    return "ok"
                if p[idx-2] != num and p[idx+1] != num:
                    return "ok"
    return "No double"

        



def main():
    start, stop = map(int, sys.stdin.readline().strip().split("-"))
    res1, res2 = 0, 0
    for i in range(start, stop+1):
        if check_criteria(str(i)) == "ok":
            res1 += 1
            if check_doubles(str(i)) == "ok":
                res2 += 1
    
    print(f"Part 1: {res1}")
    print(f"Part 2: {res2}")

    

if __name__ == "__main__":
    main()
