#include <iostream>
#include <vector>
#include <algorithm>


void solution(int& n, std::vector<std::pair<int, int>>& pairs) {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(1)
    */
    std::sort(pairs.begin(), pairs.end());
    int mainIdx = 0;
    int currentIdx = 0;
    for (int idx = 0; idx < n; ++idx) {
        if (pairs[currentIdx].second >= pairs[idx].first) {
            pairs[currentIdx].second = std::max(pairs[currentIdx].second, pairs[idx].second);
        } else {
            pairs[mainIdx] = pairs[currentIdx];
            currentIdx = idx;
            ++mainIdx;
        }
    }
    pairs[mainIdx] = pairs[currentIdx];
    ++mainIdx;
    for (int idx = 0; idx < mainIdx; ++idx) {
        std::cout << pairs[idx].first << " " << pairs[idx].second << "\n";
    }
}


int main() {
    int n;
    std::cin >> n;
    std::vector<std::pair<int, int>> pairs;
    for (int i = 0; i < n; ++i) {
        int start, end;
        std::cin >> start >> end;
        pairs.push_back({start, end});
    }
    solution(n, pairs);
}