#include <iostream>
#include <vector>
#include <unordered_map>


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
    int source, destination;
    std::cin >> source >> destination;
    std::vector<bool> seen (n + 1, false);
    std::vector<int> curNodes = {source};
    seen[source] = true;
    std::vector<int> nextNodes;
    int edges = 0;
    while (!curNodes.empty()) {
        for (int& node : curNodes) {
            if (node == destination) {
                std::cout << edges << "\n";
                return;
            }
            for (int& neighbor : adjList[node]) {
                if (!seen[neighbor]) {
                    nextNodes.push_back(neighbor);
                    seen[neighbor] = true;
                }
            }
        }
        ++edges;
        curNodes = nextNodes;
        nextNodes = {};
    }
    std::cout << "-1\n";
}


int main() {
    solution();
}