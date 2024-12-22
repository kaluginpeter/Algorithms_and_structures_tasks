#include <iostream>
#include <unordered_map>
#include <vector>


void solution(int& n, std::vector<int>& points) {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    std::unordered_map<int, int> hashmap;
    hashmap[0] = 0;
    int maxSub = 0;
    int cumSum = 0;
    for (int idx = 0; idx < n; ++idx) {
        if (points[idx]) {
            ++cumSum;
        } else {
            --cumSum;
        }
        if (cumSum == 0) {
            maxSub = std::max(maxSub, idx + 1);
        }
        if (hashmap.count(cumSum)) {
            maxSub = std::max(maxSub, idx - hashmap[cumSum]);
        } else {
            hashmap[cumSum] = idx;
        }
    }
    std::cout << maxSub << "\n";
}


int main() {
    int n;
    std::cin >> n;
    std::vector<int> points;
    for (int i = 0; i < n; ++i) {
        int point;
        std::cin >> point;
        points.push_back(point);
    }
    solution(n, points);
}