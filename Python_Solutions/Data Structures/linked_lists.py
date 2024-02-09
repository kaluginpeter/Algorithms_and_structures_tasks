
# Single linked list
# .length() - return the length of linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'[{self.data}]->{self.next}'

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return str(self.head)

    def length(self):
        count: int = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

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