#!/usr/bin/env python3
# coding: utf-8


myexample = '''3,4,3,1,2'''


def read_file(myfilename):
    with open(myfilename) as myfile:
        return myfile.read()


def calculate_lanternfish_history(n):
    '''calculates all decendents of one fish
    with a list of how many are in which stage
    of their reproductive cycle
    saving the sum for every day in a history'''
    mypopulation = [1, 0, 0, 0, 0, 0, 0, 0, 0]
    myhistory = [1]
    print('0 days', mypopulation, '1')
    for i in range(1, n+1):
        mycreators = mypopulation.pop(0)
        mypopulation[6] += mycreators
        mypopulation += [mycreators]
        mysum = sum(mypopulation)
        myhistory.append(mysum)
        print(i, 'days', mypopulation, mysum)
    return myhistory


def calculate_lanternfish_count(myhistory, mystring):
    '''count the number of fish per stage
    multiplying this with the history entry'''
    mylist = [int(x) for x in mystring.split(',')]
    myfreq = [mylist.count(i) for i in range(9)]
    mytotal = 0
    for i in range(9):
        mytotal += myfreq[i] * myhistory[-1-i]
    print('initial fish count:')
    print(myfreq, len(mylist), sum(myfreq))
    print('fish count after', len(myhistory)-1, 'days:')
    print(mytotal)


if __name__ == '__main__':
    myinput = read_file('input\\input06.txt')
    myhistory = calculate_lanternfish_history(256)
    calculate_lanternfish_count(myhistory, myinput)
    
