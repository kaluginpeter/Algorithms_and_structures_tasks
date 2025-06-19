import sys
import heapq


def solution() -> None:
    """
    Time Complexity O(k)
    Memory Complexity O(k)
    """
    k: int = int(sys.stdin.readline().rstrip())
    min_sum: list[int] = [float('inf')] * k
    min_heap: list[tuple[int, int]] = []
    for num in range(1, 10):
        remainder: int = num % k
        if min_sum[remainder] > num:
            min_sum[remainder] = num
            heapq.heappush(min_heap, (num, remainder))
    while min_heap:
        current_sum, current_remainder = heapq.heappop(min_heap)
        if current_remainder == 0:
            sys.stdout.write('{}\n'.format(current_sum))
            return
        for num in range(10):
            new_sum: int = current_sum + num
            remainder: int = (current_remainder * 10 + num) % k 
            if min_sum[remainder] > new_sum:
                min_sum[remainder] = new_sum
                heapq.heappush(min_heap, (new_sum, remainder))


if __name__ == '__main__':
    solution()