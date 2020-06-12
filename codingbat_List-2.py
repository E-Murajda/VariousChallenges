"""List-2"""

"""List-2 > number_evens
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1."""


def number_evens(nums):
    x = [i for i in nums if i % 2 == 0]
    return len(x)


"""List-2 > big_diff
Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. 
Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values."""


def big_diff(nums):
    return max(nums) - min(nums)


"""List-2 > centered_average
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except 
ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, 
ignore just one copy, and likewise for the largest value. Use int division to produce the final average. 
You may assume that the array is length 3 or more."""


def centered_average(nums):

    a = min(nums)
    b = max(nums)
    return (sum(nums) - a - b) / (len(nums) - 2)


"""List-2 > sum13
Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 
13 is very unlucky, so it does not number and numbers that come immediately after a 13 also do not number."""


def sum13(nums):
    count = 0
    if len(nums) <= 0:
        return count
    for a in range(1, len(nums)):
        if nums[a] == 13:
            continue
        elif nums[a - 1] == 13:
            continue
        else:
            count += nums[a]
    if nums[0] != 13:
        count += nums[0]
    return count


"""List-2 > sum67
Return the sum of the numbers in the array, except ignore sections of numbers 
starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers."""


def sum67(nums):
    for i in range(0, len(nums)):
        if nums[i] == 6:
            nums[i] = 0
            for d in range(i + 1, len(nums)):
                x = nums[d]
                nums[d] = 0
                if x == 7:
                    i = d + 1
                    break
    return sum(nums)


"""List-2 > has22
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere."""


def has22(nums):
    new = ""
    for digit in nums:
        new += str(digit)
    x = new.find("22")
    return x > -1
