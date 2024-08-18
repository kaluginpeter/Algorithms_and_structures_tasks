# A number is Esthetic if, in any base from base2 up to base10, the absolute difference between every pair of its adjacent digits is constantly equal to 1.
#
# num = 441 (base10)
# // Adjacent pairs of digits:
# // |4, 4|, |4, 1|
# // The absolute difference is not constant
# // 441 is not Esthetic in base10
#
# 441 in base4 = 12321
# // Adjacent pairs of digits:
# // |1, 2|, |2, 3|, |3, 2|, |2, 1|
# // The absolute difference is constant and is equal to 1
# // 441 is Esthetic in base4
# Given a positive integer num, implement a function that returns an array containing the bases (as integers from 2 up to 10) in which num results to be Esthetic, or an empty array [] if no base makes num Esthetic.
#
# Examples
# 10 ➞ [2, 3, 8, 10]
# // 10 in base2 = 1010
# // 10 in base3 = 101
# // 10 in base8 = 12
# // 10 in base10 = 10
#
# 23 ➞ [3, 5, 7, 10]
# // 23 in base3 = 212
# // 23 in base5 = 43
# // 23 in base7 = 32
# // 23 in base10 = 23
#
# 666 ➞ [8]
# // 666 in base8 = 1232
# Suggest kata description edits
# Solution
def esthetic(num):
    ans: list[int] = list()
    for i in range(2, 11):
        top: list[int] = list()
        x: int = num
        while x:
            top.append(x % i)
            x //= i
        if all(abs(x - y) == 1 for x, y in zip(top, top[1:])):
            ans.append(i)
    return ans