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
