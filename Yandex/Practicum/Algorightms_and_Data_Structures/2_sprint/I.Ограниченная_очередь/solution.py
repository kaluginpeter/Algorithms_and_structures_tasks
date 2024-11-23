import sys


class MyQueueSized:
    def __init__(self, n: int) -> None:
        self.queue: list[int] = [0] * n
        self.head: int = 0
        self.tail: int = 0
        self.capacity: int = n
        self.size_: int = 0

    def push(self, x: int) -> None:
        if self.size_ == self.capacity:
            sys.stdout.write('error\n')
            return
        self.queue[self.tail] = x
        self.tail = (self.tail + 1) % self.capacity
        self.size_ += 1

    def pop(self) -> None:
        if not self.size_:
            sys.stdout.write('None\n')
            return
        sys.stdout.write(str(self.queue[self.head]) + '\n')
        self.queue[self.head] = 0
        self.head = (self.head + 1) % self.capacity
        self.size_ -= 1

    def peek(self) -> None:
        if not self.size_:
            sys.stdout.write('None\n')
            return
        sys.stdout.write(str(self.queue[self.head]) + '\n')

    def size(self) -> None:
        sys.stdout.write(str(self.size_) + '\n')


def solution(t: int) -> None:
    """
    Time Complexity O(N) for building queue and O(1) for each operation
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline().rstrip())
    queue: MyQueueSized = MyQueueSized(n)
    for _ in range(t):
        command: str = sys.stdin.readline().rstrip()
        if command.startswith('push'):
            queue.push(command.split()[1])
        elif command.startswith('pop'):
            queue.pop()
        elif command.startswith('peek'):
            queue.peek()
        else:
            queue.size()


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)