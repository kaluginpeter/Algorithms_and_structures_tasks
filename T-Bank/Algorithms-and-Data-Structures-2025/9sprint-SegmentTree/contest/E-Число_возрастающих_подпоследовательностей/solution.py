import sys
import bisect

MOD: int = 10**9 + 7

class SegmentTree:
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.max_len: list[int] = [0] * (4 * size)
        self.count: list[int] = [0] * (4 * size)
    
    def update(self, idx: int, l: int, r: int, pos: int, new_len: int, new_count: int) -> None:
        if l == r:
            if new_len > self.max_len[idx]:
                self.max_len[idx] = new_len
                self.count[idx] = new_count
            elif new_len == self.max_len[idx]:
                self.count[idx] = (self.count[idx] + new_count) % MOD
            return
        mid: int = l + ((r - l) >> 1)
        if pos <= mid:
            self.update(2 * idx + 1, l, mid, pos, new_len, new_count)
        else:
            self.update(2 * idx + 2, mid + 1, r, pos, new_len, new_count)
        left_len: int = self.max_len[2 * idx + 1]
        right_len: int = self.max_len[2 * idx + 2]
        if left_len > right_len:
            self.max_len[idx] = left_len
            self.count[idx] = self.count[2 * idx + 1]
        elif left_len < right_len:
            self.max_len[idx] = right_len
            self.count[idx] = self.count[2 * idx + 2]
        else:
            self.max_len[idx] = left_len
            self.count[idx] = (self.count[2 * idx + 1] + self.count[2 * idx + 2]) % MOD
    
    def query(self, idx: int, l: int, r: int, ql: int, qr: int) -> tuple[int, int]:
        if qr < l or ql > r:
            return (0, 0)
        if ql <= l and r <= qr:
            return (self.max_len[idx], self.count[idx])
        mid: int = l + ((r - l) >> 1)
        left_len, left_count = self.query(2 * idx + 1, l, mid, ql, qr)
        right_len, right_count = self.query(2 * idx + 2, mid + 1, r, ql, qr)
        if left_len > right_len:
            return (left_len, left_count)
        elif left_len < right_len:
            return (right_len, right_count)
        else:
            return (left_len, (left_count + right_count) % MOD)

def solution() -> None:
    """
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))

    sorted_nums: list[int] = sorted(set(nums))
    compressed: dict[int, int] = {v: i for i, v in enumerate(sorted_nums)}
    max_compressed: int = len(sorted_nums)
    nums_compressed: list[int] = [compressed[v] for v in nums]

    st: SegmentTree = SegmentTree(max_compressed)
    dp_len: list[int] = [1] * n
    dp_count: list[int] = [1] * n

    for i in range(n):
        current: int = nums_compressed[i]
        if current > 0:
            res_len, res_count = st.query(0, 0, max_compressed - 1, 0, current - 1)
            if res_len + 1 > dp_len[i]:
                dp_len[i] = res_len + 1
                dp_count[i] = res_count
            elif res_len + 1 == dp_len[i]:
                dp_count[i] = (dp_count[i] + res_count) % MOD
        st.update(0, 0, max_compressed - 1, current, dp_len[i], dp_count[i])

    total: tuple[int, int] = st.query(0, 0, max_compressed - 1, 0, max_compressed - 1)
    sys.stdout.write('{}\n'.format(total[1]))

if __name__ == '__main__':
    solution()