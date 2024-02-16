# Design a HashSet without using any built-in hash table libraries.
#
# Implement MyHashSet class:
#
# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
#
#
# Example 1:
#
# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]
#
# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)
#
#
# Constraints:
#
# 0 <= key <= 106
# At most 104 calls will be made to add, remove, and contains.
# Solution Single Linked List
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyHashSet:

    def __init__(self):
        self.head = None

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        if not self.head:
            self.head = Node(val=key)
            return
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(val=key)
        return

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        if not self.head.next:
            self.head = None
            return
        if self.head.val == key:
            self.head = self.head.next
            return
        tmp = self.head
        while tmp.val != key:
            tmp = tmp.next
        prev_tmp = self.head
        while prev_tmp.next.val != tmp.val:
            prev_tmp = prev_tmp.next
        prev_tmp.next = tmp.next

    def contains(self, key: int) -> bool:
        tmp = self.head
        while tmp:
            if tmp.val == key:
                return True
            tmp = tmp.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)