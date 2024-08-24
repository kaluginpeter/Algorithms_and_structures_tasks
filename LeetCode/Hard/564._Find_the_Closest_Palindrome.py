# Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.
#
# The closest is defined as the absolute difference minimized between two integers.
#
#
#
# Example 1:
#
# Input: n = "123"
# Output: "121"
# Example 2:
#
# Input: n = "1"
# Output: "0"
# Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
#
#
# Constraints:
#
# 1 <= n.length <= 18
# n consists of only digits.
# n does not have leading zeros.
# n is representing an integer in the range [1, 1018 - 1].
# Solution String Simulation O(N) O(N)
class Solution:

    def choose_optimal(self, n: int, palindrome: list[str], even: bool, current_palindrome: int = 0) -> str:
        left: int = len(n) // 2
        if even: left -= 1
        if not even:
            # Case middle - 1
            current_middle: int = int(palindrome[left])
            if current_middle == 0:
                swap_neighbors = True
                current_middle = 9
            else:
                current_middle = current_middle - 1
            palindrome[left] = str(current_middle)
            palindrome_with_negative_middle: int = int(''.join(palindrome))
            # Case middle + 1
            if current_middle == 9:
                current_middle = 1
            else:
                current_middle = (current_middle + 2) % 10
            palindrome[left] = str(current_middle)
            palindrome_with_bigger_middle: int = int(''.join(palindrome))
            palindrome_less_on_one: int = int(
                ''.join(
                    '9' if idx == left else
                    str(9 if palindrome[idx] == '0' else int(palindrome[idx]) - 1)
                    for idx in range(len(palindrome))
                )
            )
            if palindrome_less_on_one == int(n):
                palindrome_less_on_one = 0
            return str(
                min(
                    current_palindrome,
                    palindrome_with_negative_middle, palindrome_with_bigger_middle,
                    int('9' * (len(n) - 1)),
                    int('1' + '0' * (len(n) - 1) + '1'),
                    palindrome_less_on_one,
                    key=lambda x: (abs(int(n) - x), x)
                )
            )
        # Case middle - 1
        current_middle: int = int(palindrome[left])
        if current_middle == 0:
            current_middle = 9
        else:
            current_middle = current_middle - 1
        palindrome[left] = str(current_middle)
        palindrome[left + 1] = str(current_middle)
        palindrome_with_negative_middle: int = int(''.join(palindrome))
        # Case middle + 1
        if current_middle == 9:
            current_middle = 1
        else:
            current_middle = (current_middle + 2) % 10
        palindrome[left] = str(current_middle)
        palindrome[left + 1] = str(current_middle)
        palindrome_with_bigger_middle: int = int(''.join(palindrome))
        palindrome_less_on_one: int = int(
            ''.join(
                '9' if idx in (left, left + 1) else
                str(9 if palindrome[idx] == '0' else int(palindrome[idx]) - 1)
                for idx in range(len(palindrome))
            )
        )
        if palindrome_less_on_one == int(n):
            palindrome_less_on_one = 0
        return str(
            min(
                current_palindrome,
                palindrome_with_negative_middle, palindrome_with_bigger_middle,
                int('9' * (len(n) - 1)),
                int('1' + '0' * (len(n) - 1) + '1'),
                palindrome_less_on_one,
                key=lambda x: (abs(int(n) - x), x)
            )
        )

    def make_palindrome(self, n: str) -> str:
        even: bool = len(n) & 1 == 0
        palindrome: list[str] = list(n)
        already_palindrome: bool = True
        middle_move: int = None
        left: int = 0
        right: int = len(n) - 1
        while left < right:
            if n[left] != n[right]:
                already_palindrome = False
                palindrome[right] = n[left]
            left += 1
            right -= 1
        current_palindrome: int = int(''.join(palindrome))

        if already_palindrome:
            return self.choose_optimal(n, palindrome, even)
        return self.choose_optimal(n, palindrome, even, current_palindrome)

    def nearestPalindromic(self, n: str) -> str:
        size: int = len(n)
        if size == 1:
            return str(int(n) - 1)

        return self.make_palindrome(n)