#include <iostream>
#include <vector>
#include <unordered_map>

bool isBipartite(int source, std::unordered_map<int, std::vector<int>>& adjList, std::vector<int>& colors) {
    std::vector<int> callStack = {source};
    while (!callStack.empty()) {
        int vertex = callStack.back();
        callStack.pop_back();
        for (int neighbor : adjList[vertex]) {
            if (colors[neighbor] == colors[vertex]) return false;
            else if (colors[neighbor] != -1) continue;
            colors[neighbor] = (colors[vertex] + 1) % 2;
            callStack.push_back(neighbor);
        }
    }
    return true;
}

void solution() {
    /*
    Time Complexity O(V + E)
    Memory Complexity O(V + E)
    */
    int n, m;
    std::cin >> n >> m;
    std::unordered_map<int, std::vector<int>> adjList;
    for (int i = 0; i < m; ++i) {
        int u, v;
        std::cin >> u >> v;
        adjList[u].push_back(v);
        adjList[v].push_back(u);
    }
    std::vector<int> colors (n + 1, -1);
    for (int vertex = 1; vertex <= n; ++vertex) {
        if (colors[vertex] != -1) continue;
        colors[vertex] = 0;
        if (!isBipartite(vertex, adjList, colors)) {
            std::cout << "NO\n";
            return;
        }
    }
    std::cout << "YES\n";
}


int main() {
    solution();
}