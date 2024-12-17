import sys

def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    t: int = int(sys.stdin.readline().rstrip())
    hashset: set[str] = set()
    for _ in range(t):
        activity: str = sys.stdin.readline().rstrip()
        if activity not in hashset:
            hashset.add(activity)
            sys.stdout.write(activity + '\n')

if __name__ == '__main__':
    solution()