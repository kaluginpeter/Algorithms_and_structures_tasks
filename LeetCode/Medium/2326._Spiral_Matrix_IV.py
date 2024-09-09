# You are given two integers m and n, which represent the dimensions of a matrix.
#
# You are also given the head of a linked list of integers.
#
# Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.
#
# Return the generated matrix.
#
#
#
# Example 1:
#
#
# Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
# Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
# Explanation: The diagram above shows how the values are printed in the matrix.
# Note that the remaining spaces in the matrix are filled with -1.
# Example 2:
#
#
# Input: m = 1, n = 4, head = [0,1,2]
# Output: [[0,1,2,-1]]
# Explanation: The diagram above shows how the values are printed from left to right in the matrix.
# The last space in the matrix is set to -1.
#
#
# Constraints:
#
# 1 <= m, n <= 105
# 1 <= m * n <= 105
# The number of nodes in the list is in the range [1, m * n].
# 0 <= Node.val <= 1000
# Solution
# Python O(MN) O(MN)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mtrx: list[list[int]] = [[-1] * n for _ in range(m)]
        right: bool = True
        down = left = up = False
        start_row = start_col = 0
        while head:
            if right:
                right, down = False, True
                for i in range(n):
                    if head:
                        mtrx[start_row][start_col] = head.val
                        head = head.next
                    else: return mtrx
                    start_col += 1
                start_col -= 1
                start_row += 1
            elif down:
                down, left = False, True
                m -= 1
                for i in range(m):
                    if head:
                        mtrx[start_row][start_col] = head.val
                        head = head.next
                    else: return mtrx
                    start_row += 1
                start_row -= 1
                start_col -= 1
            elif left:
                left, up = False, True
                n -= 1
                for i in range(n):
                    if head:
                        mtrx[start_row][start_col] = head.val
                        head = head.next
                    else: return mtrx
                    start_col -= 1
                start_col += 1
                start_row -= 1
            else:
                up, right = False, True
                m -= 1
                n -= 1
                for i in range(m):
                    if head:
                        mtrx[start_row][start_col] = head.val
                        head = head.next
                    else: return mtrx
                    start_row -= 1
                start_row += 1
                start_col += 1
        return mtrx

# C++ O(MN) O(MN)
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> spiralMatrix(int m, int n, ListNode* head) {
        std::vector<std::vector<int>> mtrx(m, std::vector<int>(n, -1));
        int start_row = 0, start_col = 0;
        bool right, down, left, up;
        right = true;
        down = left = up = false;
        while (head) {
            if (right) {
                right = false;
                down = true;
                for (int move = 0; move < n; move++) {
                    if (head){
                        mtrx[start_row][start_col] = head->val;
                        head = head->next;
                    } else {
                        return mtrx;
                    }
                    start_col += 1;
                }
                start_col -= 1;
                start_row += 1;
            } else if (down) {
                down = false;
                left = true;
                m -= 1;
                for (int move = 0; move < m; move++) {
                    if (head) {
                        mtrx[start_row][start_col] = head->val;
                        head = head->next;
                    } else {
                        return mtrx;
                    }
                    start_row += 1;
                }
                start_row -= 1;
                start_col -= 1;
            } else if (left) {
                left = false;
                up = true;
                n -= 1;
                for (int move = 0; move < n; move++) {
                    if (head) {
                        mtrx[start_row][start_col] = head->val;
                        head = head->next;
                    } else {
                        return mtrx;
                    }
                    start_col -= 1;
                }
                start_col += 1;
                start_row -= 1;
            } else {
                up = false;
                right = true;
                m -= 1;
                n -= 1;
                for (int move = 0; move < m; move++) {
                    if (head) {
                        mtrx[start_row][start_col] = head->val;
                        head = head->next;
                    } else {
                        return mtrx;
                    }
                    start_row -= 1;
                }
                start_row += 1;
                start_col += 1;
            }
        }
        return mtrx;
    }
};