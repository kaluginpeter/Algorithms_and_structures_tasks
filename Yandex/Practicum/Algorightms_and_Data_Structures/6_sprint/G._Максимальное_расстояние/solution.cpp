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
        int source, destination;
        std::cin >> source >> destination;
        adjList[source].push_back(destination);
        adjList[destination].push_back(source);
    }
    int source;
    std::cin >> source;
    std::vector<int> colors (n + 1, -1);
    colors[source] = 1;
    std::vector<int> curNodes = {source};
    std::vector<int> nextNodes;
    int distance = -1;
    while (!curNodes.empty()) {
        for (int& node : curNodes) {
            for (int& neighbor : adjList[node]) {
                if (colors[neighbor] == -1) {
                    colors[neighbor] = 1;
                    nextNodes.push_back(neighbor);
                }
            }
        }
        curNodes = nextNodes;
        nextNodes = {};
        ++distance;
    }
    std::cout << distance << "\n";
}


int main() {
    solution();
}