import sys


class Double_node:
    def __init__(
        self, value: int = None,
        next_: 'Double_node' = None,
        prev_: 'Double_node' = None,
    ) -> None:
        self.value: int = value
        self.next_: Double_node = next_
        self.prev_: Double_node = prev_


class Stack:
    def __init__(self) -> None:
        self.head: Double_node = Double_node()
        self.tail: Double_node = self.head
        self.max_head: Double_node = Double_node()
        self.max_tail: Double_node = Double_node()
        self.size: int = 0
    def push(self, x: int) -> None:
        self.size += 1
        if self.size == 1:
            self.head.next = Double_node(x)
            self.tail = self.head.next
            self.tail.prev = self.head
            self.max_head.next = Double_node(x)
            self.max_tail = self.max_head.next
            self.max_tail.prev = self.max_head
            return
        self.tail.next = Double_node(x)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
        self.max_tail.next = Double_node(max(self.max_tail.value, x))
        self.max_tail.next.prev = self.max_tail
        self.max_tail = self.max_tail.next
    def pop(self) -> None:
        if not self.size:
            sys.stdout.write('error\n')
            return
        self.tail = self.tail.prev
        self.max_tail = self.max_tail.prev
        self.size -= 1
    def get_max(self) -> None:
        if not self.size:
            sys.stdout.write('None\n')
            return
        sys.stdout.write(str(self.max_tail.value) + '\n')
    def top(self) -> None:
        if not self.size:
            sys.stdout.write('error\n')
            return
        sys.stdout.write(str(self.tail.value) + '\n')


def solution(t: int) -> None:
    """
    Time Complexity O(1)
    Memory Complexity O(N)
    """
    stack: Stack = Stack()
    for _ in range(t):
        method: str = sys.stdin.readline().rstrip()
        if method.startswith('get_max'):
            stack.get_max()
        elif method.startswith('pop'):
            stack.pop()
        elif method.startswith('top'):
            stack.top()
        else:
            num: int = int(method.split()[-1])
            stack.push(num)

if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)