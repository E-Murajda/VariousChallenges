from datetime import datetime
import numpy as np

start_time = datetime.now()


def collatz(n):

    l1 = []
    l2 = []
    a = 0
    for number in range(2, n+1):
        i = number
        while i > 1:
            if i % 2 == 0:
                i = i//2
            else:
                i = i*3+1
            l1.append(i)
            try:
                if l2[0] == l1[-1]:
                    l2 = l2+l1
                    break
            except IndexError:
                pass
        if len(l1) > len(l2):
            l2 = l1
            l1 = []
            a = number
            print(l2, number)

        else:
            l1 = []
    return a


print(collatz(1000000))


end_time = datetime.now()
print("Duration: {}".format(end_time - start_time))
