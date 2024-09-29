# Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.
#
# Implement the AllOne class:
#
# AllOne() Initializes the object of the data structure.
# inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
# dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
# getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
# getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
# Note that each function must run in O(1) average time complexity.
#
#
#
# Example 1:
#
# Input
# ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
# [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
# Output
# [null, null, null, "hello", "hello", null, "hello", "leet"]
#
# Explanation
# AllOne allOne = new AllOne();
# allOne.inc("hello");
# allOne.inc("hello");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "hello"
# allOne.inc("leet");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "leet"
#
#
# Constraints:
#
# 1 <= key.length <= 10
# key consists of lowercase English letters.
# It is guaranteed that for each call to dec, key is existing in the data structure.
# At most 5 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey.
# Solution
# Python O(1) O(N) HashMap Double Linked List
class DoubleLinkedNode:
    def __init__(
            self,
            freq: int = 0,
            prev=None,
            next=None
    ) -> None:
        self.freq: int = freq
        self.prev: DoubleLinkedNode = prev
        self.next: DoubleLinkedNode = next
        self.keys: set[str] = set()


class AllOne:
    def __init__(self):
        self.hashmap: dict[str, DoubleLinkedNode] = dict()
        self.head: DoubleLinkedNode = DoubleLinkedNode()
        self.tail: DoubleLinkedNode = DoubleLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key in self.hashmap:
            node: DoubleLinkedNode = self.hashmap[key]
            node.keys.remove(key)
            if not node.next or node.next.freq != node.freq + 1:
                node.next = DoubleLinkedNode(node.freq + 1, node, node.next)
                node.next.next.prev = node.next
            node.next.keys.add(key)
            self.hashmap[key] = node.next
            if not node.keys:
                node.next.prev = node.prev
                node.prev.next = node.next
        else:
            if not self.head.next or self.head.next.freq != 1:
                self.head.next = DoubleLinkedNode(1, self.head, self.head.next)
                self.head.next.next.prev = self.head.next
            self.head.next.keys.add(key)
            self.hashmap[key] = self.head.next

    def dec(self, key: str) -> None:
        if key not in self.hashmap: return
        node: DoubleLinkedNode = self.hashmap[key]
        node.keys.remove(key)
        if node.freq == 1:
            if not node.keys:
                node.prev.next = node.next
                node.next.prev = node.prev
            del self.hashmap[key]
            return
        if not node.prev or node.prev.freq != node.freq - 1:
            node.prev = DoubleLinkedNode(node.freq - 1, node.prev, node)
            node.prev.prev.next = node.prev
        node.prev.keys.add(key)
        self.hashmap[key] = node.prev
        if not node.keys:
            node.prev.next = node.next
            node.next.prev = node.prev

    def getMaxKey(self) -> str:
        if self.tail.prev.freq: return next(iter(self.tail.prev.keys))
        return ''

    def getMinKey(self) -> str:
        if self.head.next.freq: return next(iter(self.head.next.keys))
        return ''

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

# C++ O(1) O(N) HashMap Double Linked List
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <string>

class DoubleLinkedNode {
public:
    int freq;
    DoubleLinkedNode* prev;
    DoubleLinkedNode* next;
    std::unordered_set<std::string> keys;

    DoubleLinkedNode(int frequency = 0, DoubleLinkedNode* previous = nullptr, DoubleLinkedNode* nextNode = nullptr)
        : freq(frequency), prev(previous), next(nextNode) {}
};

class AllOne {
public:
    std::unordered_map<std::string, DoubleLinkedNode*> hashmap;
    DoubleLinkedNode* head;
    DoubleLinkedNode* tail;

    AllOne() {
        head = new DoubleLinkedNode();
        tail = new DoubleLinkedNode();
        head->next = tail;
        tail->prev = head;
    }

    void inc(std::string key) {
        if (hashmap.count(key)) {
            DoubleLinkedNode* node = hashmap[key];
            node->keys.erase(key);

            if (!node->next || node->next->freq != node->freq + 1) {
                DoubleLinkedNode* new_node = new DoubleLinkedNode(node->freq + 1, node, node->next);
                node->next->prev = new_node;
                node->next = new_node;
            }
            node->next->keys.insert(key);
            hashmap[key] = node->next;

            if (node->keys.empty()) {
                removeNode(node);
            }
        } else {
            if (head->next == tail || head->next->freq != 1) {
                DoubleLinkedNode* new_node = new DoubleLinkedNode(1, head, head->next);
                head->next->prev = new_node;
                head->next = new_node;
            }
            head->next->keys.insert(key);
            hashmap[key] = head->next;
        }
    }

    void dec(std::string key) {
        if (!hashmap.count(key)) return;

        DoubleLinkedNode* node = hashmap[key];
        node->keys.erase(key);
        if (node->freq == 1) {
            hashmap.erase(key);
            if (node->keys.empty()) {
                removeNode(node);
            }
            return;
        }

        if (!node->prev || node->prev->freq != node->freq - 1) {
            DoubleLinkedNode* new_node = new DoubleLinkedNode(node->freq - 1, node->prev, node);
            node->prev->next = new_node;
            node->prev = new_node;
        }
        node->prev->keys.insert(key);
        hashmap[key] = node->prev;

        if (node->keys.empty()) {
            removeNode(node);
        }
    }

    std::string getMaxKey() {
        if (tail->prev != head) {
            return *(tail->prev->keys.begin());
        }
        return "";
    }

    std::string getMinKey() {
        if (head->next != tail) {
            return *(head->next->keys.begin());
        }
        return "";
    }

private:
    void removeNode(DoubleLinkedNode* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
        delete node;
    }
};


/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne* obj = new AllOne();
 * obj->inc(key);
 * obj->dec(key);
 * string param_3 = obj->getMaxKey();
 * string param_4 = obj->getMinKey();
 */