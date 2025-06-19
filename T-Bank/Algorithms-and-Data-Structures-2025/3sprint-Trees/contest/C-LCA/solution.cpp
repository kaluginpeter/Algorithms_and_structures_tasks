#include <iostream>
#include <unordered_map>
#include <vector>


using namespace std;


void fillBFStree(unordered_map<int, vector<int>>& tree, unordered_map<int, int>& depth, unordered_map<int, int>& parent) {
    vector<int> curNodes = {0};
    parent[0] = -1;
    vector<int> nextNodes;
    int curDepth = -1;
    while (!curNodes.empty()) {
        ++curDepth;
        for (int& node : curNodes) {
            depth[node] = curDepth;
            for (int& child : tree[node]) {
                parent[child] = node;
                nextNodes.push_back(child);
            }
        }
        curNodes = nextNodes;
        nextNodes.clear();
    }
}


int getLCA(int& u, int& v, unordered_map<int, int>& depth, unordered_map<int, int>& parent) {
    while (depth[u] > depth[v]) u = parent[u];
    while (depth[v] > depth[u]) v = parent[v];
    while (u != v) {
        u = parent[u];
        v = parent[v];
    }
    return u;
}


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    int n;
    scanf("%d", &n);
    unordered_map<int, std::vector<int>> tree;
    for (int node = 1; node < n; ++node) {
        int parent;
        scanf("%d", &parent);
        tree[parent].push_back(node);
    }
    unordered_map<int, int> parent;
    unordered_map<int, int> depth;
    fillBFStree(tree, depth, parent);
    int m;
    scanf("%d", &m);
    for (int i = 0; i < m; ++i) {
        int u, v;
        scanf("%d %d", &u, &v);
        printf("%d\n", getLCA(u, v, depth, parent));
    }
}


int main() {
    solution();
}