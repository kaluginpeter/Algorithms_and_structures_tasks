#include <iostream>
#include <vector>
#include <queue>


using namespace std;


void solution() {
    /*
    Time Complexity O(|V| + |E|)
    Memory Complexity O(|V| + |E|)
    */
    int n;
    scanf("%d", &n);
    int x1, y1, x2, y2;
    scanf("%d %d\n%d %d", &x1, &y1, &x2, &y2);
    vector<pair<int, int>> moves = {
        {-2, 1}, {-2, -1}, {2, 1}, {2, -1}, {-1, 2}, {1, 2}, {-1, -2}, {1, -2}
    };
    queue<
        pair<
            pair<int, int>,
            vector<pair<int, int>>
        >
    > q;
    q.push({{x1, y1}, {{x1, y1}}});
    vector<vector<bool>> seen (n + 1, vector<bool>(n + 1, false));
    seen[x1][y1] = true;
    while (!q.empty()) {
        pair<int, int> curPos = q.front().first;
        vector<pair<int, int>> path = q.front().second;
        q.pop();
        if (curPos.first == x2 && curPos.second == y2) {
            printf("%d\n", path.size() - 1);
            for (pair<int, int>& pos : path) printf("%d %d\n", pos.first, pos.second);
            return;
        }
        for (pair<int, int>& move : moves) {
            int nextX = curPos.first + move.first;
            int nextY = curPos.second + move.second;
            if (min(nextX, nextY) < 1 || max(nextX, nextY) > n || seen[nextX][nextY]) continue;
            seen[nextX][nextY] = true;
            vector<pair<int, int>> nextPath = path;
            nextPath.push_back({nextX, nextY});
            q.push({{nextX, nextY}, nextPath});
        }
    }
}

int main() {
    solution();
}