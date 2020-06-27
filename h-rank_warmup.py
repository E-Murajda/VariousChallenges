'''Sock merchant'''

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    new = sorted(ar)
    new.append('x')

    count = 0
    i = 0
    while i < n:
        if new[i] == new[i+1]:
            count += 1
            i += 2
        else:
            i += 1
    return count


'''Counting Valleys'''


def countingValleys(n, s):

    level = valley = 0
    for i in range(n):
        if(s[i] == 'U'):
            level += 1
            if(level == 0):
                valley += 1
        else:
            level -= 1

    return valley


'''Jumping on the clouds'''


def jumpingOnClouds(c):
    jump = 0
    num = 0
    while num < len(c):
        if num+2 < len(c) and c[num+2] == 0:
            jump += 1
            num += 2
        elif num+1 < len(c) and c[num+1] == 0:
            jump += 1
            num += 1
        else:
            num += 1
    return jump


'''Repeated String'''


def repeatedString(s, n):

    count = s.count('a')
    repititions = n // len(s)

    count = count * repititions

    l = n % len(s)
    for i in range(l):
        if (s[i] == 'a'):
            count += 1
    return count
