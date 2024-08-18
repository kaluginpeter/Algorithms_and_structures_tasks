# You are given a string s of even length. Split this string into two halves of equal lengths,
# and let a be the first half and b be the second half.
#
# Two strings are alike if they have the same number of vowels
# ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.
#
# Return true if a and b are alike. Otherwise, return false.
#
# Example 1:
#
# Input: s = "book"
# Output: true
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
# Example 2:
#
# Input: s = "textbook"
# Output: false
# Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
# Notice that the vowel o is counted twice.
#
# Constraints:
# 2 <= s.length <= 1000
# s.length is even.
# s consists of uppercase and lowercase letters.
# Solution
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a, b, top_a, top_b = s[:len(s)//2], s[len(s)//2:], 0, 0
        vowels = 'aeiouAEIOU'
        for i in range(len(a)):
            if a[i] in vowels:
                top_a += 1
            if b[i] in vowels:
                top_b += 1
        return top_a == top_b

# Solution O(N) O(1)
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n: int = len(s) // 2
        count: int = 0
        vowels: set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for i in range(n):
            if s[i] in vowels:
                count += 1
            if s[i + n] in vowels:
                count -= 1
        return count == 0