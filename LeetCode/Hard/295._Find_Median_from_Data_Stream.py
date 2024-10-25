# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
#
# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:
#
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
#
#
# Example 1:
#
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]
#
# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
#
#
# Constraints:
#
# -105 <= num <= 105
# There will be at least one element in the data structure before calling findMedian.
# At most 5 * 104 calls will be made to addNum and findMedian.
#
#
# Follow up:
#
# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# Solution
# Python O(logN) for AddNumber and O(1) for findMedian Heap
class MedianFinder:

    def __init__(self):
        self.small: list[int] = []
        self.large: list[int] = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        if self.small and self.large and -1 * self.small[0] > self.large[0]:
            heapq.heappop(self.small)
            heapq.heappush(self.large, num)
        if len(self.small) > len(self.large) + 1:
            num: int = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, num)
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -1 * heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# C++ O(logN) for addNum and O(1) for findMedian Heaps
class MedianFinder {
public:
    std::priority_queue<int, std::vector<int>> small;
    std::priority_queue<int, std::vector<int>, std::greater<int>> large;
    MedianFinder() {};

    void addNum(int num) {
        small.push(num);
        if (small.size() && large.size() && small.top() > large.top()) {
            large.push(small.top());
            small.pop();
        }
        if (small.size() > large.size() + 1) {
            large.push(small.top());
            small.pop();
        }
        if (large.size() > small.size() + 1) {
            small.push(large.top());
            large.pop();
        }
    }

    double findMedian() {
        if (small.size() > large.size()) {
            return small.top();
        }
        if (small.size() < large.size()) {
            return large.top();
        }
        return static_cast<double>(small.top() + large.top()) / 2;
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */