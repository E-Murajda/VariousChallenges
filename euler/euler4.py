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
