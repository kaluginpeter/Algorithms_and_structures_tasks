# Given the head of a linked list, rotate the list to the right by k places.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:
#
#
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
#
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109
# Solution
# Python O(N) O(1) TwoPointers LinkedList
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k: return head
        tmp: ListNode = head
        size: int = 0
        while tmp:
            size += 1
            tmp = tmp.next
        k %= size
        if not k: return head
        tmp = head
        for _ in range(size - k - 1): tmp = tmp.next
        output: ListNode = tmp.next
        tmp.next = None
        tmp = output
        while tmp and tmp.next: tmp = tmp.next
        tmp.next = head
        return output

# C++ O(N) O(1) TwoPointers LinkedList
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
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !k) return head;
        size_t size = 0;
        ListNode* tmp = head;
        while (tmp) {
            tmp = tmp->next;
            ++size;
        }
        k %= size;
        if (!k) return head;
        tmp = head;
        for (size_t i = 0; i < size - k - 1; ++i) tmp = tmp->next;
        ListNode* output = tmp->next;
        tmp->next = nullptr;
        tmp = output;
        while (tmp && tmp->next) tmp = tmp->next;
        tmp->next = head;
        return output;

    }
};


# Python O(N) O(1) TwoPointer LinkedList
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n: int = 0
        tail: ListNode = head
        while tail:
            n += 1
            if not tail.next: break
            tail = tail.next
        if n: k %= n
        if not k or not n: return head
        predecessor: ListNode = head
        for i in range(n - k - 1): predecessor = predecessor.next
        new_head: ListNode = predecessor.next
        predecessor.next = None
        tail.next = head
        return new_head

# C++ O(N) O(1) LinkedList TwoPointers
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
    ListNode* rotateRight(ListNode* head, int k) {
        size_t n = 0;
        ListNode* tail = head;
        while (tail) {
            ++n;
            if (!tail->next) break;
            tail = tail->next;
        }
        if (n) k %= n; // avoid redundant overlap
        if (!k || !n) return head;
        ListNode* predecessor = head;
        for (size_t i = 0; i < n - k - 1; ++i) {
            predecessor = predecessor->next;
        }
        ListNode* newHead = predecessor->next;
        predecessor->next = nullptr;
        tail->next = head;
        return newHead;
    }
};