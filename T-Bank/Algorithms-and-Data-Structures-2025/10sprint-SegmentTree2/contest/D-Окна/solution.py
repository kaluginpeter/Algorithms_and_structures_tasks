import sys

class Event:
    __slots__ = ('x', 'y1', 'y2', 'type_')
    def __init__(self, x: int, y1: int, y2: int, type_: int) -> None:
        self.x: int = x
        self.y1: int = y1
        self.y2: int = y2
        self.type_: int = type_
    
    def __lt__(self, other: 'Event') -> bool:
        if self.x != other.x: return self.x < other.x
        return self.type_ > other.type_

class SegmentTree:
    __slots__ = ('size', 'max_cnt', 'cnt', 'lazy', 'max_pos')
    def __init__(self, n: int) -> None:
        self.size: int = 1
        while self.size < n: self.size <<= 1
        self.max_cnt: list[int] = [0] * (2 * self.size)
        self.cnt: list[int] = [0] * (2 * self.size)
        self.lazy: list[int] = [0] * (2 * self.size)
        self.max_pos: list[int] = [0] * (2 * self.size)
        for i in range(self.size): self.max_pos[i + self.size] = i
        for i in range(self.size - 1, 0, -1): self.max_pos[i] = self.max_pos[2 * i]
    
    def push(self, node: int, node_l: int, node_r: int) -> None:
        if self.lazy[node] == 0: return
        self.max_cnt[node] += self.lazy[node]
        self.cnt[node] += self.lazy[node]
        if node_l != node_r:
            self.lazy[2 * node] += self.lazy[node]
            self.lazy[2 * node + 1] += self.lazy[node]
        self.lazy[node] = 0
    
    def update_range(self, l: int, r: int, v: int, node: int = 1, node_l: int = 0, node_r: int = None) -> None:
        if node_r is None: node_r = self.size - 1
        self.push(node, node_l, node_r)
        if r < node_l or l > node_r: return
        if l <= node_l and node_r <= r:
            self.lazy[node] += v
            self.push(node, node_l, node_r)
            return
        mid: int = node_l + ((node_r - node_l) >> 1)
        self.update_range(l, r, v, 2 * node, node_l, mid)
        self.update_range(l, r, v, 2 * node + 1, mid + 1, node_r)
        if self.max_cnt[2 * node] >= self.max_cnt[2 * node + 1]:
            self.max_cnt[node] = self.max_cnt[2 * node]
            self.max_pos[node] = self.max_pos[2 * node]
        else:
            self.max_cnt[node] = self.max_cnt[2 * node + 1]
            self.max_pos[node] = self.max_pos[2 * node + 1]
        self.cnt[node] = max(self.cnt[2 * node], self.cnt[2 * node + 1])
    
    def get_max(self) -> tuple[int, int]:
        self.push(1, 0, self.size - 1)
        return (self.max_cnt[1], self.max_pos[1])

def solution() -> None:
    """
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline())
    events: list[Event] = []
    min_y: int = float('inf')
    max_y: int = float('-inf')
    for _ in range(n):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        if y1 > y2: y1, y2 = y2, y1
        events.append(Event(x1, y1, y2, 1))
        events.append(Event(x2, y1, y2, -1))
        min_y = min(min_y, y1)
        max_y = max(max_y, y2)
    events.sort()
    y_range = max_y - min_y + 1
    st: SegmentTree = SegmentTree(y_range)
    max_overlap: int = 0
    result_x: int = 0
    result_y: int = 0
    for event in events:
        current_max, pos = st.get_max()
        if current_max > max_overlap:
            max_overlap = current_max
            result_x = event.x
            result_y = pos + min_y
        st.update_range(event.y1 - min_y, event.y2 - min_y, event.type_)
    sys.stdout.write('{}\n{} {}\n'.format(max_overlap, result_x, result_y))

if __name__ == '__main__':
    solution()