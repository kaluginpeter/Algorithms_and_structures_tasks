# You are given a positive integer k. You are also given:
#
# a 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and
# a 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].
# The two arrays contain integers from 1 to k.
#
# You have to build a k x k matrix that contains each of the numbers from 1 to k exactly once. The remaining cells should have the value 0.
#
# The matrix should also satisfy the following conditions:
#
# The number abovei should appear in a row that is strictly above the row at which the number belowi appears for all i from 0 to n - 1.
# The number lefti should appear in a column that is strictly left of the column at which the number righti appears for all i from 0 to m - 1.
# Return any matrix that satisfies the conditions. If no answer exists, return an empty matrix.
#
#
#
# Example 1:
#
#
# Input: k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
# Output: [[3,0,0],[0,0,1],[0,2,0]]
# Explanation: The diagram above shows a valid example of a matrix that satisfies all the conditions.
# The row conditions are the following:
# - Number 1 is in row 1, and number 2 is in row 2, so 1 is above 2 in the matrix.
# - Number 3 is in row 0, and number 2 is in row 2, so 3 is above 2 in the matrix.
# The column conditions are the following:
# - Number 2 is in column 1, and number 1 is in column 2, so 2 is left of 1 in the matrix.
# - Number 3 is in column 0, and number 2 is in column 1, so 3 is left of 2 in the matrix.
# Note that there may be multiple correct answers.
# Example 2:
#
# Input: k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]
# Output: []
# Explanation: From the first two conditions, 3 has to be below 1 but the third conditions needs 3 to be above 1 to be satisfied.
# No matrix can satisfy all the conditions, so we return the empty matrix.
#
#
# Constraints:
#
# 2 <= k <= 400
# 1 <= rowConditions.length, colConditions.length <= 104
# rowConditions[i].length == colConditions[i].length == 2
# 1 <= abovei, belowi, lefti, righti <= k
# abovei != belowi
# lefti != righti
# Solution Topological sorting DFS O(N**2) O(N**2)
from collections import defaultdict
class Solution:
    def dfs(self, source, destinations, visited, previous_path, path):
        # Case if we have cycle
        if source in previous_path: return -1
        # Case if vertex already been visited, but its not a cycle(like children or tail of graph)
        if source in visited: return
        # Add vertex in visited path of global DFS vertexes
        visited.add(source)
        # Add vertex to current DFS path
        previous_path.add(source)
        # Iterate from all possible destionations from current source
        for destination in destinations[source]:
            # Make DFS on each destination
            # Case if we have cycle
            if self.dfs(destination, destinations, visited, previous_path, path) == -1:
                return -1
        # Add current vertex to path
        path.append(source)
        # Clear current DFS path
        previous_path.remove(source)

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # Make adjasency list representing rows conditions
        row_vertexes: dict[int, set[int]] = defaultdict(set)
        for source, destination in rowConditions:
            row_vertexes[source].add(destination)
        # Make topoligical sorting for rows conditions
        row_path: list[int] = []
        row_visited: set[int] = set()
        row_previous_path: set[int] = set()
        for vertex in range(1, k + 1):
            if self.dfs(vertex, row_vertexes, row_visited, row_previous_path, row_path) == -1:
                return []
        row_path.reverse()
        # Create adjasency list represent columns conditions
        col_vertexes: dict[int, set[int]] = defaultdict(set)
        for source, destination in colConditions:
            col_vertexes[source].add(destination)
        # Make topological sort for columns conditions
        col_path: list[int] = []
        col_visited: set[int] = set()
        col_previous_path: set[int] = set()
        for vertex in range(1, k + 1):
            if self.dfs(vertex, col_vertexes, col_visited, col_previous_path, col_path) == -1:
                return []
        col_path.reverse()
        # Define correct position for each number in (1 to k) inclusive range
        positions: dict[int, list[int, int]] = defaultdict(list)
        # Initially define correct row position for each number
        for vertex in range(1, k + 1):
            positions[row_path[vertex - 1]].append(vertex - 1)
        # Then define correct col position for each number
        for vertex in range(1, k + 1):
            positions[col_path[vertex - 1]].append(vertex - 1)
        # Construct k*k matrix
        mtrx: list[list[int]] = [[0] * k for _ in range(k)]
        # Place numbers by his correct row and col positions
        for ceil in positions:
            row, col = positions[ceil]
            mtrx[row][col] = ceil

        return mtrx