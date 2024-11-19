import sys


class Stack:
    def __init__(self) -> None:
        self.stack: list[int] = []
        self.max_stack: list[int] = []

    def pop(self) -> int:
        if self.stack:
            self.max_stack.pop()
            return self.stack.pop()
        sys.stdout.write('error\n')

    def push(self, x: int) -> None:
        self.max_stack.append(x if not self.stack else max(x, self.max_stack[-1]))
        self.stack.append(x)

    def get_max(self) -> int | str:
        return self.max_stack[-1] if self.stack else 'None'


def solution(t: int) -> None:
    """
    Time Complexity O(1)
    Memory Complexity O(N)
    """
    stack: Stack = Stack()
    for _ in range(t):
        method: str = sys.stdin.readline().rstrip()
        if method.startswith('get_max'):
            sys.stdout.write(str(stack.get_max()) + '\n')
        elif method.startswith('push'):
            stack.push(int(method.split()[-1]))
        else:
            stack.pop()


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
