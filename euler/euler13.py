'''
Large sum

Problem 13Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
....... euler.txt ...'''

with open('euler13nums.txt', 'r') as f:
    list_f = [line.rstrip('\n') for line in f]
    list_int = [int(i) for i in list_f]
    sum_list = (str(sum(list_int)))
    print(sum_list[:10])
