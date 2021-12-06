#!/usr/bin/env python3
# coding: utf-8

myexample = '''199
200
208
210
200
207
240
269
260
263'''


def read_file(myfilename):
    with open(myfilename) as myfile:
        return myfile.read()

def make_list(mystring):
    return [int(x) for x in mystring.split()]

def generate_sliding_window_list(mylist):
    mynewlist = []
    for i in range(len(mylist) - 2):
        mynewlist.append(sum(mylist[i:i+3]))
    return mynewlist
    
def get_number_of_increasing_measurements(mylist):
    i = 0
    d = None
    for x in mylist:
        if d and x > d:
            i += 1
        d = x
    return i


if __name__ == '__main__':
    #mylist = make_list(myexample)
    mylist = make_list(read_file('input\\input01.txt'))
    mylist = generate_sliding_window_list(mylist)
    print(len(mylist))
    print(get_number_of_increasing_measurements(mylist))
