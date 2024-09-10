# You are given two positive integers a and b.
#
# You can perform the following operations on a so as to obtain b :
#
# (a-1)/2   (if (a-1) is divisible by 2)
# a/2       (if a is divisible by 2)
# a*2
# b will always be a power of 2.
#
# You are to write a function operation(a,b) that efficiently returns the minimum number of operations required to transform a into b.
#
# For example :
#
# operation(2,8) -> 2
# 2*2 = 4
# 4*2 = 8
#
# operation(9,2) -> 2
# (9-1)/2 = 4
# 4/2 = 2
#
# operation(1024,1024) -> 0
# FUNDAMENTALSALGORITHMS
# Solution
from collections import deque


def operation(a, b):
    if a == b: return 0

    queue: list[tuple[int, int]] = deque([(a, 0)])  # (current_value, operations_count)
    visited: list[int] = set([a])

    while queue:
        current, operations_count = queue.popleft()
        if current == b: return operations_count

        if (current - 1) % 2 == 0 and (current - 1) // 2 not in visited:
            new_value: int = (current - 1) // 2
            queue.append((new_value, operations_count + 1))
            visited.add(new_value)

        if current % 2 == 0 and current // 2 not in visited:
            new_value: int = current // 2
            queue.append((new_value, operations_count + 1))
            visited.add(new_value)

        if current * 2 not in visited:
            new_value: int = current * 2
            queue.append((new_value, operations_count + 1))
            visited.add(new_value)

    return -1