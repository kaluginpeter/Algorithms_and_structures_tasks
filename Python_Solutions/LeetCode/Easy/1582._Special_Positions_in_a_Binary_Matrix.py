# Given an m x n binary matrix mat, return the number of special positions in mat.
#
# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
#
#
#
# Example 1:
#
#
# Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
# Output: 1
# Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
# Example 2:
#
#
# Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# mat[i][j] is either 0 or 1.
# Solution
class Solution(object):
    def numSpecial(self, mat):
        count = 0
        m, n = 0, 0
        while m < len(mat):
            for i in range(len(mat[m])):
                if mat[m][i] == 1:
                    top = 0
                    for k in range(len(mat[m])):
                        if mat[m][k] == 1:
                            top += 1
                            if top > 1:
                                break
                    if top == 1:
                        top = 0
                        for j in range(len(mat)):
                            if mat[j][i] == 1:
                                top += 1
                                if top > 1:
                                    break
                    if top == 1:
                        count += 1
            m += 1
        return count
# Solution 2 Python syntax sugar
class Solution(object):
    def numSpecial(self, mat):
        count = 0
        m = 0
        while m < len(mat):
            if mat[m].count(1) == 1:
                if sum(i[mat[m].index(1)] == 1 for i in mat) == 1:
                    count += 1
            m += 1
        return count