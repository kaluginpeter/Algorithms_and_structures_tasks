# Design your implementation of the circular double-ended queue (deque).
#
# Implement the MyCircularDeque class:
#
# MyCircularDeque(int k) Initializes the deque with a maximum size of k.
# boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
# boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
# boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
# boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
# int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
# int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
# boolean isEmpty() Returns true if the deque is empty, or false otherwise.
# boolean isFull() Returns true if the deque is full, or false otherwise.
#
#
# Example 1:
#
# Input
# ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
# [[3], [1], [2], [3], [4], [], [], [], [4], []]
# Output
# [null, true, true, true, false, 2, true, true, true, 4]
#
# Explanation
# MyCircularDeque myCircularDeque = new MyCircularDeque(3);
# myCircularDeque.insertLast(1);  // return True
# myCircularDeque.insertLast(2);  // return True
# myCircularDeque.insertFront(3); // return True
# myCircularDeque.insertFront(4); // return False, the queue is full.
# myCircularDeque.getRear();      // return 2
# myCircularDeque.isFull();       // return True
# myCircularDeque.deleteLast();   // return True
# myCircularDeque.insertFront(4); // return True
# myCircularDeque.getFront();     // return 4
#
#
# Constraints:
#
# 1 <= k <= 1000
# 0 <= value <= 1000
# At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.
# Solution
# Python Double Linked List Design O(1) O(k)
class ListNode:
    def __init__(self, value: int, next_: ListNode = None, prev: ListNode = None) -> None:
        self.value: int = value
        self.next: ListNode = next_
        self.prev: ListNode = prev


class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity: int = k
        self.size: int = 0
        self.head: ListNode = None
        self.tail: ListNode = self.head

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        if not self.size:
            self.head = ListNode(value=value)
            self.tail = self.head
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            self.head = ListNode(value=value, next_=self.head, prev=self.tail)
            self.head.next.prev = self.head
            self.tail.next = self.head
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        if not self.size:
            self.head = ListNode(value=value)
            self.tail = self.head
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            self.tail.next = ListNode(value=value, next_=self.head, prev=self.tail)
            self.tail = self.tail.next
            self.head.prev = self.tail
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        if self.size == 1:
            self.head = None
            self.tail = self.head
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        if self.size == 1:
            self.head = None
            self.tail = self.head
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self.head.value

    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self.tail.value

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

# C++ O(1) O(k) Double Linked List
class DoubleListNode {
public:
    int value;
    DoubleListNode* next;
    DoubleListNode* prev;
    DoubleListNode(int val, DoubleListNode* nextNode = nullptr, DoubleListNode* prevNode = nullptr)
        : value(val), next(nextNode), prev(prevNode) {}
};
class MyCircularDeque {
private:
    int capacity;
    int size;
    DoubleListNode* head;
    DoubleListNode* tail;

public:
    MyCircularDeque(int k) : capacity(k), size(0), head(nullptr), tail(nullptr) {}

    bool insertFront(int value) {
        if (isFull()) {
            return false;
        }
        DoubleListNode* newNode = new DoubleListNode(value);
        if (isEmpty()) {
            head = tail = newNode;
            head->next = head;
            head->prev = head;
        } else {
            newNode->next = head;
            newNode->prev = tail;
            head->prev = newNode;
            tail->next = newNode;
            head = newNode;
        }
        size++;
        return true;
    }

    bool insertLast(int value) {
        if (isFull()) {
            return false;
        }
        DoubleListNode* newNode = new DoubleListNode(value);
        if (isEmpty()) {
            head = tail = newNode;
            head->next = head;
            head->prev = head;
        } else {
            newNode->prev = tail;
            newNode->next = head;
            tail->next = newNode;
            head->prev = newNode;
            tail = newNode;
        }
        size++;
        return true;
    }
    bool deleteFront() {
        if (isEmpty()) {
            return false;
        }
        if (size == 1) {
            delete head;
            head = tail = nullptr;
        } else {
            DoubleListNode* toDelete = head;
            head = head->next;
            head->prev = tail;
            tail->next = head;
            delete toDelete;
        }
        size--;
        return true;
    }

    bool deleteLast() {
        if (isEmpty()) {
            return false;
        }
        if (size == 1) {
            delete head;
            head = tail = nullptr;
        } else {
            DoubleListNode* toDelete = tail;
            tail = tail->prev;
            tail->next = head;
            head->prev = tail;
            delete toDelete;
        };
        size--;
        return true;
    }

    int getFront() {
        if (isEmpty()) {
            return -1;
        };
        return head->value;
    }

    int getRear() {
        if (isEmpty()) {
            return -1;
        };
        return tail->value;
    }

    bool isEmpty() {
        return size == 0;
    }

    bool isFull() {
        return size == capacity;
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */