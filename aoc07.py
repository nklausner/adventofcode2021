#!/usr/bin/env python3
# coding: utf-8


myexample = '''16,1,2,0,4,2,7,1,2,14'''


def read_file(myfilename):
    with open(myfilename) as myfile:
        return myfile.read()


def calcuate_optimal_crab_fuel(mystring):
    mylist = [int(x) for x in mystring.split(',')]
    mytest = [x for x in range(min(mylist), max(mylist))]
    fuel_const = [0 for x in mytest]
    fuel_incre = [0 for x in mytest]
    for i in range(len(mytest)):
        for x in mylist:
            d = abs(mytest[i] - x)
            fuel_const[i] += d
            fuel_incre[i] += d * (d + 1) // 2
    print('minimum fuel for the crabs to line up:')
    print('constant', min(fuel_const))
    print('increasing', min(fuel_incre))


if __name__ == '__main__':
    myinput = read_file('input/input07.txt')
    calcuate_optimal_crab_fuel(myinput)
    
