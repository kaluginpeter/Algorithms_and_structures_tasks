
# Single linked list
# .length() -> int - return the length of linked list
# .append(val: objext) -> None - will append given object at the end of linked list
#     if appending object will be first in linked list, linked list automatically create head of list
# .__str__() -> str - by this method you can use builtin python method print()
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f'[{self.data}]'

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self) -> str:
        result: list = []
        temp = self.head
        while temp:
            result.append(str(temp))
            temp = temp.next
        result.append('None')
        return '->'.join(result)

    def length(self) -> int:
        count: int = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def append(self, val: object) -> None:
        if not self.head:
            self.head = Node(data=val)
            return
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(data=val, next=None)

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
