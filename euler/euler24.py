'''Lexicographic permutations
Submit

 Show HTML problem content
Problem 24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?'''

from itertools import permutations, islice


def perm():

    to_check = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    perms = (i for i in permutations(to_check))
    for i in islice(perms, 999999, 1000000):
        yield i


for v in perm():
    print(v)
