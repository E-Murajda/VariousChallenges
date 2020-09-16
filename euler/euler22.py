'''Names scores

Problem 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?'''


with open('euler22names.txt', 'r') as text:
    l = list(text.read().split(","))
    l2 = sorted([i.strip('"') for i in l])

    l_of_names = [list(i) for i in l2]
    total = 0

    for i in range(len(l2)):
        name = l_of_names[i]
        for j in range(len(name)):
            letter = name[j]
            letter = (ord(letter) - 64)
            l_of_names[i][j] = letter
        summed = (sum(l_of_names[i]) * (i+1))
        total += summed

    print(total)
