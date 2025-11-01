# You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3], head = [1,2,3,4,5]
#
# Output: [4,5]
#
# Explanation:
#
#
#
# Remove the nodes with values 1, 2, and 3.
#
# Example 2:
#
# Input: nums = [1], head = [1,2,1,2,1,2]
#
# Output: [2,2,2]
#
# Explanation:
#
#
#
# Remove the nodes with value 1.
#
# Example 3:
#
# Input: nums = [5], head = [1,2,3,4]
#
# Output: [1,2,3,4]
#
# Explanation:
#
#
#
# No node has value 5.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# All elements in nums are unique.
# The number of nodes in the given list is in the range [1, 105].
# 1 <= Node.val <= 105
# The input is generated such that there is at least one node in the linked list that has a value not present in nums.
# Solution Linked List HashSet O(N) O(N)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        to_delete: set[int] = set(nums)
        tmp = head
        while tmp:
            if head and head.val in to_delete:
                head = head.next
                tmp = head
            elif tmp.next and tmp.next.val in to_delete:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return head


# Python O(N) O(N)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        to_delete: set[int] = set(nums)
        # Delete all nodes thats be in head
        while head and head.val in to_delete:
            head = head.next
        # Delete all nodes in body of linked list
        tmp: Optional[ListNode] = head
        while tmp and tmp.next:
            if tmp.next.val in to_delete:
                tmp.next = tmp.next.next
            else: tmp = tmp.next
        return head
# C++ O(N) O(N)
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
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        unordered_set<int> to_delete;
        for (int number : nums) {
            to_delete.insert(number);
        }
        while (head && to_delete.count(head->val) != 0) {
            head = head->next;
        }
        ListNode* tmp = head;
        while (tmp && tmp->next) {
            if (to_delete.count(tmp->next->val) != 0) {
                tmp->next = tmp->next->next;
            } else {
                tmp = tmp->next;
            }
        }
        return head;
    }
};


# Python O(N) O(D) HashSet LinkedList
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        hashset: set[int] = set(nums)
        dummy: ListNode = ListNode(next=head)
        tmp: ListNode = dummy
        while tmp.next:
            if tmp.next.val in hashset: tmp.next = tmp.next.next
            else: tmp = tmp.next
        return dummy.next

# C++ O(N) O(D) HashSet LinkedList
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
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        std::unordered_set<int> hashset(nums.begin(), nums.end());
        ListNode* dummy = new ListNode(0, head);
        ListNode* tmp = dummy;
        while (tmp->next) {
            if (hashset.count(tmp->next->val)) tmp->next = tmp->next->next;
            else tmp = tmp->next;
        }
        return dummy->next;
    }
};