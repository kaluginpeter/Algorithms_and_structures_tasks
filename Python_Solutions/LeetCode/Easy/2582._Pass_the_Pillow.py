# There are n people standing in a line labeled from 1 to n. The first person in the line is holding a pillow initially. Every second, the person holding the pillow passes it to the next person standing in the line. Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.
#
# For example, once the pillow reaches the nth person they pass it to the n - 1th person, then to the n - 2th person and so on.
# Given the two positive integers n and time, return the index of the person holding the pillow after time seconds.
#
#
#
# Example 1:
#
# Input: n = 4, time = 5
# Output: 2
# Explanation: People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2.
# After five seconds, the 2nd person is holding the pillow.
# Example 2:
#
# Input: n = 3, time = 2
# Output: 3
# Explanation: People pass the pillow in the following way: 1 -> 2 -> 3.
# After two seconds, the 3rd person is holding the pillow.
#
#
# Constraints:
#
# 2 <= n <= 1000
# 1 <= time <= 1000
# Solutions

# Simulation
# Complexity
# Time complexity: O(N)
# Space complexity: O(1)
# Code
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        pillow: int = 1
        reverse: bool = False
        while time:
            if reverse:
                pillow -= 1
            else:
                pillow += 1
            if pillow == 1 or pillow == n:
                reverse = not reverse
            time -= 1
        return pillow

# Math
# Complexity
# Time complexity: O(1)
# Space complexity: O(1)
# Code
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        whole: int = time // (n - 1)
        remainder: int = time % (n - 1)
        return 1 + remainder if whole & 1 == 0 else n - remainder