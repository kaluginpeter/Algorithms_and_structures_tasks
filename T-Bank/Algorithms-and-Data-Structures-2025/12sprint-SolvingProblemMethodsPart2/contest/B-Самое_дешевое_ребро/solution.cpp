#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;


void dfs(
    int v, int p, int d, int edgeWeight,
    vector<vector<pair<int, int>>> &adjList,
    vector<vector<int>> &dp,
    vector<vector<int>> &minEdge,
    vector<int> &depth
) {
    dp[v][0] = p;
    minEdge[v][0] = edgeWeight;
    depth[v] = d;
    for (auto &edge : adjList[v]) {
        int u = edge.first;
        int w = edge.second;
        if (u != p) {
            dfs(u, v, d + 1, w, adjList, dp, minEdge, depth);
        }
    }
}

void preprocess(
    int n,
    vector<int> &depth,
    vector<vector<int>> &dp,
    vector<vector<int>> &minEdge,
    vector<vector<pair<int, int>>> &adjList
) {
    dfs(0, -1, 0, INT_MAX, adjList, dp, minEdge, depth);
    for (int j = 1; j < 31; j++) {
        for (int v = 0; v < n; v++) {
            if (dp[v][j - 1] != -1) {
                dp[v][j] = dp[dp[v][j - 1]][j - 1];
                minEdge[v][j] = min(minEdge[v][j - 1], minEdge[dp[v][j - 1]][j - 1]);
            }
        }
    }
}

int lca(int u, int v, vector<int> &depth, vector<vector<int>> &dp) {
    if (depth[u] < depth[v]) swap(u, v);
    for (int j = 30; j >= 0; --j) {
        if (depth[u] - (1 << j) >= depth[v]) u = dp[u][j];
    }
    if (u == v) return u;
    for (int j = 30; j >= 0; --j) {
        if (dp[u][j] != dp[v][j]) {
            u = dp[u][j];
            v = dp[v][j];
        }
    }
    return dp[u][0];
}

int getMinEdge(
    int u, int l,
    vector<int> &depth,
    vector<vector<int>> &minEdge,
    vector<vector<int>> &dp
) {
    int minW = INT_MAX;
    for (int j = 30; j >= 0; --j) {
        if (depth[u] - (1 << j) >= depth[l]) {
            minW = min(minW, minEdge[u][j]);
            u = dp[u][j];
        }
    }
    return minW;
}

void solution() {
    /*
    Time Complexity O(NlogN + MlogN)
    Memory Complexity O(N)
    */
    int n;
    scanf("%d", &n);
    vector<vector<pair<int, int>>> adjList(n);
    for (int i = 1; i < n; i++) {
        int x, y;
        scanf("%d %d", &x, &y);
        adjList[x].emplace_back(i, y);
    }
    vector<int> depth(n);
    vector<vector<int>> dp(n, vector<int>(31, -1));
    vector<vector<int>> minEdge(n, vector<int>(31, INT_MAX));
    preprocess(n, depth, dp, minEdge, adjList);
    int m;
    scanf("%d", &m);
    for (int i = 0; i < m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        int ancestor = lca(u, v, depth, dp);
        int minU = getMinEdge(u, ancestor, depth, minEdge, dp);
        int minV = getMinEdge(v, ancestor, depth, minEdge, dp);
        printf("%d\n", min(minU, minV));
    }
}

int main() {
    solution();
}