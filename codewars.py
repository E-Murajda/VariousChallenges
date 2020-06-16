


"""Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). 
Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present."""


def spin_words(sentence):
    new = []
    new_str = " "
    for i in sentence.split():
        if len(i) >= 5:
            i = i[::-1]
            new.append(i)
        else:
            new.append(i)
    return new_str.join(new)

    # one line
    # return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])


"""Highest and Lowest
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number."""


def high_and_low(numbers):
    x = numbers.split()
    x = [int(i) for i in x]
    new_str = " "
    max_min = [str(max(x)), str(min(x))]
    new_str.join(max_min)

    return new_str.join(max_min)


'''Two to One
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,
- each taken only once - coming from s1 or s2.'''


def longest(s1, s2):
    s1_l = list(s1)
    s2_l = list(s2)
    s_un = s1_l + s2_l
    s_set = sorted(set(s_un))
    new = ''.join(s_set)
    return new



'''Bit Counting
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. 
You can guarantee that input is non-negative.'''
def countBits(n):
    b = list(bin(n))
    count = b.count('1')
    return count
#one line
#return bin(n).count("1")
print((countBits(1234)))


'''Take a Ten Minute Walk'''
'''You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, 
so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones 
-- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). 
You always walk only a single block in a direction and you know it takes you one minute to traverse one city block, so create a function 
that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of 
course, return you to your starting point. Return false otherwise.'''

def is_valid_walk(walk):
    vertical = 0
    horizontal = 0
    
    
    if (len(walk) == 10):
        for i in walk:
            if i == 'n':
                vertical+=1
            if i == 's':
                vertical-=1
            if i == 'w':
                horizontal+=1
            if i == 'e':
                horizontal-=1
    else:
        return False
    return(vertical == 0 and horizontal == 0)


'''Shortest Word'''
'''Simple, given a string of words, return the length of the shortest word(s).'''

def find_short(s):
    s = s.split()
    new_l = [len(i) for i in s]
    return min(new_l)

print(find_short("bitcoin take over the world maybe who knows perhaps"))































