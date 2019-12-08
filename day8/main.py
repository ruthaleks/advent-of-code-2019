#!/usr/bin/python3

import sys
from collections import defaultdict

def div( data, width, heigth ):
    layers = defaultdict()
    l = 0
    for i in range(0, len(data), width*heigth):
        layers[l] = data[i:i+width*heigth]
        l += 1
    return layers

def count_dig(l, dig):
    return len(tuple(filter(lambda x: x == dig, map(int,l))))
    
def pixel_data(L, n):
    d = []
    for i in L:
        d.append(int(L[i][n]))
    return tuple(d)


def top_visable_pixel(data):
    for i in data:
        if i != 2:
            return i
    


def main():
    w = 25 
    h = 6 

    data = tuple(sys.stdin.readline().strip())
    #print(data)
    
    L = div(data, w, h)
    
    number_of_zeros = []
    for i in L:
        number_of_zeros.append(count_dig(L[i], 0))
    
    v = min(number_of_zeros)
    layer = number_of_zeros.index(v)

    res1 = count_dig(L[layer], 1) * count_dig(L[layer], 2)
    print(f"Part 1: {res1}")
        
    print("Part 2:") 
    res = []
    for i in range(w*h):
        if top_visable_pixel(pixel_data(L, i)) == 1:
            print('*', end="")
        else:
            print(' ', end="")
        if (i+1) % w == 0:
            print()
    
    


    
    


main()
