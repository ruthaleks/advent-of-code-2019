#!/usr/bin/python3

import sys
from collections import defaultdict


def parse( data ):
   return tuple(data.strip().split(")"))

def count_orbits(root, orbit_map, end):
    rev = 0
    while(root != end):
        root = orbit_map[root]
        rev += 1
    return rev

def orbit_path(root, orbit_map):
    path = []
    while(root != 'COM'):
        path.append(root)
        root = orbit_map[root]
    return path



def main():
    raw_data = tuple(sys.stdin.readlines())
    
    orbit_map = defaultdict()
    for data in raw_data:
        (v, k) = parse(data)
        orbit_map[k] = v
    
    
    res1 = 0
    for orbit in orbit_map:
        res1 += count_orbits(orbit, orbit_map, 'COM')
    
    print(f"Part 1: {res1}")
    
    y_path = orbit_path("YOU", orbit_map)
    s_path = orbit_path("SAN", orbit_map)
   
    common_elements = [element for element in y_path if element in s_path]
    conn = common_elements[0]
    
    res2 = count_orbits(orbit_map['YOU'], orbit_map, conn) + count_orbits(orbit_map['SAN'], orbit_map, conn)

    print(f"Part 2: {res2}")
     

if __name__ == "__main__":
    main()

