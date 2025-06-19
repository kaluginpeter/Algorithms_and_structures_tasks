#include <iostream>
#include <vector>

void dfs(
    int v,
    std::vector<std::vector<int>> &adjList,
    std::vector<std::vector<int>> &dp,
    std::vector<int> &timeIn,
    std::vector<int> &timeOut,
    int &t
) {
    timeIn[v] = t++;
    for (int u : adjList[v]) {
        dp[u][0] = v;
        dfs(u, adjList, dp, timeIn, timeOut, t);
    }
    timeOut[v] = t++;
}

bool isAncestor(int u, int v, std::vector<int> &timeIn, std::vector<int> &timeOut) {
    return timeIn[u] <= timeIn[v] && timeOut[u] >= timeOut[v];
}

int lca(
    int u, int v,
    std::vector<std::vector<int>> &dp,
    std::vector<int> &timeIn,
    std::vector<int> &timeOut
) {
    if (isAncestor(u, v, timeIn, timeOut)) return u;
    if (isAncestor(v, u, timeIn, timeOut)) return v;
    for (int level = 30; level >= 0; --level) {
        if (!isAncestor(dp[u][level], v, timeIn, timeOut)) {
            u = dp[u][level];
        }
    }
    return dp[u][0];
}

void solution() {
    /*
    Time Complexity O(NlogN + MlogN)
    Memory Complexity O(N)
    */
    int n;
    std::scanf("%d", &n);
    std::vector<std::vector<int>> adjList(n);
    std::vector<std::vector<int>> dp(n, std::vector<int>(31, 0));
    for (int i = 1; i < n; ++i) {
        int parent;
        std::scanf("%d", &parent);
        adjList[parent].push_back(i);
    }
    std::vector<int> timeIn(n), timeOut(n);
    int t = 0;
    dfs(0, adjList, dp, timeIn, timeOut, t);
    for (int v = 0; v < n; ++v) {
        for (int level = 1; level < 31; ++level) {
            dp[v][level] = dp[dp[v][level - 1]][level - 1];
        }
    }
    int m;
    std::scanf("%d", &m);
    for (int i = 0; i < m; ++i) {
        int u, v;
        std::scanf("%d %d", &u, &v);
        std::printf("%d\n", lca(u, v, dp, timeIn, timeOut));
    }
}

int main() {
    solution();
}