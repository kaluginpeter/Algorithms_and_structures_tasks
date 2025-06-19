#include <iostream>
#include <queue>
#include <vector>
#include <climits>

using namespace std;

void solution() {
    /*
    Time Complexity O(k)
    Memory Complexity O(k)
    */
    long long k;
    scanf("%lld", &k);
    vector<long long> minSum(k, LLONG_MAX);
    priority_queue<pair<long long, long long>, vector<pair<long long, long long>>, greater<pair<long long, long long>>> pq;
    for (long long num = 1; num < 10; ++num) {
        long long remainder = num % k;
        if (num < minSum[remainder]) {
            minSum[remainder] = num;
            pq.push({num, remainder});
        }
    }

    while (!pq.empty()) {
        long long currentSum = pq.top().first;
        long long currentRemainder = pq.top().second;
        pq.pop();
        if (currentRemainder == 0) {
            printf("%lld\n", currentSum);
            return;
        }
        for (long long digit = 0; digit < 10; ++digit) {
            long long newSum = currentSum + digit;
            long long newRemainder = (currentRemainder * 10 + digit) % k;
            if (newSum < minSum[newRemainder]) {
                minSum[newRemainder] = newSum;
                pq.push({newSum, newRemainder});
            }
        }
    }
}

int main() {
    solution();
}