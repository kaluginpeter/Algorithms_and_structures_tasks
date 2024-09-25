# B. Two Buttons
# time limit per test2 seconds
# memory limit per test256 megabytes
# Vasya has found a strange device. On the front panel of a device there are: a red button, a blue button and a display showing some positive integer. After clicking the red button, device multiplies the displayed number by two. After clicking the blue button, device subtracts one from the number on the display. If at some point the number stops being positive, the device breaks down. The display can show arbitrarily large numbers. Initially, the display shows number n.
#
# Bob wants to get number m on the display. What minimum number of clicks he has to make in order to achieve this result?
#
# Input
# The first and the only line of the input contains two distinct integers n and m (1 ≤ n, m ≤ 104), separated by a space .
#
# Output
# Print a single number — the minimum number of times one needs to push the button required to get the number m out of number n.
#
# Examples
# inputCopy
# 4 6
# outputCopy
# 2
# inputCopy
# 10 1
# outputCopy
# 9
# Note
# In the first example you need to push the blue button once, and then push the red button once.
#
# In the second example, doubling the number is unnecessary, so we need to push the blue button nine times.
# Solution
# Python O(N) O(N)
import sys
from collections import deque

def min_operations(n: int, m: int) -> int:
    if n >= m: return n - m
    queue = deque([(n, 0)])
    visited = set()
    min_count: int = 10**5
    while queue:
        current, steps = queue.popleft()
        if current >= m:
            min_count = min(min_count, steps + (current - m))
            continue
        next_double = current * 2
        if next_double not in visited and next_double <= 2 * m:  # Limit to avoid unnecessary large numbers
            visited.add(next_double)
            queue.append((next_double, steps + 1))
        next_decrement = current - 1
        if next_decrement >= 0 and next_decrement not in visited:
            visited.add(next_decrement)
            queue.append((next_decrement, steps + 1))
    return min_count

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().rstrip().split())
    result = min_operations(n, m)
    sys.stdout.write(str(result) + '\n')