#!/usr/bin/python3

import sys


def add(mem, inst_ptr):
    arg1_ptr, arg2_ptr = mem[inst_ptr + 1], mem[inst_ptr + 2]
    out_ptr = mem[inst_ptr + 3]
     
    mem[out_ptr] = mem[arg1_ptr] + mem[arg2_ptr] 
    return "ok", inst_ptr + 4

def multiply(mem, inst_ptr):
    arg1_ptr, arg2_ptr = mem[inst_ptr + 1], mem[inst_ptr + 2]
    out_ptr = mem[inst_ptr + 3]
     
    mem[out_ptr] = mem[arg1_ptr] * mem[arg2_ptr] 
    return "ok", inst_ptr + 4

def halt(mem, inst_ptr):
    return "halt", inst_ptr + 1

       
def int_computer(data):
    optcodes = { 1 : add, 2 : multiply, 99 : halt}
    
    inst_ptr = 0
    status = "ok"
    while(status == "ok"):
        optc = data[inst_ptr]
        if optc in optcodes.keys():
            status, inst_ptr = optcodes[optc](data, inst_ptr)
        else:
            return "Something went wrong!"
    return data[0]


def main():
    data = tuple(map(int,sys.stdin.readline().split(",")))
    
    print(f"Part 1: {int_computer(list(data))}")
    
    for noun in range(100):
        for verb in range(100):
            indata = list(data)
            indata[1] = noun
            indata[2] = verb
            if int_computer(indata) == 19690720:
                print(f"Part 2: {100*noun+verb}")

if __name__ == "__main__":                
    main()
