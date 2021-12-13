#!/usr/bin/env python3
# coding: utf-8


myexample = '''
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
'''


def read_file(myfilename):
    with open(myfilename) as myfile:
        return myfile.read()


def read_folding_instructions(mystring):
    '''split the input string
    it contains coordinates and instructions
    i is delimiter index'''
    mylist = mystring.strip().splitlines()
    i = mylist.index('')

    '''fill a set with all the coordinates'''
    myset = set()
    for myline in mylist[:i]:
        [x, y] = myline.split(',')
        myset.add((int(x), int(y)))

    '''read and execute folding instructions
    for every step the set is overwritten'''
    for myinstruction in mylist[i+1:]:
        if 'x=' in myinstruction:
            xfold = int(myinstruction[13:])
            myset = fold_along_x(myset, xfold)
        elif 'y=' in myinstruction:
            yfold = int(myinstruction[13:])
            myset = fold_along_y(myset, yfold)
        else:
            print('cannot understand instruction')
        print(len(myset))
    
    '''print coordinates as pixels'''
    print_code(myset)


def fold_along_x(oldset, xfold):
    newset = set()
    for (x, y) in oldset:
        if x < xfold:
            newset.add((x, y))
        elif x > xfold:
            newset.add((2 * xfold - x, y))
        else:
            print('on x folding line')
    return newset


def fold_along_y(oldset, yfold):
    newset = set()
    for (x, y) in oldset:
        if y < yfold:
            newset.add((x, y))
        elif y > yfold:
            newset.add((x, 2 * yfold - y))
        else:
            print('on y folding line')
    return newset


def print_code(myset):
    '''just use hardcoded 6x40 width and heigth'''
    linelist = [[' ' for j in range(40)] for i in range(6)]
    for (x, y) in myset:
        linelist[y][x] = '#'
    for line in linelist:
        print(''.join(line))



if __name__ == '__main__':
    myinput = read_file('input/input13.txt')
    read_folding_instructions(myinput)
