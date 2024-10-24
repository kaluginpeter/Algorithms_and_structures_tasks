# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
#
# BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
# boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
# int next() Moves the pointer to the right, then returns the number at the pointer.
# Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.
#
# You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.
#
#
#
# Example 1:
#
#
# Input
# ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
# Output
# [null, 3, 7, true, 9, true, 15, true, 20, false]
#
# Explanation
# BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
# bSTIterator.next();    // return 3
# bSTIterator.next();    // return 7
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 9
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 15
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 20
# bSTIterator.hasNext(); // return False
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 105].
# 0 <= Node.val <= 106
# At most 105 calls will be made to hasNext, and next.
#
#
# Follow up:
#
# Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?
# Solution
# C++ O(N) O(N) Depth-First-Search
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
class BSTIterator {
public:
    std::vector<int> stack_;
    int index = 0;
    BSTIterator(TreeNode* root) {
        dfs(root);
    }

    void dfs(TreeNode* root) {
        if (!root) {
            return;
        }
        dfs(root->left);
        stack_.push_back(root->val);
        dfs(root->right);
    }

    int next() {
        int output = stack_[index];
        ++index;
        return output;
    }

    bool hasNext() {
        return index < stack_.size();
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */

# Python O(N) O(N) Depth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack: list[TreeNode] = []
        self.dfs(root)
        self.idx: int = 0

    def dfs(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        self.dfs(root.left)
        self.stack.append(root.val)
        self.dfs(root.right)

    def next(self) -> int:
        output: int = self.stack[self.idx]
        self.idx += 1
        return output

    def hasNext(self) -> bool:
        return self.idx < len(self.stack)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# C++
# Optimize DFS
# Complexity
# Time complexity: O(h), next = hasNext = O(1)
# Space complexity: O(h)
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
class BSTIterator {
public:
    std::vector<TreeNode*> stack_;
    BSTIterator(TreeNode* root) {
        pushLeft(root);
    }

    void pushLeft(TreeNode* root) {
        while (root) {
            stack_.push_back(root);
            root = root->left;
        }
    }

    int next() {
        TreeNode* output = stack_[stack_.size() - 1];
        stack_.pop_back();
        pushLeft(output->right);
        return output->val;
    }

    bool hasNext() {
        return stack_.size();
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */

# Python
# Optimize DFS
# Complexity
# Time complexity: O(h), next = hasNext = O(1)
# Space complexity: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]) -> None:
        self.stack: list[TreeNode] = []
        self.push_left(root)

    def push_left(self, node: TreeNode) -> None:
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        output: TreeNode = self.stack.pop()
        self.push_left(output.right)
        return output.val

    def hasNext(self) -> bool:
        return bool(self.stack)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()