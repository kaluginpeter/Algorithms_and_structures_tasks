#include <iostream>
#include <vector>
#include <algorithm>


void solution(int& n, int& k, std::vector<int>& homes) {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(1)
    */
    std::sort(homes.begin(), homes.end());
    int purchased = 0;
    for (int& home : homes) {
        if (k - home < 0) {
            break;
        }
        k -= home;
        ++purchased;
    }
    std::cout << purchased << "\n";
}


int main() {
    int n, k;
    std::cin >> n >> k;
    std::vector<int> homes;
    for (int i = 0; i < n; ++i) {
        int home;
        std::cin >> home;
        homes.push_back(home);
    }
    solution(n, k, homes);
}