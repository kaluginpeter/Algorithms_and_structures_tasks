import sys


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    stack: list[int] = []
    operations: dict[str, callable[int, int]] = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }
    commands: list[str] = sys.stdin.readline().rstrip().split()
    for command in commands:
        if command in '+-*/':
            y, x = stack.pop(), stack.pop()
            stack.append(operations[command](x, y))
        else: stack.append(int(command))
    sys.stdout.write(f'{stack[-1]}\n')


if __name__ == '__main__':
    solution()