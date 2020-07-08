from collections import Counter, defaultdict


'''Strings: Making Anagrams'''


def makeAnagram(a, b):

    a = Counter(a)
    b = Counter(b)
    return sum(((a | b) - (a & b)).values())


'''Alternating Characters'''


def alternatingCharacters(s):
    count = 0
    lst = [i for i in s]
    for i in range(len(lst)-1):
        if lst[i] != lst[i+1]:
            continue
        else:
            count += 1

    return count


'''Sherlock and the Valid String'''


def isValid(s):
    c = Counter(s)
    count = 0
    l = []
    for v in c.values():
        l.append(v)
    for i in range(len(l) - 1):
        if l[0] == l[i+1]:
            continue
        else:
            count += 1
    return ('YES' if count <= 1 else 'NO')


'''Special String Again'''


def substrCount(n, s):
    answer = 0
    same_char = [0]*n
    i = 0
    while (i < n):
        same_char_count = 1
        j = i+1
        while(j < n):
            if(s[i] != s[j]):
                break
            same_char_count += 1
            j += 1
        answer += int(same_char_count*(same_char_count+1)/2)
        same_char[i] = same_char_count
        i = j
    for j in range(1, n):
        if (s[j] == s[j-1]):
            same_char[j] = same_char[j-1]
        if (j > 0 and j < (n-1) and (s[j-1] == s[j+1] and s[j] != s[j-1])):
            answer += (same_char[j-1] if (same_char[j-1] <
                                          same_char[j+1]) else same_char[j+1])
    return answer


'''Common Child'''

# switch to Pypy3 to pass all cases.


def commonChild(s1, s2):

    z = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    for i, a in enumerate(s1):
        for j, b in enumerate(s2):
            if a == b:
                z[i+1][j+1] = z[i][j] + 1
            else:
                z[i+1][j+1] = \
                    max(z[i+1][j], z[i][j+1])
    return z[-1][-1]
