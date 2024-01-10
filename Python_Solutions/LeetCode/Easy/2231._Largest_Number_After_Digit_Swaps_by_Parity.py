# You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).
#
# Return the largest possible value of num after any number of swaps.
#
#
#
# Example 1:
#
# Input: num = 1234
# Output: 3412
# Explanation: Swap the digit 3 with the digit 1, this results in the number 3214.
# Swap the digit 2 with the digit 4, this results in the number 3412.
# Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
# Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.
# Example 2:
#
# Input: num = 65875
# Output: 87655
# Explanation: Swap the digit 8 with the digit 6, this results in the number 85675.
# Swap the first digit 5 with the digit 7, this results in the number 87655.
# Note that there may be other sequences of swaps but it can be shown that 87655 is the largest possible number.
#
#
# Constraints:
#
# 1 <= num <= 109
# Solution O(N log N) O(N)
class Solution:
    def largestInteger(self, num: int) -> int:
        odd, even = [], []
        ans: list = []
        while num:
            x = num % 10
            if x % 2 == 0:
                even.append(x)
                ans.append(True)
            else:
                odd.append(x)
                ans.append(False)
            num //= 10
        odd.sort()
        even.sort()
        i: int = 0
        ans = ans[::-1]
        while odd and even:
            if ans[i] == True:
                ans[i] = even.pop()
            else:
                ans[i] = odd.pop()
            i += 1
        while odd:
            ans[i] = odd.pop()
            i += 1
        while even:
            ans[i] = even.pop()
            i += 1
        top: int = 0
        while ans:
            top =  top * 10 + ans.pop(0)
        return top