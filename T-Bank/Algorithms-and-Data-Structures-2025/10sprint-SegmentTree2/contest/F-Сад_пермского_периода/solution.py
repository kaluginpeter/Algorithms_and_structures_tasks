import sys
from typing import List, Callable
from dataclasses import dataclass


@dataclass
class Center:
    x: int
    y: int
    id: int


def solution() -> None:
    """
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    """
    n = int(sys.stdin.readline().rstrip().split()[2])
    centers: list[Center] = []
    for id in range(n):
        x, y = map(float, sys.stdin.readline().split())
        centers.append(Center(int(x * 2), int(y * 2), id))
    y_coords: list[int] = sorted(set(center.y for center in centers))
    x: list[int] = [0] * len(y_coords)
    
    def get_x(index: int) -> int:
        sum_val: int = 0
        while index >= 0:
            sum_val += x[index]
            index = (index & (index + 1)) - 1
        return sum_val
    
    def add_since_x(index: int, extra: int) -> None:
        while index < len(x):
            x[index] += extra
            index = index | (index + 1)
    
    def add_range_x(first: int, after: int, extra: int) -> None:
        add_since_x(first, extra)
        add_since_x(after, -extra)
    
    centers.sort(key=lambda center: center.x)
    ans: list[int] = [0] * n
    for center in centers:
        index: int = bisect_left(y_coords, center.y)
        dist: int = center.x - get_x(index)
        ans[center.id] = dist
        first: int = bisect_right(y_coords, center.y - dist)
        after: int = bisect_right(y_coords, center.y + dist)
        add_range_x(first, after, dist * 2)
    sys.stdout.write(' '.join(map(str, ans)) + '\n')


def bisect_left(a: list[int], x: int) -> int:
    lo, hi = 0, len(a)
    while lo < hi:
        mid: int = lo + ((hi - lo) >> 1)
        if a[mid] < x: lo = mid + 1
        else: hi = mid
    return lo


def bisect_right(a: list[int], x: int) -> int:
    lo, hi = 0, len(a)
    while lo < hi:
        mid: int = lo + ((hi - lo) >> 1)
        if x < a[mid]: hi = mid
        else: lo = mid + 1
    return lo


if __name__ == "__main__":
    solution()
