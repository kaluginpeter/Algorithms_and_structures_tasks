#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>


bool compareSegments(const std::tuple<long long, long long, int>& x, const std::tuple<long long, long long, int>& y) {
    if (std::get<1>(x) != std::get<1>(y)) return std::get<1>(x) < std::get<1>(y);
    return std::get<0>(x) < std::get<0>(y);
}


void solution() {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(1)
    */
    int n, c;
    std::scanf("%d %d", &n, &c);
    std::vector<std::tuple<long long, long long, int>> segments;
    for (int i = 1; i <= n; ++i) {
        long long start, duration;
        std::scanf("%lld %lld", &start, &duration);
        segments.push_back({start, start + duration, i});
    }
    std::sort(segments.begin(), segments.end(), compareSegments);
    std::vector<int> path;
    long long outcome = 0;
    long long prevEnd = 0;
    int taskId = 0;
    for (std::tuple<long long, long long, int>& segment : segments) {
        if (std::get<0>(segment) >= prevEnd) {
            if (prevEnd) {
                path.push_back(taskId);
                outcome += (long long)c;
            }
            prevEnd = std::get<1>(segment);
            taskId = std::get<2>(segment);
        }
    }
    outcome += c;
    path.push_back(taskId);
    std::printf("%lld\n%d\n", outcome, (int)path.size());
    for (int i = 0; i < path.size(); ++i) {
        if (i) std::printf(" ");
        std::printf("%d", path[i]);
    }
    if (!path.empty()) std::printf("\n");
}


int main() {
    solution();
}