#include <iostream>
#include <unordered_map>

std::unordered_map<int, int> memo;

int solution(int n) {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    if (memo[n]) {
        return memo[n];
    }
    if (n < 2) {
        memo[n] = 1;
        return memo[n];
    }
    memo[n] = solution(n - 1) + solution(n - 2);
    return memo[n];
}

int main() {
    int n;
    std::cin >> n;
    std::cout << solution(n) << "\n";
}