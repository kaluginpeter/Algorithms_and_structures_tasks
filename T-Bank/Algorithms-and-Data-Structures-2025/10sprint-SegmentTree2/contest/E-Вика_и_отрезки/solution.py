import sys

class Event:
    def __init__(self, x: int, y1: int, y2: int, type_: int) -> None:
        self.x: int = x
        self.y1: int = y1
        self.y2: int = y2
        self.type_: int = type_
    
    def __lt__(self, other: 'Event') -> bool:
        if self.x != other.x: return self.x < other.x
        return self.type_ > other.type_


class SegmentTree:
    def __init__(self, coords: list[int]) -> None:
        self.y_coords: list[int] = coords
        n: int = len(coords) - 1
        self.count: list[int] = [0] * (4 * n)
        self.length: list[int] = [0] * (4 * n)
        self.build(1, 0, n - 1)
    
    def build(self, node: int, start: int, end: int) -> None:
        self.count[node] = 0
        self.length[node] = 0
        
        if start == end: return
        
        mid: int = start + ((end - start) >> 1)
        self.build(2 * node, start, mid)
        self.build(2 * node + 1, mid + 1, end)
    
    def update(self, node: int, start: int, end: int, l: int, r: int, val: int) -> None:
        if start > r or end < l: return
        
        if start >= l and end <= r:
            self.count[node] += val
            if self.count[node] > 0:
                self.length[node] = self.y_coords[end + 1] - self.y_coords[start]
            else:
                if start == end: self.length[node] = 0
                else:
                    self.length[node] = self.length[2 * node] + self.length[2 * node + 1]
            return
        mid: int = start + ((end - start) >> 1)
        self.update(2 * node, start, mid, l, r, val)
        self.update(2 * node + 1, mid + 1, end, l, r, val)
        
        if self.count[node] > 0:
            self.length[node] = self.y_coords[end + 1] - self.y_coords[start]
        else:
            self.length[node] = self.length[2 * node] + self.length[2 * node + 1]
    
    def update_range(self, l: int, r: int, val: int) -> None:
        self.update(1, 0, len(self.y_coords) - 2, l, r, val)
    
    def get_length(self) -> int:
        return self.length[1]


def solution() -> None:
    """
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline().rstrip())
    events: list[Event] = []
    y_coords_set: set[int] = set()
    
    for _ in range(n):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
        if x1 > x2: x1, x2 = x2, x1
        if y1 > y2: y1, y2 = y2, y1
        
        if y1 == y2:
            events.append(Event(x1, y1, y1 + 1, 1))
            events.append(Event(x2 + 1, y1, y1 + 1, -1))
        else:
            events.append(Event(x1, y1, y2 + 1, 1))
            events.append(Event(x1 + 1, y1, y2 + 1, -1))
        
        y_coords_set.add(y1)
        y_coords_set.add(y1 + 1)
        if y1 != y2:
            y_coords_set.add(y2)
            y_coords_set.add(y2 + 1)
    
    y_coords: list[int] = sorted(list(y_coords_set))
    y_compress: dict[int, int] = {coord: idx for idx, coord in enumerate(y_coords)}
    events.sort()
    seg_tree = SegmentTree(y_coords)
    total_cells: int = 0
    prev_x: int = events[0].x
    
    for event in events:
        width = event.x - prev_x
        total_cells += width * seg_tree.get_length()
        y1_idx = y_compress[event.y1]
        y2_idx = y_compress[event.y2] - 1
        seg_tree.update_range(y1_idx, y2_idx, event.type_)
        prev_x = event.x
    
    sys.stdout.write('{}\n'.format(total_cells))


if __name__ == '__main__':
    solution()
