# Given a Sudoku data structure with size NxN, N > 0 and √N == integer, write a method to validate if it has been filled out correctly.
#
# The data structure is a multi-dimensional Array, i.e:
#
# [
#   [7,8,4,  1,5,9,  3,2,6],
#   [5,3,9,  6,7,2,  8,4,1],
#   [6,1,2,  4,3,8,  7,5,9],
#
#   [9,2,8,  7,1,5,  4,6,3],
#   [3,5,7,  8,4,6,  1,9,2],
#   [4,6,1,  9,2,3,  5,8,7],
#
#   [8,7,6,  3,9,4,  2,1,5],
#   [2,4,3,  5,6,1,  9,7,8],
#   [1,9,5,  2,8,7,  6,3,4]
# ]
# Rules for validation
#
# Data structure dimension: NxN where N > 0 and √N == integer
# Rows may only contain integers: 1..N (N included)
# Columns may only contain integers: 1..N (N included)
# 'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)
# ARRAYSPUZZLESALGORITHMS
# Solution
class Sudoku(object):
    def __init__(self, data):
        self.data = data
    def is_valid(self):
        if any(len(i) != len(self.data) for i in self.data):
            return False
        for i in range(len(self.data)):
            s = set(range(1, len(self.data) + 1))
            for j in range(len(self.data)):
                if not isinstance(self.data[i][j], int) or type(self.data[i][j]) == bool:
                    return False
                if self.data[i][j] in s:
                    s.remove(self.data[i][j])
            if len(s) != 0:
                return False
        for i in range(len(self.data)):
            s = set(range(1, len(self.data) + 1))
            for j in range(len(self.data)):
                if self.data[j][i] in s:
                    s.remove(self.data[j][i])
            if len(s) != 0:
                return False
        step = 1
        while step ** 2 < len(self.data):
            step += 1
        pos = list(range(step))
        for i in range(0, len(self.data), step):
            for j in range(0, len(self.data), step):
                s = set(range(1, len(self.data) + 1))
                for k in pos:
                    for l in pos:
                        if self.data[i+k][j + l] not in s:
                            return False
                        else:
                            s.remove(self.data[i+k][j + l])
        return True