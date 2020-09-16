import numpy
import os
import sys


def fizzBuzz(n):
    l = [each for each in range(1, n + 1)]
    for i in l:
        if i % 3 == 0:
            if i % 5 == 0:
                print("FizzBuzz")
            if i % 5 != 0:
                print("Fizz")
        if i % 5 == 0 and i % 3 != 0:
            print("Buzz")
        if i % 5 != 0 and i % 3 != 0:
            print(i)


# if __name__ == "__main__":
#     n = int(input().strip())

#     fizzBuzz(n)

# fizzBuzz(15)


"""Stay positive"""
# a = int(input("enter len"))
# arr = []
# while a:
#     b = int(input("enter b"))
#     arr.append(b)
#     a -= 1
# a = sys.stdin.read("input000.txt").split()
# print(a)
with open("input002.txt", "r") as file:
    input_lines = [line.strip() for line in file]
print(input_lines)
arr = input_lines[1:]
arr = [int(i) for i in arr]
print(arr)


def minStart(arr):

    x = 1
    arr.insert(0, x)
    run_sum = list(numpy.cumsum(arr))
    all_positive = all(n > 0 for n in run_sum)
    while not all_positive:
        x += 1
        del arr[0]
        arr.insert(0, x)
        run_sum = list(numpy.cumsum(arr))
        all_positive = all(n > 0 for n in run_sum)
    return x


print(minStart(arr))


# if __name__ == "__main__":
#     fptr = open(os.environ[input000.txt], "w")

#     arr_count = int(input().strip())

#     arr = []

#     for _ in range(arr_count):
#         arr_item = int(input().strip())
#         arr.append(arr_item)

#     result = minStart(arr)

#     fptr.write(str(result) + "\n")

#     fptr.close()
