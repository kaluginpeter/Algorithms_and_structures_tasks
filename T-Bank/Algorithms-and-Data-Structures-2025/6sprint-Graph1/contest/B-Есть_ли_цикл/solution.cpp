#include <iostream>
#include <vector>


bool dfs(int& start, std::vector<std::vector<int>>& adjList, std::vector<int>& colors) {
    std::vector<int> queue = {start};
    while (!queue.empty()) {
        int vertex = queue.back();
        queue.pop_back();
        if (!colors[vertex]) {
            colors[vertex] = 1;
            queue.push_back(vertex);
            for (int neighbor : adjList[vertex]) {
                if (colors[neighbor] == 1) return true;
                if (!colors[neighbor]) queue.push_back(neighbor);
            }
        } else colors[vertex] = 2;
    }
    return false;
}


void solution() {
    /*
    Time Complexity O(|V| + |E|)
    Memory Complexity O(|V| + |E|)
    */
    int n, m;
    std::scanf("%d %d", &n, &m);
    std::vector<std::vector<int>> adjList (n + 1, std::vector<int>());
    for (int i = 0; i < m; ++i) {
        int u, v;
        std::scanf("%d %d", &u, &v);
        adjList[u].push_back(v);
    }
    std::vector<int> colors (n + 1, 0);
    bool hasCycle = false;
    for (int vertex = 1; vertex <= n; ++vertex) {
        if (!colors[vertex]) {
            hasCycle = hasCycle || dfs(vertex, adjList, colors);
        }
    }
    std::printf("%d\n", (hasCycle? 1 : 0));
}


int main() {
    solution();
}