#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


void solution() {
    /*
    Time Complexity O(N**3)
    Memory Complexity O(N**2)
    */
    int n, m;
    scanf("%d %d ", &n, &m);
    vector<vector<long long>> grid (n + 1, vector<long long>(n + 1, 1e14));
    for (int town = 1; town <= n; ++town) grid[town][town] = 0;
    for (int i = 0; i < m; ++i)  {
        long long source, destination, weight;
        scanf("%lld %lld %lld", &source, &destination, &weight);
        grid[source][destination] = min(grid[source][destination], weight);
        grid[destination][source] = min(grid[destination][source], weight);
    }
    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j]);
            }
        }
    }
    int startTown = 0;
    long long maxDistance = 10e14;
    for (int town = 1; town <= n; ++town) {
        long long curMaxDistance = 0;
        for (int i = 1; i <= n; ++i) {
            if (curMaxDistance < grid[town][i]) {
                curMaxDistance = grid[town][i];
            }
        }
        if (curMaxDistance < maxDistance) {
            startTown = town;
            maxDistance = curMaxDistance;
        }
    }
    printf("%d\n", startTown);
}


int main() {
    solution();
}