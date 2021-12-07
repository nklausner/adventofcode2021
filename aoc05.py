#!/usr/bin/env python3
# coding: utf-8

import numpy as np

myexample = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''


def read_file(myfilename):
    with open(myfilename) as myfile:
        return myfile.read()


def read_vent_line_coords(mystring):
    mylist = []
    mysplit = mystring.split()
    for i in range(len(mysplit) // 3):
        myline = []
        myline += mysplit[i*3].split(',')
        myline += mysplit[i*3+2].split(',')
        myline = [int(x) for x in myline]
        mylist.append(myline)
    return mylist


def fill_vent_map():
    dc = 0
    for (x0, y0, x1, y1) in mylist:
        n = abs(x1 - x0)
        m = abs(y1 - y0)
        if n == m:
            dc += 1
        if n == 0:
            n = m
        if n == 0:
            continue
        dx = (x1 - x0) // n
        dy = (y1 - y0) // n
        for i in range(n+1):
            mymap[y0 + i*dy, x0 + i*dx] += 1
    print('diagonals:', dc)
    #print(mymap)


def count_dangerous_spots():
    mymap[mymap == 1] = 0
    mymap[mymap > 1] = 1
    print(mymap.sum())


if __name__ == '__main__':
    myinput = read_file('input/input05.txt')
    mylist = read_vent_line_coords(myinput)
    mymap = np.zeros((1000, 1000), dtype=int)
    fill_vent_map()
    count_dangerous_spots()
    
