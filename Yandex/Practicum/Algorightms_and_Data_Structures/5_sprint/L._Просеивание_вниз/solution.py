def sift_down(heap, idx) -> int:
    """
    Time Complexity O(H) -> O(logN)
    Memory Complexity O(H) -> O(logN)
    """
    upper_bound: int = len(heap) - 1
    left_idx: int = idx * 2
    right_idx: int = idx * 2 + 1
    if left_idx > upper_bound:
        return idx
    largest_idx: int = left_idx
    if right_idx <= upper_bound and heap[left_idx] < heap[right_idx]:
        largest_idx = right_idx
    if heap[idx] < heap[largest_idx]:
        heap[idx], heap[largest_idx] = heap[largest_idx], heap[idx]
        return sift_down(heap, largest_idx)
    return idx


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5


if __name__ == '__main__':
    test()