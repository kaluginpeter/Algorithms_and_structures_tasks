# There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.
#
# You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.
#
# The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.
#
# Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.
#
#
#
# Example 1:
#
# Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
# Output: 0.78333
# Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.
# Example 2:
#
# Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
# Output: 0.53485
#
#
# Constraints:
#
# 1 <= classes.length <= 105
# classes[i].length == 2
# 1 <= passi <= totali <= 105
# 1 <= extraStudents <= 105
# Solution
# Python O(NlogN + MlogN) O(N) Priority Queue
class Solution:
    def get_ratio(self, passed: int, total: int) -> float:
        if passed == total: return 0
        return (passed + 1) / (total + 1) - passed / total

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        min_heap: list[list[float, int, int]] = []
        for exam in classes:
            passed, total = exam
            heapq.heappush(min_heap, (-self.get_ratio(passed, total), passed, total))
        while extraStudents:
            ratio, passed, total = heapq.heappop(min_heap)
            passed, total = passed + 1, total + 1
            heapq.heappush(min_heap, (-self.get_ratio(passed, total), passed, total))
            extraStudents -= 1
        return sum(exam[1] / exam[2] for exam in min_heap) / len(classes)

# C++ O(NlogN + MlogN) O(N) Priority Queue
class Solution {
public:
    double getRatio(int& passed, int& total) {
        if (passed == total) {
            return 0;
        }
        double dP = static_cast<double>(passed);
        double dT = static_cast<double>(total);
        return (dP + 1) / (dT + 1) - dP / dT;
    }

    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        std::priority_queue<std::tuple<double, int, int>, std::vector<std::tuple<double, int, int>>> maxHeap;
        for (std::vector<int>& exam : classes) {
            int& passed = exam[0];
            int& total = exam[1];
            maxHeap.push({getRatio(passed, total), passed, total});
        }
        while (extraStudents) {
            auto [ratio, passed, total] = maxHeap.top();
            maxHeap.pop();
            ++passed;
            ++total;
            maxHeap.push({getRatio(passed, total), passed, total});
            --extraStudents;
        }
        double averageRatio = 0;
        while (maxHeap.size()) {
            auto [ratio, passed, total] = maxHeap.top();
            averageRatio += static_cast<double>(passed) / static_cast<double>(total);
            maxHeap.pop();
        }
        return averageRatio / static_cast<double>(classes.size());
    }
};


# Python O(NlogN + KlogN) O(N) PriorityQueue
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        output: float = 0.0
        min_heap: list[tuple[float, int, int]] = []
        for pass_, total in classes:
            if pass_ == total:
                output += 1
                continue
            first: float = pass_ / total
            second: float = (pass_ + 1) / (total + 1) - first
            heapq.heappush(min_heap, (-second, pass_, total))
        while extraStudents and min_heap:
            _, pass_, total = heapq.heappop(min_heap)
            pass_ += 1
            total += 1
            first: float = pass_ / total
            second: float = (pass_ + 1) / (total + 1) - first
            heapq.heappush(min_heap, (-second, pass_, total))
            extraStudents -= 1
        while min_heap:
            _, pass_, total = heapq.heappop(min_heap)
            output += pass_ / total
        return output / len(classes)

# C++ O(NlogN + KlogN) O(N) PriorityQueue
class Solution {
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        std::priority_queue<std::tuple<double, int, int>, std::vector<std::tuple<double, int, int>>, std::greater<std::tuple<double, int, int>>> minHeap;
        double output = 0.0;
        for (const std::vector<int> &class_ : classes) {
            if (class_[0] == class_[1]) {
                output += 1;
                continue;
            }
            double first = static_cast<double>(class_[0]) / class_[1];
            double second = static_cast<double>(class_[0] + 1) / (class_[1] + 1) - first;
            minHeap.push(std::make_tuple(-second, class_[0], class_[1]));
        }
        while (extraStudents  && !minHeap.empty()) {
            std::tuple<double, int, int> cls = minHeap.top();
            minHeap.pop();
            int pass = std::get<1>(cls) + 1, total = std::get<2>(cls) + 1;
            double first = static_cast<double>(pass) / total;
            double second = static_cast<double>(pass + 1) / (total + 1) - first;
            minHeap.push(std::make_tuple(-second, pass, total));
            --extraStudents;
        }

        while (!minHeap.empty()) {
            output += static_cast<double>(std::get<1>(minHeap.top())) / std::get<2>(minHeap.top());
            minHeap.pop();
        }
        return output / classes.size();
    }
};