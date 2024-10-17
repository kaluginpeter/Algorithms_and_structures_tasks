# You are given an integer num. You can swap two digits at most once to get the maximum valued number.
#
# Return the maximum valued number you can get.
#
#
#
# Example 1:
#
# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:
#
# Input: num = 9973
# Output: 9973
# Explanation: No swap.
#
#
# Constraints:
#
# 0 <= num <= 108
# Solution
# General idea
# To simplify a problem we can transform number to string of character, where each character represent a digit.
# Then use following idea to solving problem by two pointers technique:
#
# Find index of leftmost value that not equal to '9'. Because by definition in base 10, the biggest digit is already '9', so it's impossible to find digit that gives more if we swap '9'
# 9 9 9 9 3
#         ^
#         L
# Only digit by that index can be possibly changed
# in the future for giving us a bigger number
# After first, step we have a number (left pointer index) that we should swap to get possibly a bigger number. And now we need to find an index of first digit that not equal to our current (left pointer) digit. Because if we choose same digit in the future, like in that case:
# 9 8 8 3
#   ^ ^
#   L R
# By swapping them (left and right) together,
# its not give us a bigger number, because they both equal
# Then start from right index to the end of string and find the maximum digit in that part of array
# 9 8 8 3 4 9 3 4
#       ^        ^
#       R        N
# We need to find rightmost maximum digit in range [R, N)
# where R is our right pointer and N is the end of the string.
# Use >= comparison between digit to find rightmost position
# The next we need to find that position of left pointer,
# that swapping digit by left pointer with
# digit by max_number pointer we get a bigger number.
# 9 8 8 7 6 5 4 2 7
#   ^   ^         ^
#   L   R         MX
# We find a rightmost maximum number between [R, N), but
# digit by left pointer can be greater or equal to our maximum number.
# So iterate until our left pointer not overlapps with
# maximum_number pointer and digit by left pointer
# greater or equal to maximum number.
# while L < MX AND digits[L] >= digits[MX]
# And the last step will be just to check, that we can make a swap between left pointer and maximum_number pointer correctly.
# 9 8 8 7 7 7 7
#             ^
#            L/MX
# In case when maximum number will be less or equal to all of digits by the left pointer.
# Our left pointer just overlaps with maximum number pointer.
# 9 8 8 5 2 6 9 7
#       ^     ^
#       L     MX
# In that case if our left pointer not overlaps with maximum number pointer,
# it means that we can make a swap.
# So check condition:
# if L < MX
# Complexity
# Time complexity: O(N)
#
# Space complexity: O(N)
#
# Where N is length of digits in number
# Python O(N) O(N) Two Pointers Greedy
class Solution:
    def maximumSwap(self, num: int) -> int:
        digits: list[str] = list(str(num))
        left: int = 0
        while left < len(digits) and digits[left] == '9':
            left += 1
        right: int = left
        while right < len(digits) and digits[left] == digits[right]:
            right += 1
        next_number: int = '0'
        number_idx: int = -1
        while right < len(digits):
            if digits[right] >= next_number:
                next_number = digits[right]
                number_idx = right
            right += 1
        while left < number_idx and digits[left] >= digits[number_idx]:
            left += 1
        if left < number_idx:
            digits[left], digits[number_idx] = digits[number_idx], digits[left]
        return int(''.join(digits))

# C++ O(N) O(N) Two Pointers Greedy
class Solution {
public:
    int maximumSwap(int num) {
        std::string digits = std::to_string(num);
        int left = 0;
        while (left < digits.size() && digits[left] == '9') {
            ++left;
        }
        int right = left;
        while (right < digits.size() && digits[left] == digits[right]) {
            ++right;
        }
        char max_number = '0';
        int max_number_idx = -1;
        while (right < digits.size()) {
            if (digits[right] >= max_number) {
                max_number = digits[right];
                max_number_idx = right;
            }
            ++right;
        }
        while (left < max_number_idx && digits[left] >= max_number) {
            ++left;
        }
        if (left < max_number_idx) {
            digits[max_number_idx] = digits[left];
            digits[left] = max_number;
        }
        return std::stoi(digits);
    }
};