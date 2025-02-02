#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>


void solution() {
    /*
    Time Complexity O(V + E)
    Memory Complexity O(V + E)
    */
    int n, m;
    std::cin >> n >> m;
    std::unordered_map<int, std::unordered_set<int>> adjList;
    for (int i = 0; i < m; ++i) {
        int u, v;
        std::cin >> u >> v;
        if (u != v) {
            adjList[u].insert(v);
            adjList[v].insert(u);
        }
    }
    for (auto& p : adjList) {
        if (p.second.size() != n - 1) {
            std::cout << "NO\n";
            return;
        }
    }
    std::cout << ((adjList.size() == n) || (n == 1)? "YES" : "NO") << "\n";
}


int main() {
    solution();
}