# An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.
#
# Given an integer n, return true if n is strictly palindromic and false otherwise.
#
# A string is palindromic if it reads the same forward and backward.
#
#
#
# Example 1:
#
# Input: n = 9
# Output: false
# Explanation: In base 2: 9 = 1001 (base 2), which is palindromic.
# In base 3: 9 = 100 (base 3), which is not palindromic.
# Therefore, 9 is not strictly palindromic so we return false.
# Note that in bases 4, 5, 6, and 7, n = 9 is also not palindromic.
# Example 2:
#
# Input: n = 4
# Output: false
# Explanation: We only consider base 2: 4 = 100 (base 2), which is not palindromic.
# Therefore, we return false.
#
#
#
# Constraints:
#
# 4 <= n <= 105
# Solution Two Pointer + Math O(N) O(1)
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def is_palindrome(arr: list) -> bool:
            left, right = 0, len(arr) - 1
            while left < right:
                if arr[left] != arr[right]:
                    return False
                left, right = left + 1, right - 1
            return True
        def num_to_base(num: int, base: int) -> list:
            if num == 0:
                return [0]
            ans: list = list()
            while num:
                ans.append(num % base)
                num //= base
            return ans[::-1]
        for base in range(2, n - 1):
            if not is_palindrome(num_to_base(n, base)):
                return False
        return True