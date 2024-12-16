# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
#
# Implement the SmallestInfiniteSet class:
#
# SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
# int popSmallest() Removes and returns the smallest integer contained in the infinite set.
# void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
#
#
# Example 1:
#
# Input
# ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
# [[], [2], [], [], [], [1], [], [], []]
# Output
# [null, null, 1, 2, 3, null, 1, 4, 5]
#
# Explanation
# SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
# smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
# smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
# smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
# smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
#                                    // is the smallest number, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.
#
#
# Constraints:
#
# 1 <= num <= 1000
# At most 1000 calls will be made in total to popSmallest and addBack.
# Solution
# Python O(logN) O(N) Priority Queue HashSet
class SmallestInfiniteSet:

    def __init__(self):
        self.current_number: int = 1
        self.min_heap: list[int] = []
        self.added_back: set[int] = set()

    def popSmallest(self) -> int:
        output: int = 0
        if not self.min_heap or self.min_heap[0] > self.current_number:
            output = self.current_number
            self.current_number += 1
        else:
            self.added_back.remove(self.min_heap[0])
            output = heapq.heappop(self.min_heap)
        return output

    def addBack(self, num: int) -> None:
        if num < self.current_number and num not in self.added_back:
            heapq.heappush(self.min_heap, num)
            self.added_back.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

# C++ O(logN) O(N) Priority Queue HashSet
class SmallestInfiniteSet {
public:
    int currentNumber = 1;
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
    std::unordered_set<int> addedBack;
    SmallestInfiniteSet() {};

    int popSmallest() {
        int output = 0;
        if (minHeap.empty() || minHeap.top() > currentNumber) {
            output = currentNumber++;
        } else {
            output = minHeap.top();
            addedBack.erase(minHeap.top());
            minHeap.pop();
        }
        return output;
    }

    void addBack(int num) {
        if (num < currentNumber && addedBack.find(num) == addedBack.end()) {
            minHeap.push(num);
            addedBack.insert(num);
        }
    }
};

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet* obj = new SmallestInfiniteSet();
 * int param_1 = obj->popSmallest();
 * obj->addBack(num);
 */