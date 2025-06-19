import sys


class Stack:
    def __init__(self) -> None:
        self.stack: list[int] = []
        self.min_stack: list[int] = []
    
    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(x)
            self.min_stack.append(x)
        else:
            self.stack.append(x)
            self.min_stack.append(min(self.min_stack[-1], x))
    
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
    
    def get_min(self) -> int:
        return self.min_stack[-1]



def solution() -> None:
    """
    Time Complexity O(1) for operations
    Memory Complexity O(N) for storage
    """
    stack: Stack = Stack()
    n: int = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        operation, *args = map(int, sys.stdin.readline().rstrip().split())
        if operation == 1:
            stack.push(args[0])
        elif operation == 2:
            stack.pop()
        else:
            sys.stdout.write(f'{stack.get_min()}\n')


if __name__ == '__main__':
    solution()