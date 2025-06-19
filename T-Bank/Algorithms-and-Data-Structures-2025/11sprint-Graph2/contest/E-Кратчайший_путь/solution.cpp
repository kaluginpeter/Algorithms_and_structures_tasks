#include <iostream>
#include <vector>
#include <queue>
#include <cstdint>



void solution() {
    /*
    Time Complexity O(NlogM)
    Memory Complexity O(N + M)
    */
    int n, m;
    std::scanf("%d %d", &n, &m);
    std::vector<bool> seen(n + 1, false);
    std::vector<long long> cost(n + 1, INT64_MAX);
    seen[1] = true;
    cost[1] = 0;
    std::vector<std::vector<std::pair<int, int>>> adjList(n + 1, std::vector<std::pair<int, int>>());
    for (int i = 0; i < m; ++i) {
        int source, destination, weight;
        std::scanf("%d %d %d", &source, &destination, &weight);
        adjList[source].push_back({destination, weight});
        adjList[destination].push_back({source, weight});
    }
    std::priority_queue<std::pair<long long, int>, std::vector<std::pair<long long, int>>, std::greater<std::pair<long long, int>>> minHeap;
    minHeap.push({0, 1});
    while (!minHeap.empty()) {
        int vertex = minHeap.top().second;
        long long amount = minHeap.top().first;
        minHeap.pop();
        for (std::pair<int, int> edge : adjList[vertex]) {
            if (!seen[edge.first] || (amount + edge.second < cost[edge.first])) {
                seen[edge.first] = true;
                cost[edge.first] = amount + edge.second;
                minHeap.push({amount + edge.second, edge.first});
            }
        }
    }
    for (int vertex = 1; vertex <= n; ++vertex) {
        std::printf("%lld ", cost[vertex]);
    }
    std::cout << '\n';
}


int main() {
    solution();
}