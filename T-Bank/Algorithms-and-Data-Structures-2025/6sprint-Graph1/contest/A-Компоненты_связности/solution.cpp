#include <iostream>
#include <vector>
#include <algorithm>


void dfs(int& start, std::vector<std::vector<int>>& adjList, std::vector<int>& colors, std::vector<std::vector<int>>& components, int& color) {
    std::vector<int> queue = {start};
    colors[start] = color;
    components.push_back({start});
    while (!queue.empty()) {
        int& vertex = queue.back();
        queue.pop_back();
        for (int& neighbor : adjList[vertex]) {
            if (colors[neighbor] == -1) {
                colors[neighbor] = color;
                queue.push_back(neighbor);
                components[color].push_back(neighbor);
            }
        }
    }
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
        adjList[v].push_back(u);
    }
    std::vector<int> colors (n + 1, -1);
    std::vector<std::vector<int>> components;
    int color = 0;
    for (int vertex = 1; vertex <= n; ++vertex) {
        if (colors[vertex] == -1) {
            dfs(vertex, adjList, colors, components, color);
            ++color;
        }
    }
    std::printf("%d\n", components.size());
    for (std::vector<int>& component : components) {
        std::printf("%d\n", component.size());
        std::sort(component.begin(), component.end());
        for (int& vertex : component) std::printf("%d ", vertex);
        std::printf("\n");
    }
}


int main() {
    solution();
}