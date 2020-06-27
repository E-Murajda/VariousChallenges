'''2D Array - DS'''


def hourglassSum(arr):

    sub = []

    for a in range(4):
        for i in range(4):
            sub.append(arr[a][i]+arr[a][i+1]+arr[a][i+2]+arr[a+1]
                       [i+1]+arr[a+2][i]+arr[a+2][i+1]+arr[a+2][i+2])

    return max(sub)


'''Arrays: Left Rotation'''


def rotLeft(a, d):
    return a[d:]+a[:d]


'''New Year Chaos'''


def minimumBribes(q):

    counter = 0

    for pos, val in enumerate(q):
        if (val-1) - pos > 2:
            return('Too chaotic')

        else:
            for i in range(len(q)-1, 0, -1):
                for j in range(i):

                    if q[j] > q[j+1]:
                        temp = q[j]
                        q[j] = q[j+1]
                        q[j+1] = temp
                        counter += 1
    return(counter)


'''Minimum Swaps 2'''


def minimumSwaps(arr):
    counter = 0

    for i in range(0, len(arr) - 1):
        while arr[i] != i + 1:
            t = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = t
            counter += 1
    return counter


'''Array Manipulation'''


def arrayManipulation(n, queries):

    lst = [0]*n
    for i in queries:
        lst[i[0]-1] += i[2]
        if i[1] != len(lst):
            lst[i[1]] -= i[2]
    val = 0
    it = 0

    for j in lst:
        it += j
        if it > val:
            val = it
    return val
