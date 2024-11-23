#include <iostream>
#include <cmath>

int solution(long long n, long long k) {
    /*
    Time Complexity O(N)
    Memory Complexity O(1)
    */
    long long bound = std::pow(10, k);
    long long x = 1, y = 1;
    for (int i = 1; i < n; ++i) {
        long long c = y;
        y = (x % bound + y % bound) % bound;
        x = c;
    }
    return y;
}

int main() {
    long long n, k;
    std::cin >> n >> k;
    std::cout << solution(n, k) << "\n";
}