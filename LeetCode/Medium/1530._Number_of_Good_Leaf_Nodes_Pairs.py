# You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.
#
# Return the number of good leaf node pairs in the tree.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3,null,4], distance = 3
# Output: 1
# Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.
# Example 2:
#
#
# Input: root = [1,2,3,4,5,6,7], distance = 3
# Output: 2
# Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.
# Example 3:
#
# Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
# Output: 1
# Explanation: The only good pair is [2,5].
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 210].
# 1 <= Node.val <= 100
# 1 <= distance <= 10
# Solution DFS O(N*K**2) O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    good_pairs: int = 0
    def dfs(self, root, distance):
        if not root: return []
        if not root.left and not root.right:
            return [1]
        left_leafs: list[int] = self.dfs(root.left, distance)
        right_leafs: list[int] = self.dfs(root.right, distance)
        for l_leaf in left_leafs:
            for r_leaf in right_leafs:
                if l_leaf + r_leaf <= distance:
                    self.good_pairs += 1
        return [dist_leaf + 1 for dist_leaf in left_leafs + right_leafs if dist_leaf + 1 < distance]

    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.dfs(root, distance)
        return self.good_pairs