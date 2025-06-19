#include <iostream>
#include <vector>
#include <tuple>


class UnionFind {
private:
    int n;
    std::vector<int> parent;
    std::vector<int> rank;
    std::vector<int> minValue;
    std::vector<int> maxValue;
    int components;

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
        components = n;
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
        --components;
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
};



void solution() {
    /*
    Time Complexity O((NM)log(NM))
    Memory Complexity O(NM)
    */
    int n, m;
    std::scanf("%d %d", &n, &m);
    UnionFind uf(n * m + 2);
    std::vector<std::vector<int>> grid (n + 1, std::vector<int>(m + 1, 0));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) std::scanf("%d", &grid[i][j]);
    }
    for (int r = 1; r <= n; ++r) {
        for (int c = 1; c <= m; ++c) {
            if (grid[r][c] == 1) {
                uf.union_((r - 1) * m + c, (r - 1) * m + c + m);
            } else if (grid[r][c] == 2) {
                uf.union_((r - 1) * m + c, (r - 1) * m + c + 1);
            } else if (grid[r][c] == 3) {
                uf.union_((r - 1) * m + c, (r - 1) * m + c + m);
                uf.union_((r - 1) * m + c, (r - 1) * m + c + 1);
            }
        }
    }
    int score = 0;
    std::vector<std::tuple<int, int, int>> moves;
    for (int r = 1; r < n; ++r) {
        for (int c = 1; c <= m; ++c) {
            if (uf.find((r - 1) * m + c) != uf.find((r - 1) * m + c + m)) {
                ++score;
                uf.union_((r - 1) * m + c, (r - 1) * m + c + m);
                moves.push_back({r, c, 1});
            }
        }
    }
    for (int r = 1; r <= n; ++r) {
        for (int c = 1; c < m; ++c) {
            if (uf.find((r - 1) * m + c) != uf.find((r - 1) * m + c + 1)) {
                score += 2;
                moves.push_back({r, c, 2});
                uf.union_((r - 1) * m + c, (r - 1) * m + c + 1);
            }
        }
    }
    std::printf("%d %d\n", moves.size(), score);
    for (std::tuple<int, int, int> &move : moves) {
        std::printf("%d %d %d\n", std::get<0>(move), std::get<1>(move), std::get<2>(move));
    }
}


int main() {
    solution();
}