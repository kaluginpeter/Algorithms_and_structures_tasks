# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.
#
#
#
# Example 1:
#
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:
#
# Input: lists = []
# Output: []
# Example 3:
#
# Input: lists = [[]]
# Output: []
#
#
# Constraints:
#
# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.
# Solution
# Python O(NlogN) O(N) PriorityQueue
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap: list[int] = []
        for linked_list in lists:
            while linked_list:
                heapq.heappush(min_heap, linked_list.val)
                linked_list = linked_list.next
        head: ListNode = ListNode()
        tmp: ListNode = head
        while min_heap:
            tmp.next = ListNode(heapq.heappop(min_heap))
            tmp = tmp.next
        return head.next

# C++ O(NlogN) O(N) PriorityQueue
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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
            std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
            for (ListNode* &linkedList : lists) {
                while (linkedList) {
                    minHeap.push(linkedList->val);
                    linkedList = linkedList->next;
                }
            }
            ListNode *head = new ListNode();
            ListNode *tmp = head;
            while (!minHeap.empty()) {
                ListNode *node = new ListNode(minHeap.top());
                minHeap.pop();
                tmp->next = node;
                tmp = tmp->next;
            }
            return head->next;
    }
};