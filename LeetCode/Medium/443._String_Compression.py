# Given an array of characters chars, compress it using the following algorithm:
#
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
#
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
#
# After you are done modifying the input array, return the new length of the array.
#
# You must write an algorithm that uses only constant extra space.
#
#
#
# Example 1:
#
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
# Example 2:
#
# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.
# Example 3:
#
# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
#
#
# Constraints:
#
# 1 <= chars.length <= 2000
# chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
# Solutions
# For loop
# Complexity
# Time complexity: O(N)
# Space complexity: O(1)
# Code
class Solution:
    def compress(self, chars: List[str]) -> int:
        main_index: int = 0
        left = right = 0
        for current_index in range(1, len(chars)):
            if chars[current_index] == chars[right]:
                right += 1
            elif left == right:
                chars[main_index] = chars[left]
                main_index += 1
                left = right = current_index
            else:
                chars[main_index] = chars[left]
                main_index += 1
                for num in str(right - left + 1):
                    chars[main_index] = num
                    main_index += 1
                left = right = current_index
        if left == right:
            chars[main_index] = chars[left]
            main_index += 1
        else:
            chars[main_index] = chars[left]
            main_index += 1
            for num in str(right - left + 1):
                chars[main_index] = num
                main_index += 1
        return main_index

# While loop
# Complexity
# Time complexity: O(N)
# Space complexity: O(1)
# Code
class Solution:
    def compress(self, chars: List[str]) -> int:
        main_index: int = 0
        left: int = 0
        while left < len(chars):
            right: int = left
            frequence: int = 0
            while right < len(chars) and chars[right] == chars[left]:
                right += 1
                frequence += 1
            chars[main_index] = chars[left]
            main_index += 1
            if frequence > 1:
                for num in str(frequence):
                    chars[main_index] = num
                    main_index += 1
            left = right
        return main_index