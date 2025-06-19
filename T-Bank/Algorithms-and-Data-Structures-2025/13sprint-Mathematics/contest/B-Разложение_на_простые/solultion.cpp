#include <iostream>
#include <vector>
#include <cmath>


void solution() {
    /*
    Time Complexity O(sqrtN)
    Memory Complexity O(sqrtN)
    */
    int n;
    std::scanf("%d", &n);
    std::vector<std::pair<int, int>> output;
    int amount = 0;
    while (n % 2 == 0) {
        ++amount;
        n /= 2;
    }
    if (amount) output.push_back({2, amount});
    int bound = std::sqrt(n) + 1;
    for (int d = 3; d < bound; d += 2) {
        int amount = 0;
        while (n % d == 0) {
            ++amount;
            n /= d;
        }
        if (amount) output.push_back({d, amount});
    }
    if (n > 2) output.push_back({n, 1});
    for (int i = 0; i < output.size(); ++i) {
        if (output[i].second != 1) std::printf("%d^%d", output[i].first, output[i].second);
        else std::printf("%d", output[i].first);
        if (i + 1 != output.size()) std::printf("*");
    }
    std::printf("\n");
    
    
}


int main() {
    solution();
}