# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.
#
# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.
#
#
#
# Example 1:
#
#
# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
# Example 2:
#
#
# Input: root = [2,1,3]
# Output: [2,1,3]
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# 1 <= Node.val <= 105
# Solution In Order DFS O(N) O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.array: list[int] = []
        def inorder_traversal(root) -> None:
            if not root: return
            inorder_traversal(root.left)
            self.array.append(root.val)
            inorder_traversal(root.right)
        def constructed_bst(left, right):
            if left > right: return
            middle: int = (left + right) >> 1
            left = constructed_bst(left, middle - 1)
            right = constructed_bst(middle + 1, right)
            return TreeNode(self.array[middle], left, right)
        inorder_traversal(root)
        return constructed_bst(0, len(self.array) - 1)


# C++ O(V) O(H + V) DepthFirstSearch
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
    void dfs(TreeNode* root, std::vector<int>& nums) {
        if (!root) return;
        dfs(root->left, nums);
        nums.push_back(root->val);
        dfs(root->right, nums);
    }
    TreeNode* build(std::vector<int>& nums, int left, int right) {
        if (left > right) return nullptr;
        int middle = left + ((right - left) >> 1);
        TreeNode* root = new TreeNode(nums[middle]);
        root->left = build(nums, left, middle - 1);
        root->right = build(nums, middle + 1, right);
        return root;
    }
    TreeNode* balanceBST(TreeNode* root) {
        std::vector<int> nums;
        dfs(root, nums);
        TreeNode* output = build(nums, 0, nums.size() - 1);
        return output;
    }
};

# Python O(V) O(H + V) DepthFirstSearch
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: TreeNode, nums: list[int]) -> None:
        if not root: return
        self.dfs(root.left, nums)
        nums.append(root.val)
        self.dfs(root.right, nums)

    def build(self, nums: list[int], left: int, right: int) -> TreeNode:
        if left > right: return None
        middle: int = left + ((right - left) >> 1)
        root: TreeNode = TreeNode(nums[middle])
        root.left = self.build(nums, left, middle - 1)
        root.right = self.build(nums, middle + 1, right)
        return root

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nums: list[int] = []
        self.dfs(root, nums)
        output: TreeNode = self.build(nums, 0, len(nums) - 1)
        return output