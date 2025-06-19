#include <iostream>
#include <vector>
#include <unordered_set>
#include <cmath>


void solution() {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    */
    int n;
    std::scanf("%d", &n);
    std::vector<int> primeNumbers;
    std::vector<bool> sieve(n + 1, false);
    for (int d = 2; d <= n; ++d) {
        if (!sieve[d]) {
            primeNumbers.push_back(d);
            for (int nextD = d; nextD <= n; nextD += d) sieve[nextD] = true;
        }
    }
    std::unordered_set<int> seen;
    int x = -1, y = -1;
    for (int prime : primeNumbers) {
        seen.insert(prime);
        if (seen.count(n - prime)) {
            x = n - prime, y = prime;
        }
    }
    std::printf("%d %d\n", x, y);
}


int main() {
    solution();
}