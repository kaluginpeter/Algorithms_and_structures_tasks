#include <iostream>
#include <unordered_map>
#include <vector>
#include <tuple>
#include <cmath>
#include <functional>

struct TupleHash {
    template <class T>
    size_t operator()(const std::tuple<T, T>& t) const {
        auto hash1 = std::hash<T>()(std::get<0>(t));
        auto hash2 = std::hash<T>()(std::get<1>(t));
        return hash1 ^ (hash2 << 1);
    }
};

int euqlidieanDistanceSquared(std::tuple<int, int>& p1, std::tuple<int, int>& p2) {
    return std::pow(std::get<0>(p1) - std::get<0>(p2), 2) + std::pow(std::get<1>(p1) - std::get<1>(p2), 2);
}

void solution() {
    /*
    Time Complexity O(N + M + NK)
    Memory Complexity O(N + M)
    */
    int n;
    std::cin >> n;
    std::vector<std::tuple<int, int>> nPoints;
    for (int i = 0; i < n; ++i) {
        int x, y;
        std::cin >> x >> y;
        nPoints.push_back({x, y});
    }
    int m;
    std::cin >> m;
    std::vector<std::tuple<int, int>> mPoints;
    for (int i = 0; i < m; ++i) {
        int x, y;
        std::cin >> x >> y;
        mPoints.push_back({x, y});
    }
    int maxDistance = 20;
    int bound = std::pow(maxDistance, 2);
    int gridSize = maxDistance;
    std::unordered_map<std::tuple<int, int>, std::vector<std::tuple<int, int>>, TupleHash> grid;
    for (int idx = 0; idx < m; ++idx) {
        int cellX = std::get<0>(mPoints[idx]) / gridSize;
        int cellY = std::get<1>(mPoints[idx]) / gridSize;
        grid[{cellX, cellY}].push_back({std::get<0>(mPoints[idx]), std::get<1>(mPoints[idx])});
    }
    int maxCount = 0;
    int bestPointIndex = -1;
    std::vector<int> moves = {-1, 0, 1};
    for (int idx = 0; idx < n; ++idx) {
        int count = 0;
        int cellXN = std::get<0>(nPoints[idx]) / gridSize;
        int cellYN = std::get<1>(nPoints[idx]) / gridSize;
        for (int dX : moves) {
            for (int dY : moves) {
                std::tuple<int, int> currentCell = {cellXN + dX, cellYN + dY};
                if (grid.count(currentCell)) {
                    for (std::tuple<int, int> pair : grid[currentCell]) {
                        if (euqlidieanDistanceSquared(nPoints[idx], pair) <= bound) {
                            ++count;
                        }
                    }
                }
            }
        }
        if (count > maxCount) {
            maxCount = count;
            bestPointIndex = idx;
        }
    }
    std::cout << bestPointIndex + 1 << "\n";
}


int main() {
    solution();
}