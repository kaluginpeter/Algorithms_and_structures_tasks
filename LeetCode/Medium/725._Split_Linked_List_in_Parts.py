# Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.
#
# The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.
#
# The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
#
# Return an array of the k parts.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but its string representation as a ListNode is [].
# Example 2:
#
#
# Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
# Output: [[1,2,3,4],[5,6,7],[8,9,10]]
# Explanation:
# The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
#
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 1000].
# 0 <= Node.val <= 1000
# 1 <= k <= 50
# Solution
# Python O(N) O(K), where K is length of parts of linked list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n: int = 0
        tmp: Optional[ListNode] = head
        while tmp:
            n += 1
            tmp = tmp.next
        part_length: int = n // k - 1
        additional: int = [0, n % k][n > k and n % k != 0]
        linked_list_parts: list[Optional[ListNode]] = []
        for _ in range(k):
            if not head:
                linked_list_parts.append(head)
            else:
                tmp_head: Optional[ListNode] = head
                tmp: Optional[ListNode] = tmp_head
                for _ in range(part_length + int(additional > 0)):
                    tmp = tmp.next
                head = tmp.next
                tmp.next = None
                linked_list_parts.append(tmp_head)
                additional -= 1

        return linked_list_parts

# C++ O(N) O(K), where K is length of parts of linked list
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
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        int n = 0;
        ListNode* tmp = head;
        while (tmp) {
            n += 1;
            tmp = tmp->next;
        }
        int part_length = n / k - 1;
        int remainder = 0;
        if (n % k != 0) {
            remainder += n % k;
        }
        vector<ListNode*> linked_list_parts;
        for (int i = 0; i < k; i++) {
            if (head) {
                ListNode* tmp_head = head;
                ListNode* tmp = tmp_head;
                for (int move = 0; move < part_length + (remainder > 0); move++) {
                    tmp = tmp->next;
                }
                head = tmp->next;
                tmp->next = nullptr;
                linked_list_parts.push_back(tmp_head);
                remainder -= 1;
            } else {
                linked_list_parts.push_back(head);
            }
        }
        return linked_list_parts;
    }
};