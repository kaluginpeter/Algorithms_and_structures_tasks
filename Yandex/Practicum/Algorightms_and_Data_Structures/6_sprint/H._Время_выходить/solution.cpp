#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
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
    }
    for (auto& pair : adjList) {
        std::sort(pair.second.begin(), pair.second.end(), std::greater<int>());
    }
    std::vector<int> enter (n + 1, 0);
    std::vector<int> leave (n + 1, 0);
    std::vector<std::string> colors (n + 1, "white");
    std::vector<int> callStack = {1};
    int curTime = -1;
    while (!callStack.empty()) {
        int& vertex = callStack[callStack.size() - 1];
        callStack.pop_back();
        if (colors[vertex] != "black") ++curTime;
        if (colors[vertex] == "white") {
            colors[vertex] = "grey";
            enter[vertex] = curTime;
            callStack.push_back(vertex);
            for (int& neighbor : adjList[vertex]) {
                if (colors[neighbor] == "white") {
                    callStack.push_back(neighbor);
                }
            }
        } else if (colors[vertex] == "grey") {
            colors[vertex] = "black";
            leave[vertex] = curTime;
        }
    }
    for (int vertex = 1; vertex <= n; ++vertex) {
        std::cout << enter[vertex] << " " << leave[vertex] << "\n";
    }
}


int main() {
    solution();
}