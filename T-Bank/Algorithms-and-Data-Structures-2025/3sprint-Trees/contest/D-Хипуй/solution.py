import sys

class MaxHeap:
    def __init__(self) -> None:
        self.arr: list[int] = [0] # Dummy 0 for 1-indexing 
    
    def insert(self, x: int) -> None:
        self.arr.append(x)
        x_idx: int = len(self.arr) - 1
        while x_idx > 1:
            parent_idx: int = x_idx >> 1
            if self.arr[parent_idx] >= self.arr[x_idx]: break
            self.arr[x_idx], self.arr[parent_idx] = self.arr[parent_idx], self.arr[x_idx]
            x_idx = parent_idx
    
    def extract(self) -> int:
        last_idx: int = len(self.arr) - 1 
        self.arr[1], self.arr[last_idx] = self.arr[last_idx], self.arr[1]
        top_value: int = self.arr.pop()
        
        top_idx: int = 1
        upper_bound: int = last_idx - 1
        while True:
            left_child_idx: int = top_idx << 1
            if left_child_idx > upper_bound: break
            right_child_idx: int = left_child_idx + 1
            child_idx: int = left_child_idx
            if right_child_idx <= upper_bound and self.arr[right_child_idx] > self.arr[child_idx]:
                child_idx = right_child_idx
            if self.arr[top_idx] >= self.arr[child_idx]: break
            self.arr[top_idx], self.arr[child_idx] = self.arr[child_idx], self.arr[top_idx]
            top_idx = child_idx
        return top_value
        
        
def solution() -> None:
    """
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline().rstrip())
    max_heap: MaxHeap = MaxHeap()
    for _ in range(n):
        command, *args = sys.stdin.readline().rstrip().split()
        if command == '0':
            max_heap.insert(int(args[0]))
        else: sys.stdout.write('{}\n'.format(max_heap.extract()))
        
        
if __name__ == '__main__':
    solution()