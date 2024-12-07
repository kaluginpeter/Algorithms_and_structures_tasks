#include <iostream>
#include <vector>
#include <algorithm>


void solution(int& n, std::vector<int>& greedy, int& m, std::vector<int>& cookies) {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(1)
    */
    int happy = 0;
    std::sort(greedy.begin(), greedy.end());
    std::sort(cookies.begin(), cookies.end());
    int cookiesIdx = 0;
    for (int gred : greedy) {
        while (cookiesIdx < m && cookies[cookiesIdx] < gred) {
            ++cookiesIdx;
        }
        if (cookiesIdx < m) {
            ++happy;
            ++cookiesIdx;
        } else {
            break;
        }
    }
    std::cout << happy << "\n";
}


int main() {
    int n;
    std::cin >> n;
    std::vector<int> greedy;
    for (int i = 0; i < n; ++i) {
        int gred;
        std::cin >> gred;
        greedy.push_back(gred);
    }
    int m;
    std::cin >> m;
    std::vector<int> cookies;
    for (int i = 0; i < m; ++i) {
        int cookie;
        std::cin >> cookie;
        cookies.push_back(cookie);
    }
    solution(n, greedy, m, cookies);
}