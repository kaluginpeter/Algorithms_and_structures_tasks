#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>


void dfs(int& source, std::unordered_map<int, std::vector<int>>& adjList, std::vector<std::string>& colors, std::vector<int>& output) {
    std::vector<int> callStack = {source};
    while (!callStack.empty()) {
        int vertex = callStack[callStack.size() - 1];
        callStack.pop_back();
        if (colors[vertex] == "white") {
            colors[vertex] = "grey";
            callStack.push_back(vertex);
            for (int& neighbor : adjList[vertex]) {
                if (colors[neighbor] == "white") callStack.push_back(neighbor);
            }
        } else if (colors[vertex] == "grey") {
            output.push_back(vertex);
            colors[vertex] = "black";
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
    }
    std::vector<std::string> colors (n + 1, "white");
    std::vector<int> output;
    for (int vertex = n; vertex > 0; --vertex) {
        if (colors[vertex] == "white") dfs(vertex, adjList, colors, output);
    }
    for (int idx = n - 1; idx >= 0; --idx) {
        if (idx != n - 1) std::cout << " ";
        std::cout << output[idx];
    }
    std::cout << "\n";
}


int main() {
    solution();
}