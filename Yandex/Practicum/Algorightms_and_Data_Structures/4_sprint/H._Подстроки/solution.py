import sys


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(K), where K is length of distinct characters
    """
    sentence: str = sys.stdin.readline().rstrip()
    hashmap: dict[str, int] = dict()
    max_sub: int = 0
    left: int = 0
    for right in range(len(sentence)):
        hashmap[sentence[right]] = hashmap.get(sentence[right], 0) + 1
        if len(hashmap) != right - left + 1:
            hashmap[sentence[left]] -= 1
            if not hashmap[sentence[left]]:
                del hashmap[sentence[left]]
            left += 1
        max_sub = max(max_sub, right - left + 1)
    sys.stdout.write(str(max_sub) + '\n')


if __name__ == '__main__':
    solution()
