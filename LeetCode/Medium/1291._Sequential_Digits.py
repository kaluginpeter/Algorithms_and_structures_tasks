# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
#
# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
#
#
#
# Example 1:
#
# Input: low = 100, high = 300
# Output: [123,234]
# Example 2:
#
# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
#
#
# Constraints:
#
# 10 <= low <= high <= 10^9
# Solution O(K * 9) where K is high // 10 Memory O(N)
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits: str = '123456789'
        ans: list = []
        n1, n2 = len(str(low)), len(str(high))
        while n1 <= n2:
            for i in range(9 - (n1 - 1)):
                x: int = int(digits[i:i+n1])
                if x < low:
                    continue
                if x <= high:
                    ans.append(x)
                else:
                    break
            n1 += 1
        return ans