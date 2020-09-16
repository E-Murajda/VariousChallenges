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
