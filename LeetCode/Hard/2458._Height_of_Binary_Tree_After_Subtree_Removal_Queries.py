# You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.
#
# You have to perform m independent queries on the tree where in the ith query you do the following:
#
# Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.
# Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.
#
# Note:
#
# The queries are independent, so the tree returns to its initial state after each query.
# The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.
#
#
# Example 1:
#
#
# Input: root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]
# Output: [2]
# Explanation: The diagram above shows the tree after removing the subtree rooted at node with value 4.
# The height of the tree is 2 (The path 1 -> 3 -> 2).
# Example 2:
#
#
# Input: root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8]
# Output: [3,2,3,2]
# Explanation: We have the following queries:
# - Removing the subtree rooted at node with value 3. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 4).
# - Removing the subtree rooted at node with value 2. The height of the tree becomes 2 (The path 5 -> 8 -> 1).
# - Removing the subtree rooted at node with value 4. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 6).
# - Removing the subtree rooted at node with value 8. The height of the tree becomes 2 (The path 5 -> 9 -> 3).
#
#
# Constraints:
#
# The number of nodes in the tree is n.
# 2 <= n <= 105
# 1 <= Node.val <= n
# All the values in the tree are unique.
# m == queries.length
# 1 <= m <= min(n, 104)
# 1 <= queries[i] <= n
# queries[i] != root.val
# Solution
# C++ O(N + Q) O(N) Depth-First-Search
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxHeightAtLevel[100001];
    int currentMaxHeightAtLevel = 0;

    void dfsLeftToRight(TreeNode* root, int currentHeight) {
        if (!root) {
            return;
        }
        maxHeightAtLevel[root->val] = currentMaxHeightAtLevel;
        currentMaxHeightAtLevel = std::max(currentMaxHeightAtLevel, currentHeight);
        dfsLeftToRight(root->left, currentHeight + 1);
        dfsLeftToRight(root->right, currentHeight + 1);
    }

    void dfsRightToLeft(TreeNode* root, int currentHeight) {
        if (!root) {
            return;
        }
        maxHeightAtLevel[root->val] = std::max(maxHeightAtLevel[root->val], currentMaxHeightAtLevel);
        currentMaxHeightAtLevel = std::max(currentMaxHeightAtLevel, currentHeight);
        dfsRightToLeft(root->right, currentHeight + 1);
        dfsRightToLeft(root->left, currentHeight + 1);
    }

    vector<int> treeQueries(TreeNode* root, vector<int>& queries) {
        dfsLeftToRight(root, 0);
        currentMaxHeightAtLevel = 0;
        dfsRightToLeft(root, 0);
        std::vector<int> answer;
        for (int query : queries) {
            answer.push_back(maxHeightAtLevel[query]);
        }
        return answer;
    }
};

# Python O(N + Q) O(N) Depth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.node_depths: dict[int, int]
        self.subtree_heights: dict[int, int]
        self.first_largest_height: dict[int, int]
        self.second_largest_height: dict[int, int]

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        self.node_depths = dict()
        self.subtree_heights = dict()
        self.first_largest_height = dict()
        self.second_largest_height = dict()
        self.dfs(root, 0)
        answer: list[int] = []
        for query in queries:
            max_depth: int = self.node_depths[query]
            if self.subtree_heights[query] == self.first_largest_height[self.node_depths[query]]:
                max_depth += self.second_largest_height.get(self.node_depths[query], 0)
            else:
                max_depth += self.first_largest_height.get(self.node_depths[query], 0)
            answer.append(max_depth - 1)
        return answer

    def dfs(self, root: TreeNode, level: int) -> int:
        if not root:
            return 0
        self.node_depths[root.val] = level
        left_part: int = self.dfs(root.left, level + 1)
        right_part: int = self.dfs(root.right, level + 1)
        max_height_at_level: int = 1 + max(left_part, right_part)
        self.subtree_heights[root.val] = max_height_at_level
        if max_height_at_level > self.first_largest_height.get(level, 0):
            self.second_largest_height[level] = self.first_largest_height.get(level, 0)
            self.first_largest_height[level] = max_height_at_level
        elif max_height_at_level > self.second_largest_height.get(level, 0):
            self.second_largest_height[level] = max_height_at_level
        return max_height_at_level