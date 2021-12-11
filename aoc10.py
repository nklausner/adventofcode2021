#!/usr/bin/env python3
# coding: utf-8


myexample = '''
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''

opening_chars = ['(', '[', '{', '<']
closing_chars = [')', ']', '}', '>']
error_scores = [3, 57, 1197, 25137]


def read_file(myfilename):
    with open(myfilename) as myfile:
        return myfile.read()


def evaluate_lines(mystring):
    '''Evaluate the corrupted command list.
    Calculate syntax error score for corrupted lines.
    Calculate the completion scores for other lines.
    Find the median of these.
    Assume completion string are longer than 1.'''
    es = 0
    closing_scores = []
    for myline in mystring.strip().split():
        mylist = find_line_errors_or_completion(myline)
        if(len(mylist) == 1):
            i = closing_chars.index(mylist[0])
            es += error_scores[i]
            print('found corrupted line with:', mylist[0])
        else:
            cs_line = 0
            for char in mylist:
                cs_line = cs_line * 5
                cs_line += closing_chars.index(char) + 1
            closing_scores.append(cs_line)
            print('found incomplete line', cs_line)
    print('')
    print('total sytax error score:', es)
    cs = sorted(closing_scores)[len(closing_scores) // 2]
    print('median completion score:', cs)


def find_line_errors_or_completion(myline):
    '''Find corruption in chunk closing:
    - yes: Return correpted char
    - no: Returns the sequence of missing closing chars.'''
    closing_list = []
    for char in list(myline):
        if char in opening_chars:
            i = opening_chars.index(char)
            closing_list.append(closing_chars[i])
        elif char in closing_chars:
            if char == closing_list[-1]:
                 del closing_list[-1]
            else:
                return [char]
        else:
            print('found illegal char:', char)
    closing_list.reverse()
    return closing_list


if __name__ == '__main__':
    myinput = read_file('input/input10.txt')
    evaluate_lines(myinput)
    
