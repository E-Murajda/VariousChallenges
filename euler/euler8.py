from numpy import product as pr

'''Largest product in a series

Problem 8
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
9698...

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?'''

with open('euler8nums.txt', 'r') as n:

    l = []
    for _ in n:
        z = _.rstrip('\n')
        l.append(z)
    nums = ''.join(l)
    new_l = [int(i) for i in list(nums)]

    largest = 0
    first = 0
    last = 13
    for i in range(len(new_l)):
        checked = pr(new_l[first:last])
        if checked > largest:
            largest = checked
        first += 1
        last += 1
    print(largest)
