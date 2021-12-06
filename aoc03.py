#!/usr/bin/env python3
# coding: utf-8

import numpy as np

myexample = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''


def read_file(myfilename):
    with open(myfilename) as myfile:
        return myfile.read()


def calculate_power_consumption(mystring):
    mylist = mystring.split()
    myarray = np.array([list(s) for s in mylist], dtype=np.int)
    freq = myarray.sum(axis=0)
    h = myarray.shape[0] // 2
    gamma = ''.join(['1' if x > h else '0' for x in freq])
    epsil = ''.join(['0' if x > h else '1' for x in freq])
    g = int(gamma, 2)
    e = int(epsil, 2)
    print('gamma rate:', gamma)
    print('epsilon rate:', epsil)
    print('power consumption:', g * e)


def calculate_life_support_rating(mystring):
    mylist = mystring.split()
    myarray = np.array([list(s) for s in mylist], dtype=np.int)
    oxyrate = filter_oxy_rating(myarray)
    co2rate = filter_co2_rating(myarray)
    o = int(oxyrate, 2)
    c = int(co2rate, 2)
    print('oxy rate:', oxyrate)
    print('co2 rate:', co2rate)
    print('life support rating:', o * c)


def filter_oxy_rating(myarray):
    # filter out numbers until only last left
    # using most common digit or 1
    d = 0
    while myarray.shape[0] > 1:
        d = d % myarray.shape[1]
        c1 = myarray.sum(axis=0)[d]
        c0 = myarray.shape[0] - c1
        if c1 >= c0:
            myarray = filter_by_bit(myarray, d, 1)
        else:
            myarray = filter_by_bit(myarray, d, 0)
        d += 1
    return ''.join([str(x) for x in myarray[0]])


def filter_co2_rating(myarray):
    # filter out numbers until only last left
    # using least common digit or 0
    d = 0
    while myarray.shape[0] > 1:
        d = d % myarray.shape[1]
        c1 = myarray.sum(axis=0)[d]
        c0 = myarray.shape[0] - c1
        if c0 <= c1:
            myarray = filter_by_bit(myarray, d, 0)
        else:
            myarray = filter_by_bit(myarray, d, 1)
        d += 1
    return ''.join([str(x) for x in myarray[0]])


def filter_by_bit(myold, d, b):
    mynew = []
    for myline in myold:
        if myline[d] == b:
            mynew.append(myline)
    return np.array(mynew)


if __name__ == '__main__':
    s = read_file('input\\input03.txt')
    calculate_power_consumption(s)
    calculate_life_support_rating(s)
