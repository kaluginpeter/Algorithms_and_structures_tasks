
# Single linked list
# .length() -> int - return the length of linked list
# .append(val: objext) -> None - will append given object at the end of linked list
#     if appending object will be first in linked list, linked list automatically create head of list
# .__str__() -> str - by this method you can use builtin python method print()
# .search(val: object) -> bool - will return boolean value True if object exists in list otherwise False
# .pop() -> None - will pop element at the end of the list
# .reverse() -> None - will reverse linked list by speed O(N) and memory O(1)
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f'[{self.data}]'


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self) -> str:
        if self.length() == 0:
            return 'None'
        result: list = []
        temp = self.head
        while temp.next:
            result.append(str(temp))
            temp = temp.next
        result.append(str(temp))
        result.append('None')
        return '->'.join(result)

    def length(self) -> int:
        return self.size

    def append(self, val: object) -> None:
        self.size += 1
        if not self.head:
            self.head = Node(data=val)
            return
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(data=val)

    def search(self, val: object) -> bool:
        tmp = self.head
        while tmp:
            if tmp.data == val:
                return True
            tmp = tmp.next
        return False

    def pop(self) -> None:
        if self.length() == 0:
            raise ValueError("You can't delete from empty list")
        if self.size == 1:
            self.head = None
            self.size -= 1
            return
        tmp = self.head
        while tmp.next.next:
            tmp = tmp.next
        tmp.next = None
        self.size -= 1
        return

    def reverse(self):
        if self.length() == 0:
            raise ValueError("You can't reverse empty list")
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

# Example of usage
# linkedlist = SingleLinkedList()
# temp = Node(1)
# linkedlist.head = temp
# for i in range(2, 6):
#     temp.next Node(i)
#     temp = temp.next
# print(linkedlist)
#     [1]->[2]->[3]->[4]->[5]->None
# print(linkedlist.length())
#     5
# Example of usage part 2
# linkedlist = SingleLinkedList()
# for i in range(1, 6):
#     linkedlist.append(i)
# print(linkedlist)
#     [1]->[2]->[3]->[4]->[5]->None
# print(linkedlist.length())
#     5


# Double Linked List implementation
# .append(n: object) -> None - will append object to the tail of list
# .prepend(n: object) -> None - will append object to the head of list
# .pop() -> object - will delete element at the tail of list
# .size() -> int - will return size of linked list
# .__len__() -> int - by this method you can use builtin python len()
# .is_empty() -> bool - return boolean True if list is empty otherwise False
# .__str__() -> str - by this method you can use builtin python print()
# .contains(n: object) -> bool - will return boolean True if object in list otherwise False
# .__contains__(item: object) -> bool - by this method you can use builtin python "in" method
# .remove(n: object) -> None - will remove given object in a list
# .remove_at(i: int) -> None - will remove object by given index (0-based indexing)
# .clear() -> None - will remove all elements in a list
class DoubleNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        return f'[{self.data}]'


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, n: object) -> None:
        if self.is_empty():
            self.head = DoubleNode(data=n, prev=None, next=None)
            self.tail = self.head
        else:
            self.tail.next = DoubleNode(data=n, prev=self.tail, next=None)
            self.tail = self.tail.next
        self.length += 1

    def prepend(self, n: object) -> None:
        if self.is_empty():
            self.head = DoubleNode(data=n, prev=None, next=None)
            self.tail = self.head
        else:
            nxt = self.head
            self.head = DoubleNode(data=n, prev=None, next=nxt)
        self.length += 1

    def pop(self) -> object:
        if self.is_empty():
            raise ValueError('List is empty')
        if self.size() == 1:
            data = self.head
            self.head = None
            self.tail = self.head
        else:
            data = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return data

    def size(self) -> int:
        return self.length

    def __len__(self) -> int:
        return self.length

    def is_empty(self) -> bool:
        return self.size() == 0

    def __str__(self):
        if self.length == 0:
            return 'None'
        result: list = ['None']
        tmp = self.head
        while tmp:
            result.append(str(tmp))
            tmp = tmp.next
        result.append('None')
        return '<->'.join(result)

    def contains(self, n: object) -> bool:
        tmp = self.head
        while tmp:
            if tmp.data == n:
                return True
            tmp = tmp.next
        return False

    def __contains__(self, item) -> bool:
        return self.contains(item)

    def remove(self, n: object):
        if self.is_empty():
            raise ValueError('List is empty')
        if not self.contains(n):
            raise ValueError('Unexciting object')
        if self.size() == 1:
            self.length -= 1
            self.head = None
            self.tail = self.head
        else:
            tmp = self.head
            while tmp.data != n:
                tmp = tmp.next
            if tmp.prev:
                tmp.prev.next = tmp.next
            else:
                self.head = tmp.next
            if tmp.next:
                tmp.next.prev = tmp.prev
            else:
                self.tail = tmp.prev
            self.length -= 1

    def remove_at(self, i: int) -> None:
        if i > self.size() or i < 0:
            raise ValueError('Index out of list')
        tmp = self.head
        for j in range(i):
            tmp = tmp.next
        self.remove(tmp.data)

    def clear(self) -> None:
        self.head = None
        self.tail = self.head
        self.length = 0


class CycleLinkedList:
    def __init__(self, head: object = None):
        self.head: object = head
        self.last: object = self.head
        self.size: int = 0

    def __str__(self):
        if self.size == 0:
            return 'None'
        ans: list[str] = list()
        tmp: object = self.head
        while tmp:
            ans.append(str(tmp))
            tmp = tmp.next
        ans.append('None')
        return '->'.join(ans)

    def append(self, x: any) -> None:
        if self.size == 0:
            self.head = Node(data=x)
            self.last = self.head
            self.size += 1
            return
        self.last.next = Node(data=x, next=self.head)
        self.size += 1
        self.last = self.last.next

    # TODO rewrite for contains and remove methods
    def pop(self) -> object:
        if self.size == 0:
            raise ValueError("You can't delete from empty list")
        if self.size == 1:
            self.head = None
            self.last = self.head
            self.size -= 1
            return
        tmp: object = self.head
        while
