#!/usr/bin/env python3
# coding: utf-8


myexample = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''


def read_file(myfilename):
    with open(myfilename) as myfile:
        return myfile.read()


def find_unique_digit_count_numbers(mystring):
    '''Here we just count the appearence of
    the digits with unique length (1, 4, 7, 8)'''
    mydict = { 1: 0, 4: 0, 7: 0, 8: 0 }
    mylist = mystring.splitlines()
    mylist = [s.split() for s in mylist]
    for myline in mylist:
        for s in myline[-4:]:
            if len(s) == 2: mydict[1] += 1
            elif len(s) == 3: mydict[7] += 1
            elif len(s) == 4: mydict[4] += 1
            elif len(s) == 7: mydict[8] += 1
    mytotal = 0
    print('these digits appear:')
    for (key, value) in mydict.items():
        print(key, value)
        mytotal += value
    print('sum:', mytotal)


def decipher_numbers(mystring):
    '''Find the exit numbers in the output part
    - analyze all combinations in the control part
    - get rid of permutations by sorting'''
    mylist = mystring.splitlines()
    mylist = [s.split() for s in mylist]
    mylist = [[''.join(sorted(s)) for s in myline] for myline in mylist]
    print('')
    mytotal = 0
    for myline in mylist:
        mytotal += decipher_line(myline)
    print('sum:', mytotal)

def decipher_line(mylist):
    '''Use a pattern list with 10 entries.
    First find the obvious patterns and
    collect sets of the muliple options.
    Solve the puzzle by testing which already
    known pattern fits into the unknowns.
    In the end decipher the output part.'''
    p = ['' for i in range(10)]
    p[1] = get_digit_single(mylist, 2)
    p[4] = get_digit_single(mylist, 4)
    p[7] = get_digit_single(mylist, 3)
    p[8] = get_digit_single(mylist, 7)    
    set235 = get_digit_multi(mylist, 5)
    set069 = get_digit_multi(mylist, 6)

    for s in set235:
        if check_all_in(list(p[1]), s):
            p[3] = s
        elif check_all_in(get_diff(p[4], p[1]), s):
            p[5] = s
        else:
            p[2] = s
    for s in set069:
        if check_all_in(list(p[3]), s):
            p[9] = s
        elif check_all_in(list(p[1]), s):
            p[0] = s
        else:
            p[6] = s
    
    myresult = ''
    for x in mylist[-4:]:
        for i in range(10):
            if x == p[i]:
                myresult += str(i)
    print(int(myresult))
    return int(myresult)


def get_digit_single(mylist, n):
    for s in mylist:
        if len(s) == n:
            return s

def get_digit_multi(mylist, n):
    myset = set()
    for s in mylist:
        if len(s) == n:
            myset.add(s)
    return myset

def check_all_in(charlist, mystring):
    for a in charlist:
        if a not in mystring:
            return False
    return True

def get_diff(str1, str2):
    newlist = []
    for a in str1:
        if a not in str2:
            newlist.append(a)
    return newlist


if __name__ == '__main__':
    myinput = read_file('input/input08.txt')
    find_unique_digit_count_numbers(myinput)
    decipher_numbers(myinput)
    
