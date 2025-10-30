/*
Given any number of arrays each sorted in ascending order, find the nth smallest number of all their elements.

All the arguments except the last will be arrays, the last argument is n.

nthSmallest([1,5], [2], [4,8,9], 4) // returns 5 because it's the 4th smallest value
Be mindful of performance.

ArraysAlgorithmsPerformance
*/
// Solution
#include <vector>
#include <queue>

int nthSmallest(const std::vector<std::vector<int>>& arr, int n) {
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
    for (const std::vector<int>& v : arr) {
        for (const int& num : v) minHeap.push(num);
    }
    for (int i = 0; i < n - 1; ++i) minHeap.pop();
    return minHeap.top();
}