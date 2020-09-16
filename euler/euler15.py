import math

'''Lattice paths

Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?'''

# https://math.stackexchange.com/questions/286437/arrangement-of-binary-bits


def path_count(grid):
    p = math.factorial(grid*2)/(math.factorial(grid)**2)
    return p


print(path_count(20))
