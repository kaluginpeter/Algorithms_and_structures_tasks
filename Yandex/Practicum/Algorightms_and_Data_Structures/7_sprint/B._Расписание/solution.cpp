#include <iostream>
#include <algorithm>
#include <vector>


void solution() {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(1)
    */
    int n;
    std::cin >> n;
    std::vector<std::tuple<double, double>> events;
    for (int i = 0; i < n; ++i) {
        double start, end;
        std::cin >> start >> end;
        events.push_back({start, end});
    }
    std::sort(
        events.begin(), events.end(),
        [](const auto& x, const auto& y) {
            if (std::get<1>(x) != std::get<1>(y)) return std::get<1>(x) < std::get<1>(y);
            return std::get<0>(x) < std::get<0>(y);
    });
    int passed = 0;
    std::vector<std::tuple<double, double>> output;
    double curEnd = -1;
    for (std::tuple<double, double>& p : events) {
        if (std::get<0>(p) >= curEnd) {
            ++passed;
            output.push_back(p);
            curEnd = std::get<1>(p);
        }
    }
    std::cout << passed << "\n";
    for (int i = 0; i < passed; ++i) {
        double x = std::get<0>(output[i]);
        double y = std::get<1>(output[i]);
        std::cout << ((int)x == x? (int)x : x) << " " << ((int)y == y? (int)y : y) << "\n";
    }
}


int main() {
    solution();
}