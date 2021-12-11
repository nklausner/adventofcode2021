#!/usr/bin/env python3
# coding: utf-8


myexample = '''
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''

def read_file(myfilename):
    with open(myfilename) as myfile:
        return myfile.read()


class OctopusGrid:
    def __init__(self, mystring):
        '''
        There are luminescent octopuses in a grid with level (0-9).
        Every step the count increases by 1.
        When the count for one reaches 10 it flashes and jumps to 0.
        The flashing also increases the count of the 8 adjacent octopuses.
        Special indicators:
        - 10: this one will flash, still need to affect adjacent neighbors
        - 11: this one will flash
        So eventually the all become syncronized and flash at one.
        This class counts the total flashes and stops when synchronized.
        '''
        self.grid = [list(s) for s in mystring.strip().split()]
        self.grid = [[int(x) for x in myline] for myline in self.grid]
        self.ymax = len(self.grid)
        self.xmax = len(self.grid[0])
        self.flash_count = 0

        for i in range(1000):
            self.increase_by_one(0, 0, self.xmax, self.ymax)
            while self.in_grid(10):
                self.affect_adjacent_ones()
            c = self.get_all_flashes()
            self.flash_count += c
            if c == self.xmax * self.ymax:
                print('first all flashing step:', i+1)
                print('')
                break
        
        self.print_grid()


    def increase_by_one(self, x0, y0, x1, y1):
        x0 = x0 if x0 >= 0 else 0
        y0 = y0 if y0 >= 0 else 0
        x1 = x1 if x1 <= self.xmax else self.xmax
        y1 = y1 if y1 <= self.ymax else self.ymax
        for y in range(y0, y1):
            for x in range(x0, x1):
                if self.grid[y][x] < 10:
                    self.grid[y][x] += 1
    

    def affect_adjacent_ones(self):
        for y in range(self.ymax):
            for x in range(self.xmax):
                if self.grid[y][x] == 10:
                    self.grid[y][x] = 11
                    self.increase_by_one(x -1, y - 1, x + 2, y + 2)


    def in_grid(self, x):
        for myline in self.grid:
            for myentr in myline:
                if myentr == x:
                    return True
        return False
    

    def get_all_flashes(self):
        c = 0
        for y in range(self.ymax):
            for x in range(self.xmax):
                if self.grid[y][x] == 11:
                    self.grid[y][x] = 0
                    c += 1
        return c


    def print_grid(self):
        for myline in self.grid:
            print(''.join([str(x) for x in myline]))
        print('total flash count', self.flash_count)


if __name__ == '__main__':
    myinput = read_file('input/input11.txt')
    og = OctopusGrid(myinput)
    
