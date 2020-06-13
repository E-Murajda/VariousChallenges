"""Logic-2"""

"""Logic-2 > make_bricks
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch 
each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the 
given bricks. This is a little harder than it looks and can be done without any loops"""


def make_bricks(small, big, goal):

    return (goal % 5) <= small and (goal - (big * 5)) <= small


"""Logic-2 > lone_sum
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum."""


def lone_sum(a, b, c):
    if a == b == c:
        return 0
    if a == b:
        return c
    if b == c:
        return a
    if a == c:
        return b
    else:
        return a + b + c


print(lone_sum(1, 2, 3))
print(lone_sum(3, 2, 3))
print(lone_sum(3, 3, 3))


"""Logic-2 > lucky_sum
Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards 
the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count."""


def lucky_sum(a, b, c):
    l = [a, b, c]
    if 13 in l:
        num = l.index(13)
        new = sum(l[:num])
        return new
    else:
        return sum(l)


"""Logic-2 > no_teen_sum
Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 
inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper 
"def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you 
avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent 
level as the main no_teen_sum()."""


def no_teen_sum(a, b, c):
    nums = (a, b, c)
    return sum(fix_teen(n) for n in nums)


def fix_teen(n):
    if n not in (15, 16) and 13 <= n <= 19:
        return 0
    else:
        return n


"""Logic-2 > round_sum
For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, 
so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 
, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, 
rite a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same 
indent level as round_sum()."""


def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


def round10(num):
    mod = num % 10
    if mod < 5:
        num = int(num / 10) * 10
        return num
    else:
        num = int((num + 10) / 10) * 10
        return num


"""Logic-2 > close_far
Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other 
is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number."""


def close_far(a, b, c):

    diff1 = abs(a - b) <= 1 and abs(b - c) >= 2 and abs(a - c) >= 2
    diff2 = abs(a - c) <= 1 and abs(a - b) >= 2 and abs(c - b) >= 2
    return diff1 or diff2


"""Logic-2 > make_chocolate
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't 
be done."""


def make_chocolate(small, big, goal):
    if (small + big * 5 < goal) or (goal % 5 > small):
        return -1
    elif 5 <= goal:
        count = 0
        for i in range(1, big + 1):
            if 5 * i + small >= goal:
                if 5 * i > goal:
                    break
                count = goal - 5 * i
        return count
    elif small >= goal:
        return small
