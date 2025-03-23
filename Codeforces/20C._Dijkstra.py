# C. Dijkstra?
# time limit per test1 second
# memory limit per test64 megabytes
# You are given a weighted undirected graph. The vertices are enumerated from 1 to n. Your task is to find the shortest path between the vertex 1 and the vertex n.
#
# Input
# The first line contains two integers n and m (2 ≤ n ≤ 105, 0 ≤ m ≤ 105), where n is the number of vertices and m is the number of edges. Following m lines contain one edge each in form ai, bi and wi (1 ≤ ai, bi ≤ n, 1 ≤ wi ≤ 106), where ai, bi are edge endpoints and wi is the length of the edge.
#
# It is possible that the graph has loops and multiple edges between pair of vertices.
#
# Output
# Write the only integer -1 in case of no path. Write the shortest path in opposite case. If there are many solutions, print any of them.
#
# Examples
# InputCopy
# 5 6
# 1 2 2
# 2 5 5
# 2 3 4
# 1 4 1
# 4 3 3
# 3 5 1
# OutputCopy
# 1 4 3 5
# InputCopy
# 5 6
# 1 2 2
# 2 5 5
# 2 3 4
# 1 4 1
# 4 3 3
# 3 5 1
# OutputCopy
# 1 4 3 5
# Solution
# C++ O(|E|log(|V|)) O(|V|) Dijkstra ShortestPath
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

void solution() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<pair<int, int>>> adjList (n + 1, vector<pair<int, int>>());
    vector<int> path (n + 1, -1);
    for (int i = 0; i < m; ++i) {
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);
        if (adjList[u].empty()) adjList[u].push_back({0, 0});
        if (adjList[v].empty()) adjList[v].push_back({0, 0});
        adjList[u].push_back({v, w});
        adjList[v].push_back({u, w});
    }
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> minHeap;
    vector<long long> costVertex (n + 1, 1e12);
    costVertex[1] = 0;
    minHeap.push({0, 1});
    while (!minHeap.empty()) {
        long long curCost = minHeap.top().first;
        int vertex = minHeap.top().second;
        minHeap.pop();
        if (vertex == n) break;
        for (pair<int, int>& edge : adjList[vertex]) {
            long long nextCost = curCost + edge.second;
            if (nextCost < costVertex[edge.first]) {
                path[edge.first] = vertex;
                costVertex[edge.first] = nextCost;
                minHeap.push({nextCost, edge.first});
            }
        }
    }
    vector<int> order;
    int vertex = n;
    if (path[vertex] != -1) order.push_back(vertex);
    while (path[vertex] != -1) {
        order.push_back(path[vertex]);
        vertex = path[vertex];
    }
    if (order.empty()) {
        printf("-1\n");
        return;
    }
    for (int i = order.size() - 1; i >= 0; --i) printf("%d ", order[i]);
    printf("\n");
}


int main() {
    solution();
}

# Python O(|E|log(|V|)) O(|V|) Dijkstra ShortestPath
import sys
import heapq


def solution() -> None:
    n, m = map(int, sys.stdin.readline().rstrip().split())
    path: list[int] = [-1] * (n + 1)
    cost: list[int] = [float('inf')] * (n + 1)
    adj_list: list[list[tuple[int, int]]] = [[(0, 0)] for _ in range(n + 1)]
    for _ in range(m):
        u, v, weight = map(int, sys.stdin.readline().rstrip().split())
        adj_list[u].append((v, weight))
        adj_list[v].append((u, weight))
    min_heap: list[tuple[int, int]] = [(0, 1)]
    cost[1] = 0
    cost[1] = 0
    while min_heap:
        cur_cost, vertex = heapq.heappop(min_heap)
        if vertex == n: break
        for neighbor, weight in adj_list[vertex][1:]:
            next_cost: int = cur_cost + weight
            if next_cost < cost[neighbor]:
                cost[neighbor] = next_cost
                path[neighbor] = vertex
                heapq.heappush(min_heap, (next_cost, neighbor))
    order: list[int] = []
    vertex: int = n
    if path[vertex] != -1: order.append(vertex)
    while path[vertex] != -1:
        vertex = path[vertex]
        order.append(vertex)
    if not order: sys.stdout.write('-1\n')
    else: sys.stdout.write('{}\n'.format(' '.join(str(v) for v in reversed(order))))

if __name__ == '__main__':
    solution()