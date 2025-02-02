#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <algorithm>



void dfs(int& source, std::unordered_map<int, std::vector<int>>& adjList, int& v) {
    std::vector<std::string> colors (v + 1, "white");
    std::vector<int> callStack = {source};
    while (!callStack.empty()) {
        int& curVertex = callStack[callStack.size() - 1];
        callStack.pop_back();
        if (colors[curVertex] == "white") {
            std::cout << curVertex << " ";
            colors[curVertex] = "grey";
            callStack.push_back(curVertex);
            for (int& nextVertex : adjList[curVertex]) {
                if (colors[nextVertex] == "white") callStack.push_back(nextVertex);
            }
        } else if (colors[curVertex] == "grey") colors[curVertex] = "black";
    }
}


void solution() {
    /*
    Time Complexity O(ElogE + (V + E))
    Memory Complexity O(V + E)
    */
    int v, e;
    std::cin >> v >> e;
    std::unordered_map<int, std::vector<int>> adjList;
    for (int i = 0; i < e; ++i) {
        int source, destination;
        std::cin >> source >> destination;
        adjList[source].push_back(destination);
        adjList[destination].push_back(source);
    }
    int start;
    std::cin >> start;
    for (auto& pair : adjList) {
        std::sort(pair.second.begin(), pair.second.end(), std::greater<int>());
    }
    dfs(start, adjList, v);
}


int main() {
    solution();
}