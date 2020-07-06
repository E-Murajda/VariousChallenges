from collections import defaultdict
from collections import Counter


'''Hash Tables: Ransom Note'''


def ransom_note(magazine, note):
    word_counts = Counter(magazine)
    for word in note:
        if word_counts[word] > 0:
            word_counts[word] -= 1
        else:
            return 'No'
    return 'Yes'


'''Two Strings'''
s1 = 'hello'
s2 = 'world'


def twoStrings(s1, s2):

    s1d = set(s1)
    s2d = set(s2)

    if set.intersection(s1d, s2d):
        return 'YES'
    return 'NO'


'''Sherlock and Anagrams'''


def sherlockAndAnagrams(s):

    res = 0
    n = len(s)
    for i in range(1, n):
        d = {}
        for j in range(n-i+1):
            sub = ''.join(sorted(s[j:j+i]))
            if sub not in d:
                d[sub] = 1
            else:
                d[sub] += 1
            res += d[sub] - 1
    return res


'''Count Triplets'''


def countTriplets(arr, r):

    a = Counter()
    b = Counter()
    count = 0

    for i in arr:
        if i in b:
            count += b[i]

        if i in a:
            b[i*r] += a[i]

        a[i*r] += 1

    return count


'''Frequency Queries'''


def freqQuery(queries):

    new = defaultdict(int)
    freq = defaultdict(int)
    answer = []

    for q in queries:
        num, val = q

        if num == 1:
            freq[new[val]] = max(0, freq[new[val]]-1)
            new[val] += 1
            freq[new[val]] += 1
        elif num == 2:
            freq[new[val]] = max(0, freq[new[val]]-1)
            new[val] = max(0, new[val] - 1)
            freq[new[val]] += 1
        elif num == 3:
            if freq[val] > 0:
                answer.append(1)
            else:
                answer.append(0)

    return answer
