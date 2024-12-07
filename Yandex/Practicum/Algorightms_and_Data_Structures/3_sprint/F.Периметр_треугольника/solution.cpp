#include <iostream>
#include <vector>
#include <algorithm>


void solution(int& n, std::vector<int>& stripes) {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(1)
    */
    std::sort(stripes.begin(), stripes.end(), std::greater<int>());
    for (int idx = 0; idx < n; ++idx) {
        if (stripes[idx] < stripes[idx + 1] + stripes[idx + 2]) {
            std::cout << stripes[idx] + stripes[idx + 1] + stripes[idx + 2] << "\n";
            break;
        }
    }
}


int main() {
    int n;
    std::cin >> n;
    std::vector<int> stripes;
    for (int i = 0; i < n; ++i) {
        int stripe;
        std::cin >> stripe;
        stripes.push_back(stripe);
    }
    solution(n, stripes);
}