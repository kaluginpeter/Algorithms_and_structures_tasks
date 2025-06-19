#include <iostream>
#include <vector>
#include <climits>

using namespace std;


void solution() {
    /*
    Time Complexity O(2^M)
    Memory Complexity O(M)
    */
    int N, M;
    scanf("%d %d", &N, &M);
    vector<int> coins(M);
    for (int i = 0; i < M; ++i) scanf("%d", &coins[i]);
    int min_coins = INT_MAX;
    vector<int> best_combination;
    for (int mask = 0; mask < (1 << (2 * M)); ++mask) {
        int total = 0;
        int count = 0;
        vector<int> current;
        bool valid = true;
        for (int i = 0; i < M; ++i) {
            int bits = (mask >> (2 * i)) & 0x3;
            if (bits > 2) {
                valid = false;
                break;
            }
            total += bits * coins[i];
            count += bits;
            for (int j = 0; j < bits; ++j) current.push_back(coins[i]);
        }
        if (valid && total == N) {
            if (count < min_coins) {
                min_coins = count;
                best_combination = current;
            }
        }
    }

    if (min_coins != INT_MAX) {
        printf("%d\n", min_coins);
        for (int coin : best_combination) printf("%d ", coin);
        printf("\n");
    } else {
        int totalMoney = 0;
        for (int coin : coins) totalMoney += 2 * coin;
        printf("%d\n", (totalMoney < N? -1 : 0));
    }
}


int main() {
    solution();
}