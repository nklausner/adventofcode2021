#!/usr/bin/env python3
# coding: utf-8

myexample = '''forward 5
down 5
forward 8
up 3
down 8
forward 2'''


def read_file(myfilename):
    with open(myfilename) as myfile:
        return myfile.read()

def sum_command_sequence(mystring):
    mylist = mystring.split()
    x = 0
    z = 0
    aim = 0
    for i in range(len(mylist)//2):
        c = mylist[2*i]
        d = int(mylist[2*i+1])
        if c == 'down':
            aim += d
        elif c == 'up':
            aim -= d
        elif c == 'forward':
            x += d
            z += aim * d
    return x, z



if __name__ == '__main__':
    s = read_file('input\\input02.txt')
    x, z = sum_command_sequence(s)
    print(x, z)
    print(x*z)
