'''Number letter counts
Submit

 Show HTML problem content
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.'''


dict_ones = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
    8: 'eight', 9: 'nine'}

dict_teens = {
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
    14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
    18: 'eighteen', 19: 'nineteen'}

dict_tens = {
    20: 'twenty', 30: 'thirty', 40: 'forty',
    50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}


def number_letter_count(num):

    l = [int(i) for i in str(num)]

    if len(l) == 1:
        return dict_ones.get(num)
    if num == 1000:
        return 'onethousand'

    str_num = str(num)
    l2 = int(str_num[1:])

    hundreds = dict_ones.get(l[0])
    teens = dict_teens.get(l2)
    tens = dict_tens.get(l2 - l[-1])
    ones = dict_ones.get(l[-1])

    if len(l) == 3:

        if 20 > l2 > 9:
            return (hundreds + 'hundredand' + teens)
        if l2 >= 20:
            if l[2] == 0:
                return (hundreds + 'hundredand' + tens)
            return (hundreds + 'hundredand' + tens + ones)
        if l[1:] == [0, 0]:
            return (hundreds + 'hundred')
        if l[1] == 0 and l[2] != 0:
            return (hundreds + 'hundredand' + ones)

    if len(l) == 2 and num >= 20:

        if l[1] == 0:
            return (dict_tens.get(num))
        if l[1] != 0:
            rnd = num - l2
            return dict_tens.get(rnd) + ones
    if len(l) == 2 and 9 < num < 20:
        return dict_teens.get(num)


x = [number_letter_count(i) for i in range(1, 1001)]
print(len(''.join(x)))
