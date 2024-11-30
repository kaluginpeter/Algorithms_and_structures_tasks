#include <iostream>
#include <vector>

int leftmostBinarySearch(std::vector<int>& days, int bikeCost) {
    int left = 0;
    int right = days.size() - 1;
    bool isFound = false;
    while (left <= right) {
        int middle = left + (right - left) / 2;
        if (days[middle] >= bikeCost) {
            isFound = true;
            right = middle - 1;
        } else {
            left = middle + 1;
        }
    }
    return (isFound? right + 2 : -1);
}

void solution() {
    /*
    Time Complexity O(logN)
    Memory Complexity O(1)
    */
    int n;
    std::cin >> n;
    std::vector<int> days;
    for (int i = 0; i < n; ++i) {
        int day;
        std::cin >> day;
        days.push_back(day);
    }
    int bikeCost;
    std::cin >> bikeCost;
    std::cout << leftmostBinarySearch(days, bikeCost) << " ";
    std::cout << leftmostBinarySearch(days, bikeCost * 2) << "\n";
}

int main() {
    solution();
}