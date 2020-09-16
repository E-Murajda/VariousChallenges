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
