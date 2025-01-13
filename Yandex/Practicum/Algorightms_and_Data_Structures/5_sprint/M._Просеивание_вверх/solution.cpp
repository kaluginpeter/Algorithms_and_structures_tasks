#include <vector>
#include <cassert>
#ifdef REMOTE_JUDGE
#include "solution.h"
#endif


int siftUp(std::vector<int>& heap, int idx) {
    /*
    Time Complexity O(H) -> O(logN)
    Memory Complexity O(H) -> O(logN)
    */
    if (idx == 1) return idx;
    int parentIdx = idx / 2;
    if (heap[parentIdx] < heap[idx]) {
        std::swap(heap[parentIdx], heap[idx]);
        return siftUp(heap, parentIdx);
    }
    return idx;
}

#ifndef REMOTE_JUDGE
void test() {
    std::vector<int> sample = {-1, 12, 6, 8, 3, 15, 7};
    assert(siftUp(sample, 5) == 1);
}


int main() {
    test();
}
#endif