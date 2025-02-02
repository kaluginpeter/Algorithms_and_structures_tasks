#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>


void solution() {
    /*
    Time Complexity O((V + E) + ElogE)
    Memory Complexity O(V + E)
    */
    int v, e;
    std::cin >> v >> e;
    std::unordered_map<int, std::vector<int>> adjList;
    for (int i = 0; i < e; ++i) {
        int source, destination;
        std::cin >> source >> destination;
        adjList[source].push_back(destination);
    }
    for (int vertex = 1; vertex <= v; ++vertex) {
        int edges = adjList[vertex].size();
        if (!edges) std::cout << 0 << "\n";
        else {
            std::sort(adjList[vertex].begin(), adjList[vertex].end());
            std::cout << edges << " ";
            for (int idx = 0; idx < adjList[vertex].size(); ++idx) {
                if (idx) std::cout << " ";
                std::cout << adjList[vertex][idx];
            }
            std::cout << "\n";
        }
    }
}


int main() {
    solution();
}