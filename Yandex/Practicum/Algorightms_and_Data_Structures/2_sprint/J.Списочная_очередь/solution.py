import sys

class QueueNode:
    def __init__(self, x: int) -> None:
        self.value: int = x
        self.nxt: QueueNode = None

class Queue:
    def __init__(self) -> None:
        self.head: QueueNode = None
        self.tail: QueueNode = None
        self.size_: int = 0
    def get(self) -> None:
        if not self.size_:
            sys.stdout.write('error\n')
            return
        sys.stdout.write(str(self.head.value) + '\n')
        self.head = self.head.nxt
        self.size_ -= 1
    def put(self, x: int) -> None:
        self.size_ += 1
        if self.size_ == 1:
            self.head = QueueNode(x)
            self.tail = self.head
            return
        self.tail.nxt = QueueNode(x)
        self.tail = self.tail.nxt
    def size(self) -> None:
        sys.stdout.write(str(self.size_) + '\n')


def solution(t: int) -> None:
    """
    Time Complexity O(1)
    Memory Complexity O(N) for store N items
    """
    queue: Queue = Queue()
    for _ in range(t):
        command: str = sys.stdin.readline().rstrip()
        if command.startswith('get'):
            queue.get()
        elif command.startswith('put'):
            queue.put(int(command.split()[1]))
        else:
            queue.size()


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)