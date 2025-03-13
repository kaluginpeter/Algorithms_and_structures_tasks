#include <iostream>
#include <vector>
#include <cstdint>
#include <algorithm>


using namespace std;

void solution() {
    /*
    Time Complexity O(N**2)
    Memory Complexity O(N**2)
    */
    int n;
    scanf("%d", &n);
    vector<int> prices (n, 0);
    for (int i = 0; i <= n; ++i) scanf("%d", &prices[i]);
    vector<vector<int>> dp (n + 1, vector<int>(n + 2, INT32_MAX - 10000001));
    dp[0][0] = 0;
    for (int day = 1; day <= n; ++day) {
        for (int ticket = 0; ticket <= day; ++ticket) {
            if (prices[day - 1] > 500) {
                dp[day][ticket] = dp[day - 1][ticket + 1];
                if (ticket) dp[day][ticket] = min(dp[day][ticket], dp[day - 1][ticket - 1] + prices[day - 1]);
            } else dp[day][ticket] = min(dp[day - 1][ticket] + prices[day - 1], dp[day - 1][ticket + 1]);
        }
    }
    int minPrice = INT32_MAX;
    int ticket = 0;
    for (int chosenTicket = 0; chosenTicket <= n; ++chosenTicket) {
        if (dp[n][chosenTicket] < minPrice) {
            minPrice = dp[n][chosenTicket];
            ticket = chosenTicket;
        }
    }
    int lastPrice = minPrice;
    vector<int> days;
    for (int day = n - 1; day >= 0; --day) {
        if (dp[day][ticket + 1] == lastPrice) {
            days.push_back(day + 1);
            ++ticket;
        } else {
            if (prices[day] > 500) --ticket;
            lastPrice -= prices[day];
        }
    }
    reverse(days.begin(), days.end());
    printf("%d %d\n", minPrice, days.size());
    for (int& day : days) printf("%d ", day);
    if (!days.empty()) printf("\n");
}


int main() {
    solution();
}