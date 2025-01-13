def sift_up(heap, idx) -> int:
    """
    Time Complexity O(H) -> O(logN)
    Memory Complexity O(H) -> O(logN)
    """
    if idx == 1:
        return idx
    parent_idx: int = idx // 2
    if heap[idx] > heap[parent_idx]:
        heap[idx], heap[parent_idx] = heap[parent_idx], heap[idx]
        return sift_up(heap, parent_idx)
    return idx


def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1


if __name__ == '__main__':
    test()