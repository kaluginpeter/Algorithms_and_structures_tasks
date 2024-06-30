# You are given two integers red and blue representing the count of red and blue colored balls. You have to arrange these balls to form a triangle such that the 1st row will have 1 ball, the 2nd row will have 2 balls, the 3rd row will have 3 balls, and so on.
#
# All the balls in a particular row should be the same color, and adjacent rows should have different colors.
#
# Return the maximum height of the triangle that can be achieved.
#
#
#
# Example 1:
#
# Input: red = 2, blue = 4
#
# Output: 3
#
# Explanation:
#
#
#
# The only possible arrangement is shown above.
#
# Example 2:
#
# Input: red = 2, blue = 1
#
# Output: 2
#
# Explanation:
#
#
# The only possible arrangement is shown above.
#
# Example 3:
#
# Input: red = 1, blue = 1
#
# Output: 1
#
# Example 4:
#
# Input: red = 10, blue = 1
#
# Output: 2
#
# Explanation:
#
#
# The only possible arrangement is shown above.
#
#
#
# Constraints:
#
# 1 <= red, blue <= 100
# Solution O(N) O(1)
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        copy_x, copy_y = red, blue
        layers = [copy_x, copy_y]
        flag = False
        accs = [1, 2]
        count_copy: int = 0
        while True: # Simulate red, blue positions first
            if layers[flag] - accs[flag] >= 0:
                count_copy += 1
                layers[flag] -= accs[flag]
                accs[flag] += 2
                flag = not flag
            else: break
        layers = [blue, red]
        accs = [1, 2]
        main_total: int = 0
        flag = False
        while True: # Simluate blue, red positions second
            if layers[flag] - accs[flag] >= 0:
                main_total += 1
                layers[flag] -= accs[flag]
                accs[flag] += 2
                flag = not flag
            else: break
        return max(main_total, count_copy) # return maximum of them