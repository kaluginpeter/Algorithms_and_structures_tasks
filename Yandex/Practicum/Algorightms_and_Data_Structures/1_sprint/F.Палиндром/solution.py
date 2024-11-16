import sys

def solution(sentence: str) -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(1)
    """
    is_valid: bool = True
    left: int = 0
    right: int = len(sentence) - 1
    while left < right:
        while left < right and not sentence[left].isalnum():
            left += 1
        while left < right and not sentence[right].isalnum():
            right -= 1
        if left < right and sentence[left].lower() != sentence[right].lower():
            is_valid = False
            break
        left += 1
        right -= 1
    sys.stdout.write('True' if is_valid else 'False')

if __name__ == '__main__':
    sentence: str = sys.stdin.readline().rstrip()
    solution(sentence)
