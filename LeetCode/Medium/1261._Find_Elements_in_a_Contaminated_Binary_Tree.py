# Given a binary tree with the following rules:
#
# root.val == 0
# For any treeNode:
# If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
# If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
# Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.
#
# Implement the FindElements class:
#
# FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
# bool find(int target) Returns true if the target value exists in the recovered binary tree.
#
#
# Example 1:
#
#
# Input
# ["FindElements","find","find"]
# [[[-1,null,-1]],[1],[2]]
# Output
# [null,false,true]
# Explanation
# FindElements findElements = new FindElements([-1,null,-1]);
# findElements.find(1); // return False
# findElements.find(2); // return True
# Example 2:
#
#
# Input
# ["FindElements","find","find","find"]
# [[[-1,-1,-1,-1,-1]],[1],[3],[5]]
# Output
# [null,true,true,false]
# Explanation
# FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
# findElements.find(1); // return True
# findElements.find(3); // return True
# findElements.find(5); // return False
# Example 3:
#
#
# Input
# ["FindElements","find","find","find","find"]
# [[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
# Output
# [null,true,false,false,true]
# Explanation
# FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
# findElements.find(2); // return True
# findElements.find(3); // return False
# findElements.find(4); // return False
# findElements.find(5); // return True
#
#
# Constraints:
#
# TreeNode.val == -1
# The height of the binary tree is less than or equal to 20
# The total number of nodes is between [1, 104]
# Total calls of find() is between [1, 104]
# 0 <= target <= 106
# Solution
# Python O(V) O(V) Tree HashSet Depth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.root: TreeNode = root
        self.hashset: set[int] = set()
        self.recover_tree(root, 0, self.hashset)

    def recover_tree(self, root: TreeNode, depth: int, hashset: set[int]):
        if not depth:
            root.val = 0
            hashset.add(root.val)
        if root.left:
            root.left.val = root.val * 2 + 1
            hashset.add(root.left.val)
            self.recover_tree(root.left, depth + 1, hashset)
        if root.right:
            root.right.val = root.val * 2 + 2
            hashset.add(root.right.val)
            self.recover_tree(root.right, depth + 1, hashset)

    def find(self, target: int) -> bool:
        return target in self.hashset

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

# C++ O(V) O(V) Tree HashSet Depth-First-Search
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
class FindElements {
private:
    TreeNode* mainRoot;
    std::unordered_set<int> hashset;
public:
    void recoverTree(TreeNode* root, int depth, std::unordered_set<int>& hashset) {
        if (!depth) {
            root->val = 0;
            hashset.insert(root->val);
        }
        if (root->left) {
            root->left->val = root->val * 2 + 1;
            hashset.insert(root->left->val);
            recoverTree(root->left, depth + 1, hashset);
        }
        if (root->right) {
            root->right->val = root->val * 2 + 2;
            hashset.insert(root->right->val);
            recoverTree(root->right, depth + 1, hashset);
        }
    }

    FindElements(TreeNode* root) {
        hashset = {};
        recoverTree(root, 0, hashset);
        mainRoot = root;
    }

    bool find(int target) {
        return hashset.count(target);
    }
};

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements* obj = new FindElements(root);
 * bool param_1 = obj->find(target);
 */