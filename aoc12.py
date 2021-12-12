#!/usr/bin/env python3
# coding: utf-8


myexample1 = '''
start-A
start-b
A-c
A-b
b-d
A-end
b-end
'''
myexample2 = '''
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
'''

def read_file(myfilename):
    with open(myfilename) as myfile:
        return myfile.read()


class CaveExplorer:
    def __init__(self, mystring):
        '''
        Generates possible paths trough cave network start->end.
        Input: String with cave connections.
        Output: Prints number of path found.
        Lower case (small) caves can be visited generally only once.
        But there's an exception, one small cave can be visited twice.
        '''
        self.conns = mystring.strip().split()
        self.conns = [myline.split('-') for myline in self.conns]
        self.pathset = set()
        self.smallcaves = self.generate_set_of_small_caves()
        self.count_paths()
    

    def count_paths(self):
        print(self.smallcaves)
        for c in self.smallcaves:
            print('counting with small cave twice allowed:', c)
            self.twicecave = c
            self.paths = [['start']]
            i = 1
            while i > 0:
                i = self.add_another_step()
            for p in self.paths:
                self.pathset.add('-'.join(p))
            print(len(self.pathset))
        print('total number of paths found:', len(self.pathset))


    def add_another_step(self):
        print('add step', len(self.paths))
        newlist = []
        i = 0
        for p in self.paths:
            if p[-1] == 'end':
                newlist.append(p)
                continue
            for c in self.conns:
                if c[0] == p[-1] and self.visit_allowed(p, c[1]):
                    newpath = p.copy()
                    newpath.append(c[1])
                    newlist.append(newpath)
                if c[1] == p[-1] and self.visit_allowed(p, c[0]):
                    newpath = p.copy()
                    newpath.append(c[0])
                    newlist.append(newpath)
            i += 1
        self.paths = newlist
        return i
    

    def visit_allowed(self, mypath, mycave):
        if mycave.isupper() or mycave not in mypath:
            return True
        if mycave == self.twicecave and mypath.count(mycave) == 1:
            return True
        return False


    def generate_set_of_small_caves(self):
        newset = set()
        for c in self.conns:
            for e in c:
                if e.islower() and e not in ('start', 'end'):
                    newset.add(e)
        return newset


#is the following code breaking python?
#- newlist.append(pathlist + [newelement])


if __name__ == '__main__':
    myinput = read_file('input/input12.txt')
    ce = CaveExplorer(myinput)
    
