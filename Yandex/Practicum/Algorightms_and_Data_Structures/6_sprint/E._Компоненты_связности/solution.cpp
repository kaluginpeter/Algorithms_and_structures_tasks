#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <algorithm>


void dfs(int& source, std::unordered_map<int, std::vector<int>>& adjList, std::vector<int>& colors, int& componentColor, std::vector<std::vector<int>>& components) {
    std::vector<int> callStack = {source};
    while (!callStack.empty()) {
        int vertex = callStack[callStack.size() - 1];
        callStack.pop_back();
        if (colors[vertex] == -1){
            components[componentColor].push_back(vertex);
            colors[vertex] = componentColor;
        }
        for (int& neighbor : adjList[vertex]) {
            if (colors[neighbor] == -1) callStack.push_back(neighbor);
        }
    }
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
        int before, after;
        std::cin >> before >> after;
        adjList[before].push_back(after);
        adjList[after].push_back(before);
    }
    std::vector<int> colors (n + 1, -1);
    std::vector<std::vector<int>> components;
    int componentColor = 0;
    for (int vertex = 1; vertex <= n; ++vertex) {
        if (colors[vertex] == -1) {
            components.push_back({});
            dfs(vertex, adjList, colors, componentColor, components);
            ++componentColor;
        }
    }
    for (std::vector<int>& component : components) {
        std::sort(component.begin(), component.end());
    }
    std::sort(components.begin(), components.end());
    std::cout << componentColor << "\n";
    for (std::vector<int>& component : components) {
        for (int idx = 0; idx < component.size(); ++idx) {
            if (idx) std::cout << " ";
            std::cout << component[idx];
        }
        std::cout << "\n";
    }
}


int main() {
    solution();
}