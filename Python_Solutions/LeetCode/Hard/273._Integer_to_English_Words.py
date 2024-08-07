# Convert a non-negative integer num to its English words representation.
#
#
#
# Example 1:
#
# Input: num = 123
# Output: "One Hundred Twenty Three"
# Example 2:
#
# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:
#
# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
#
#
# Constraints:
#
# 0 <= num <= 231 - 1
# Solution HashTable Recursion String O(log10(N)) O(log10(N))
class Solution:
    def get_string_representation(self, n: int) -> list[str]:
        if n == 0: return ['Zero']
        modules: dict[int, str] = {
            1_000_000_000: 'Billion', 1_000_000: 'Million',
            1_000: 'Thousand', 100: 'Hundred', 90: 'Ninety',
            80: 'Eighty', 70: 'Seventy', 60: 'Sixty',
            50: 'Fifty', 40: 'Forty', 30: 'Thirty',
            20: 'Twenty', 19: 'Nineteen', 18: 'Eighteen',
            17: 'Seventeen', 16: 'Sixteen', 15: 'Fifteen',
            14: 'Fourteen', 13: 'Thirteen', 12: 'Twelve', 11: 'Eleven',
            10: 'Ten', 9: 'Nine', 8: 'Eight',
            7: 'Seven', 6: 'Six', 5: 'Five', 4: 'Four', 3: 'Three',
            2: 'Two', 1: 'One',
        }
        have_own_names: set[int] = {
            90, 80, 70, 60, 50, 40, 30, 20,
            19, 18, 17, 16, 15, 14, 13, 12,
            11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
        }
        output: list[str] = []
        for module in modules:
            if n >= module:
                if module in have_own_names:
                    output.append(modules[module])
                    n -= module
                else:
                    quotitent: int = n // module
                    str_quotitent: str = self.get_string_representation(quotitent)
                    # Because str_quotitent is list of strings
                    output.extend(str_quotitent)
                    output.append(modules[module])
                    n %= module
        return output

    def numberToWords(self, num: int) -> str:
        str_num: list[str] = self.get_string_representation(num)
        return ' '.join(str_num)