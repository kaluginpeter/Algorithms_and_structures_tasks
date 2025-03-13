#include <iostream>
#include <vector>
#include <deque>

using namespace std;

void solution() {
    /*
    Time Complexity O(VE)
    Memory Complexity O(VE)
    */
    int MOD = 1000000007;
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> adjList (n + 1, vector<int>());
    vector<int> inDegree (n + 1, 0);
    for (int i = 0; i < m; ++i) {
        int u, v;
        scanf("%d %d", &u, &v);
        adjList[u].push_back(v);
        ++inDegree[v];
    }
    deque<int> q;
    for (int vertex = 1; vertex <= n; ++vertex) {
        if (!inDegree[vertex]) q.push_back(vertex);
    }
    vector<int> topologicalOrder;
    while (!q.empty()) {
        int& vertex = q.front();
        q.pop_front();
        topologicalOrder.push_back(vertex);
        for (int& neighbor : adjList[vertex]) {
            --inDegree[neighbor];
            if (!inDegree[neighbor]) q.push_back(neighbor);
        }
    }
    int A, B;
    scanf("%d %d", &A, &B);
    vector<int> dp (n + 1, 0);
    dp[A] = 1;
    for (int& vertex : topologicalOrder) {
        for (int& neighbor : adjList[vertex]) {
            dp[neighbor] = (dp[neighbor] + dp[vertex]) % MOD;
        }
    }
    printf("%d\n", dp[B]);
}


int main() {
    solution();
}