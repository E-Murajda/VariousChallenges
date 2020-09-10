from random import randint, seed
import itertools
import math
import numpy as np

'''Multiples of 3 and 5

Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.'''


num = 1000


def multiples(num):
    all_div5and3 = []
    for i in range(1, num):
        if i % 3 == 0 or i % 5 == 0:
            all_div5and3.append(i)
    return sum(all_div5and3)


print(multiples(num))


'''Even Fibonacci numbers
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''


n = 100


def Fib(n):

    l2 = []

    p = pp = 1
    for i in range(n):
        if i == 0:
            l2.append(0)
        elif i <= 2:
            l2.append(1)
        else:
            n = p + pp
            pp, p = p, n
            l2.append(n)
            if n >= 4000000:
                break
    return(l2)


x = [i for i in Fib(n) if i % 2 == 0]


print(sum(x))


'''Largest prime factor

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

number = 600851475143


def prime_factor(number):
    pr_factors = []

    while number % 2 == 0:
        pr_factors.append(2)
        number //= 2
    div = 3

    while number != 1 and div <= number:
        if number % div == 0:
            pr_factors.append(div)
            number //= div
        else:
            div += 2
    for i in range(len(pr_factors)):
        print(pr_factors[i], end=' ')


prime_factor(number)


'''Largest palindrome product

Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''


def largest_palindrome():
    l = []
    for x in range(900, 1000):
        for y in range(900, 1000):
            z = x*y
            strz = str(z)
            if strz[::-1] == strz:
                l.append(strz)
                break

    print(l[-1])


largest_palindrome()


'''Smallest multiple
 
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''


# def sm_multiple():

#     l = [11, 13, 14, 16, 17, 18, 19, 20]
#     for num in range(2520, 999999999, 20):
#         if all(num % n == 0 for n in l):
#             return num
#     return None


# print(sm_multiple())

'''Sum square difference

Problem 6
The sum of the squares of the first ten natural numbers is, 1**2 + 2**2 + 3**2 ... + 10**2 = 385

The square of the sum of the first ten natural numbers is, (1 + 2 + 3 ... + 10) = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is - 3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''


def sq_diff():
    l = [i for i in range(1, 101)]
    sum_squares = sum(list(map(lambda x: x**2, l)))
    square_sum = sum(l) ** 2
    print(square_sum, '-', sum_squares, '=', square_sum - sum_squares)


sq_diff()


'''10001st prime

Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?'''

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/


def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


primes = gen_primes()
result = itertools.islice(primes, 10001, 10002)
print(list(result))


'''Special Pythagorean triplet

Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''

n = 1000


def sp_pyth_triplet(n):

    for i in range(1, int(n / 3) + 1):

        for j in range(i + 1,
                       int(n / 2) + 1):

            k = n - i - j
            if (i * i + j * j == k * k):
                print(i, ", ", j, ", ", k, sep="")
                print(i*j*k)
                return
    print("No Triplet")


sp_pyth_triplet(n)


'''Summation of primes

Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''


def sum_of_primes():

    prime_nums = gen_primes()
    sum_primes = 0
    for prime in prime_nums:

        if prime >= 2000000:
            break
        else:
            sum_primes += prime
    return (sum_primes)


print(sum_of_primes())


arr = np.array([[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
                [49, 49, 99, 40, 17, 81, 18, 57, 60, 87,
                 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
                [81, 49, 31, 73, 55, 79, 14, 29, 93, 71,
                 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
                [52, 70, 95, 23, 4, 60, 11, 42, 69, 24,
                 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
                [22, 31, 16, 71, 51, 67, 63, 89, 41, 92,
                 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
                [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33,
                 53, 78, 36, 84, 20, 35, 17, 12, 50],
                [32, 98, 81, 28, 64, 23, 67, 10, 26, 38,
                 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
                [67, 26, 20, 68, 2, 62, 12, 20, 95, 63,
                 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
                [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78,
                 78, 96, 83, 14, 88, 34, 89, 63, 72],
                [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35,
                 14, 0, 61, 33, 97, 34, 31, 33, 95],
                [78, 17, 53, 28, 22, 75, 31, 67, 15, 94,
                 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
                [16, 39, 5, 42, 96, 35, 31, 47, 55, 58,
                 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
                [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44,
                 37, 44, 60, 21, 58, 51, 54, 17, 58],
                [19, 80, 81, 68, 5, 94, 47, 69, 28, 73,
                 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
                [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57,
                 32, 16, 26, 26, 79, 33, 27, 98, 66],
                [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33,
                 67, 46, 55, 12, 32, 63, 93, 53, 69],
                [4, 42, 16, 73, 38, 25, 39, 11, 24, 94,
                 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
                [20, 69, 36, 41, 72, 30, 23, 88, 34, 62,
                 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
                [20, 73, 35, 29, 78, 31, 90, 1, 74, 31,
                 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
                [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]])


def find_largest(arr):

    largest = 0

    count = 0
    row = 0
    col = 0

    first = 0
    last = 4
    # Check rows
    for a in range(len(arr)):

        for i in range((len(arr[row]))-3):

            count = np.prod(arr[row, first:last])
            first += 1
            last += 1
            if count > largest:
                largest = count

        first = 0
        last = 4
        row += 1

    # Check columns
    for b in range(len(arr)):

        for j in range((len(arr[col]))-3):

            count = np.prod(arr[first:last, col])
            first += 1
            last += 1
            if count > largest:
                largest = count

        first = 0
        last = 4
        col += 1

    row = 0
    col = 0

    # Check diagonal L to R
    for c in range(17):
        for k in range(17):
            diag1 = (arr[row, first], arr[row+1, first+1],
                     arr[row+2, first+2], arr[row+3, first+3])
            count = np.prod(diag1)

            first += 1
            if count > largest:
                largest = count
        first = 0
        row += 1

    row = 0
    # Check diagonal R to L
    for d in range(17):
        for l in range(17):
            diag2 = (arr[row, first+3], arr[row+1, first+2],
                     arr[row+2, first+1], arr[row+3, first])
            count = np.prod(diag2)

            first += 1
            if count > largest:
                largest = count
        first = 0
        row += 1
    print(largest)


find_largest(arr)


'''Highly divisible triangular number
 
Problem 12
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?'''


def triangle_numbers(num):
    return sum([i for i in range(1, num + 1)])


j = 0
num = 0
num_of_divisors = 0

while num_of_divisors <= 500:
    num_of_divisors = 0
    j += 1
    num = triangle_numbers(j)

    i = 1
    while i <= num**0.5:
        if num % i == 0:
            num_of_divisors += 1
        i += 1
    num_of_divisors *= 2

print(num)

'''Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
....... euler.txt ...'''

with open('euler.txt', 'r') as f:
    list_f = [line.rstrip('\n') for line in f]
    list_int = [int(i) for i in list_f]
    sum_list = (str(sum(list_int)))
    print(sum_list[:10])


'''Longest Collatz sequence

Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


def collatz():
    l1 = [0]
    longest = 1
    start = 1
    for i in range(1, 1000000):
        cnt = 1
        n = i
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3*n + 1
            try:
                cnt += l1[n]
                break
            except:
                cnt += 1
        l1.append(cnt)
        if cnt > longest:
            longest = cnt
            start = i
    return start


print(collatz())

'''Lattice paths

Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?'''

# https://math.stackexchange.com/questions/286437/arrangement-of-binary-bits


def path_count(grid):
    p = math.factorial(grid*2)/(math.factorial(grid)**2)
    return p


print(path_count(20))


'''Power digit sum

Problem 16
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?'''

print(sum([int(x) for x in str(2**1000)]))


'''Number letter counts
Submit

 Show HTML problem content
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.'''


dict_ones = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
    8: 'eight', 9: 'nine'}

dict_teens = {
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
    14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
    18: 'eighteen', 19: 'nineteen'}

dict_tens = {
    20: 'twenty', 30: 'thirty', 40: 'forty',
    50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}


def number_letter_count(num):

    l = [int(i) for i in str(num)]

    if len(l) == 1:
        return dict_ones.get(num)
    if num == 1000:
        return 'onethousand'

    str_num = str(num)
    l2 = int(str_num[1:])

    hundreds = dict_ones.get(l[0])
    teens = dict_teens.get(l2)
    tens = dict_tens.get(l2 - l[-1])
    ones = dict_ones.get(l[-1])

    if len(l) == 3:

        if 20 > l2 > 9:
            return (hundreds + 'hundredand' + teens)
        if l2 >= 20:
            if l[2] == 0:
                return (hundreds + 'hundredand' + tens)
            return (hundreds + 'hundredand' + tens + ones)
        if l[1:] == [0, 0]:
            return (hundreds + 'hundred')
        if l[1] == 0 and l[2] != 0:
            return (hundreds + 'hundredand' + ones)

    if len(l) == 2 and num >= 20:

        if l[1] == 0:
            return (dict_tens.get(num))
        if l[1] != 0:
            rnd = num - l2
            return dict_tens.get(rnd) + ones
    if len(l) == 2 and 9 < num < 20:
        return dict_teens.get(num)


x = [number_letter_count(i) for i in range(1, 1001)]
print(len(''.join(x)))


'''Maximum path sum I

Problem 18
By starting at the top of the triangle below and moving to adjacent 
numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:



NOTE: As there are only 16384 routes, it is possible to solve this problem 
by trying every route. However, Problem 67, is the same challenge with a 
triangle containing one-hundred rows; it cannot be solved by brute force, 
and requires a clever method! ;o)'''


triangle = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''


def max_path(triangle):

    numbers = triangle.strip().split('\n')
    for i in range(1, len(numbers)):
        numbers[i] = numbers[i].strip().split(' ')
        numbers[i] = [int(x) for x in numbers[i]]
    numbers[0] = [75]

    for x in range(len(numbers) - 2, -1, -1):
        for y in range(len(numbers[x])):
            numbers[x][y] = numbers[x][y] + \
                max(numbers[x+1][y], numbers[x+1][y+1])

    return (max(numbers))


print(max_path(triangle))
