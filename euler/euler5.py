'''Smallest multiple
 
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''


def sm_multiple():

    l = [11, 13, 14, 16, 17, 18, 19, 20]
    for num in range(2520, 999999999, 20):
        if all(num % n == 0 for n in l):
            return num
    return None


print(sm_multiple())
