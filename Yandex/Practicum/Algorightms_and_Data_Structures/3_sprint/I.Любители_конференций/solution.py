import sys


def solution(n: int, universities_id: list[int], k: int) -> None:
    """
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    """
    hashmap: dict[int, int] = dict()
    for university_id in universities_id:
        hashmap[university_id] = hashmap.get(university_id, 0) + 1
    universities_id_distinct: list[int] = sorted(hashmap.keys(), reverse=True, key=lambda university_id: (hashmap[university_id], -university_id))
    for idx in range(min(len(universities_id_distinct), k)):
        if idx:
            sys.stdout.write(' ')
        sys.stdout.write(str(universities_id_distinct[idx]))
    sys.stdout.write('\n')


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    universities_id: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    k: int = int(sys.stdin.readline().rstrip())
    solution(n, universities_id, k)