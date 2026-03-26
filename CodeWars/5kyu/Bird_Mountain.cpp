/*
Kata Task
A bird flying high above a mountain range is able to estimate the height of the highest peak.

Can you?

Example
The birds-eye view
^^^^^^
 ^^^^^^^^
  ^^^^^^^
  ^^^^^
  ^^^^^^^^^^^
  ^^^^^^
  ^^^^
The bird-brain calculations
111111
 1^^^^111
  1^^^^11
  1^^^1
  1^^^^111111
  1^^^11
  1111

111111
 12222111
  12^^211
  12^21
  12^^2111111
  122211
  1111

111111
 12222111
  1233211
  12321
  12332111111
  122211
  1111

Height = 3

Series
Bird Mountain
Bird Mountain - the river
AlgorithmsGraph Theory
*/
#include <bits/stdc++.h>
using namespace std;

int peak_height(vector<string>& mountain) {
    int n = mountain.size();
    int m = mountain[0].size();

    vector<vector<int>> height(n, vector<int>(m, 0));
    queue<pair<int,int>> q;

    auto is_boundary = [&](int i, int j) {
        if (mountain[i][j] != '^') return false;

        vector<pair<int,int>> dirs = {{-1,0},{1,0},{0,-1},{0,1}};
        for (auto [dx, dy] : dirs) {
            int ni = i + dx, nj = j + dy;
            if (ni < 0 || nj < 0 || ni >= n || nj >= m || mountain[ni][nj] == ' ')
                return true;
        }
        return false;
    };
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (is_boundary(i, j)) {
                height[i][j] = 1;
                q.push({i, j});
            }
        }
    }

    int maxh = 0;
    vector<pair<int,int>> dirs = {{-1,0},{1,0},{0,-1},{0,1}};

    while (!q.empty()) {
        auto [i, j] = q.front(); q.pop();
        maxh = max(maxh, height[i][j]);

        for (auto [dx, dy] : dirs) {
            int ni = i + dx, nj = j + dy;

            if (ni >= 0 && nj >= 0 && ni < n && nj < m) {
                if (mountain[ni][nj] == '^' && height[ni][nj] == 0) {
                    height[ni][nj] = height[i][j] + 1;
                    q.push({ni, nj});
                }
            }
        }
    }

    return maxh;
}