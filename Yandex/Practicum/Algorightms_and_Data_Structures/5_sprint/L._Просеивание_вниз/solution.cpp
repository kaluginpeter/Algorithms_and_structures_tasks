#include <vector>
#include <cassert>
#ifdef REMOTE_JUDGE
#include "solution.h"
#endif


int siftDown(std::vector<int>& heap, int idx) {
    /*
    Time Complexity O(H) -> O(logN)
    Memory Complexity O(H) -> O(logN)
    */
    int upperBound = heap.size() - 1;
    int leftIdx = idx * 2;
    int rightIdx = idx * 2 + 1;
    if (leftIdx > upperBound) return idx;
    int largestIdx = leftIdx;
    if (rightIdx <= upperBound && heap[leftIdx] < heap[rightIdx]) {
        largestIdx = rightIdx;
    }
    if (heap[idx] < heap[largestIdx]) {
        std::swap(heap[idx], heap[largestIdx]);
        return siftDown(heap, largestIdx);
    }
    return idx;
}

#ifndef REMOTE_JUDGE
void test() {
    std::vector<int> sample = {-1, 12, 1, 8, 3, 4, 7};
    assert(siftDown(sample, 2) == 5);
}


int main() {
    test();
}
#endif