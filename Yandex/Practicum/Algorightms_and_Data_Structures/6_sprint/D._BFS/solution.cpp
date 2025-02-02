#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>


void solution() {
    /*
    Time Complexity O(V + E)
    Memory Complexity O(V + E)
    */
    int n, m;
    std::cin >> n >> m;
    std::unordered_map<int, std::vector<int>> adjList;
    for (int i = 0; i < m; ++i) {
        int source, destination;
        std::cin >> source >> destination;
        adjList[source].push_back(destination);
        adjList[destination].push_back(source);
    }
    int source;
    std::cin >> source;
    for (auto& pair : adjList) {
        std::sort(pair.second.begin(), pair.second.end());
    }
    std::vector<int> colors (n + 1, -1);
    colors[source] = 1;
    std::vector<int> curNodes = {source};
    std::vector<int> nextNodes;
    while (!curNodes.empty()) {
        for (int& node : curNodes) {
            std::cout << node << " ";
            for (int& neighbor : adjList[node]) {
                if (colors[neighbor] == -1) {
                    colors[neighbor] = 1;
                    nextNodes.push_back(neighbor);
                }
            }
        }
        curNodes = nextNodes;
        nextNodes = {};
    }
}


int main() {
    solution();
}