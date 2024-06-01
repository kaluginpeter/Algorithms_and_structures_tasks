# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#
#
#
# Example 1:
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:
#
# Input: digits = ""
# Output: []
# Example 3:
#
# Input: digits = "2"
# Output: ["a","b","c"]
#
#
# Constraints:
#
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
# Brute Force
# Complexity
# Time complexity: O(N**K)
# Space complexity: O(N**K)
# Where N is length of letters in digits and K is length of digits

# Code
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        digits_store: dict[str, str] = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }
        output: list[str] = list()
        if len(digits) == 1:
            return list(digits_store.get(digits))
        elif len(digits) == 2:
            for i in digits_store.get(digits[0]):
                for j in digits_store.get(digits[1]):
                    output.append(i + j)
        elif len(digits) == 3:
            for i in digits_store.get(digits[0]):
                for j in digits_store.get(digits[1]):
                    for k in digits_store.get(digits[2]):
                        output.append(i + j + k)
        elif len(digits) == 4:
            for i in digits_store.get(digits[0]):
                for j in digits_store.get(digits[1]):
                    for k in digits_store.get(digits[2]):
                        for l  in digits_store.get(digits[3]):
                            output.append(i + j + k + l)
        return output

# Backtracking
# Complexity
# Time complexity: O(N**K)
# Space complexity: O(N**K)
# Where N is length of letters in digits and K is length of digits

# Code
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtracking(idx: int, current_string: str) -> None:
            if len(current_string) == len(digits):
                output.append(current_string)
                return
            for letter in digits_store.get(digits[idx]):
                backtracking(idx + 1, current_string + letter)
        digits_store: dict[str, str] = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }
        output: list[str] = list()
        if digits: backtracking(0, '')
        return output