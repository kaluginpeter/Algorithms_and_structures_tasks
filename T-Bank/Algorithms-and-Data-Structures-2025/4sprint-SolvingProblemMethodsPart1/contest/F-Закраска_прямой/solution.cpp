#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdint>


void solution() {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(1)
    */
    int n;
    std::scanf("%d", &n);
    std::vector<std::pair<int, int>> segments;
    for (int i = 0; i < n; ++i) {
        int start, end;
        std::scanf("%d %d", &start, &end);
        segments.push_back({start, end});
    }
    std::sort(segments.begin(), segments.end());
    long long output = 0;
    int prevStart = INT32_MIN, prevEnd = INT32_MIN;
    for (std::pair<int, int>& segment : segments) {
        if (segment.first <= prevEnd) prevEnd = std::max(prevEnd, segment.second);
        else {
            output += (long long)prevEnd - (long long)prevStart;
            prevStart = segment.first;
            prevEnd = segment.second;
        }
    }
    output += (long long)prevEnd - (long long)prevStart;
    std::printf("%lld\n", output);
}


int main() {
    solution();
}