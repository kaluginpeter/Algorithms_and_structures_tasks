#include <iostream>
#include <string>
#include <vector>


class UnionFind {
private:
    int n;
    std::vector<int> parent;
    std::vector<int> rank;
    std::vector<int> minValue;
    std::vector<int> maxValue;

public:
    UnionFind(int n_) : n(n_) {
        parent.resize(n, 0);
        rank.resize(n, 1);
        minValue.resize(n, 0);
        maxValue.resize(n, 0);
        for (int i = 0; i < n; ++i) {
            parent[i] = i;
            minValue[i] = i;
            maxValue[i] = i;
        }
    }
    
    int find(int x) {
        while (x != parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }
    
    void union_(int v, int u) {
        int vParent = find(v), uParent = find(u);
        if (vParent == uParent) return;
        if (rank[vParent] >= rank[uParent]) {
            parent[uParent] = vParent;
            rank[vParent] += rank[uParent];
            minValue[vParent] = std::min(minValue[vParent], minValue[uParent]);
            maxValue[vParent] = std::max(maxValue[vParent], maxValue[uParent]);
        } else {
            parent[vParent] = uParent;
            rank[uParent] += rank[vParent];
            minValue[uParent] = std::min(minValue[uParent], minValue[vParent]);
            maxValue[uParent] = std::max(maxValue[uParent], maxValue[vParent]);
        }
    }
    
    void get(int x) {
        int xParent = find(x);
        std::printf("%d %d %d\n", minValue[xParent], maxValue[xParent], rank[xParent]);
    }
};



void solution() {
    /*
    Time Complexity O(MlogN)
    Memory Complexity O(N)
    */
    int n, m;
    std::scanf("%d %d", &n, &m);
    UnionFind uf(n + 1);
    for (int i = 0; i < m; ++i) {
        std::string op;
        std::cin >> op;
        if (op == "union") {
            int u, v;
            std::scanf("%d %d", &u, &v);
            uf.union_(u, v);
        } else {
            int x;
            std::scanf("%d", &x);
            uf.get(x);
        }
    }
}


int main() {
    solution();
}