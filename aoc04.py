#!/usr/bin/env python3
# coding: utf-8

import numpy as np

myexample = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''


def read_file(myfilename):
    with open(myfilename) as myfile:
        return myfile.read()


def split_input(mystring):
    '''splitting input string in number list and board array
    caution: exclude the last line with empty string'''
    mylist = mystring.split('\n\n')
    mynumbers = np.array(mylist[0].split(','), dtype=np.int)
    myboards = [b.split('\n') for b in mylist[1:-1]]
    myboards = [[myline.split() for myline in b] for b in myboards]
    myboards = np.array(myboards, dtype=np.int)
    print(mynumbers.shape, myboards.shape)
    return mynumbers, myboards


def calculate_winning_score(numbers, boards):
    '''steps:
    - looping over drawn bingo numbers
    - looping over every puzzle
    - replacing matches with -1 
    - checking for row or columns sums of -5 (all drawn)
    - if found replacing -1 by 0
    - and calculating the sum of remaining numbers'''
    for n in numbers:
        for b in boards:
            b[b == n] = -1
            rows = b.sum(axis=1)
            cols = b.sum(axis=0)
            if -5 in rows or -5 in cols:
                b[b == -1] = 0
                print('winning:', n, b.sum(), n*b.sum())
                return


def calculate_loosing_score(numbers, puzzles):
    '''steps:
    - see calculate winning score
    - set winning boads fully to -1
    - keep track of how many boards are left
    - calculate the sum for the last boards when winning
    '''
    last = 0
    curr = 0
    for n in numbers:
        last = curr
        curr = 0
        for b in boards:
            if b.sum() > -25:
                b[b == n] = -1
                rows = b.sum(axis=1)
                cols = b.sum(axis=0)
                if -5 in rows or -5 in cols:
                    if last > 1:
                        b[b >= 0] = -1
                    else:
                        b[b == -1] = 0
                        print('loosing:', n, b.sum(), n*b.sum())
                else:
                    curr += 1
        #print(n, curr)
    


if __name__ == '__main__':
    s = read_file('input/input04.txt')
    numbers, boards = split_input(s)
    calculate_winning_score(numbers, boards)
    calculate_loosing_score(numbers, boards)
    
