#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <utility>
#include <limits>


std::vector<int> dijkstra(int& source, std::unordered_map<int, std::vector<std::pair<int, int>>>& adjList, int& n) {
    std::vector<int> dist (n + 1, -1);
    dist[source] = 0;
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> minHeap;
    minHeap.push({0, source});
    while (minHeap.size() > 0) {
        auto [weight, vertex] = minHeap.top();
        minHeap.pop();
        for (std::pair<int, int>& edge : adjList[vertex]) {
            int amount = weight + edge.second;
            if ((dist[edge.first] == -1) || (amount < dist[edge.first])) {
                dist[edge.first] = amount;
                minHeap.push({amount, edge.first});
            }
        }
    }
    return dist;
}


void solution() {
    /*
    Time Complexity O(V(VlogE))
    Memory Complexity O(V + E)
    */
    int n, m;
    std::cin >> n >> m;
    std::unordered_map<int, std::vector<std::pair<int, int>>> adjList;
    for (int i = 0; i < m; ++i) {
        int source, destination, weight;
        std::cin >> source >> destination >> weight;
        adjList[source].push_back({destination, weight});
        adjList[destination].push_back({source, weight});
    }
    for (int vertex = 1; vertex <= n; ++vertex) {
        std::vector<int> shortestPathTree = dijkstra(vertex, adjList, n);
        for (int idx = 1; idx <= n; ++idx) {
            if (idx > 1) std::cout << " ";
            std::cout << shortestPathTree[idx];
        }
        std::cout << "\n";
    }
}


int main() {
    solution();
}