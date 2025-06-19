#include <iostream>
#include <vector>
#include <stack>

void solution() {
    /*
    Time Complexity O(|V| + |E|)
    Memory Complexity O(|V| + |E|)
    */
    int n, m;
    std::scanf("%d %d", &n, &m);
    std::vector<std::vector<int>> adjList(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        std::scanf("%d %d", &u, &v);
        adjList[u].push_back(v);
    }
    std::vector<int> order(n);
    for (int i = 0; i < n; ++i) std::scanf("%d", &order[i]);
    std::vector<int> position(n + 1);
    for (int i = 0; i < n; ++i) position[order[i]] = i;
    for (int u = 1; u <= n; ++u) {
        for (int v : adjList[u]) {
            if (position[u] > position[v]) {
                std::printf("NO\n");
                return;
            }
        }
    }

    std::printf("YES\n");
}

int main() {
    solution();
    return 0;
}