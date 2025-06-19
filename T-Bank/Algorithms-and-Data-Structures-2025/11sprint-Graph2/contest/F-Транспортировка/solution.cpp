#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>
#include <climits>

using namespace std;

bool check(int cups, const vector<vector<tuple<int, int, int>>> &adjList, int n) {
    vector<int> dist(n + 1, INT_MAX);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    dist[1] = 0;
    pq.push({0, 1});
    while (!pq.empty()) {
        int current_time = pq.top().first;
        int city = pq.top().second;
        pq.pop();
        if (city == n) return true;
        if (current_time > dist[city]) continue;
        for (const auto &edge : adjList[city]) {
            int neighbor = get<0>(edge);
            int time = get<1>(edge);
            int weight_limit = get<2>(edge);

            if (cups * 100 <= weight_limit) {
                int new_time = current_time + time;
                if (new_time < dist[neighbor] && new_time <= 1440) {
                    dist[neighbor] = new_time;
                    pq.push({new_time, neighbor});
                }
            }
        }
    }
    return dist[n] <= 1440;
}


void solution() {
    /*
    Time Complexity O((VlogE)log(M))
    Memory Complexity O(E)
    */
    int n, m;
    std::scanf("%d %d", &n, &m);
    std::vector<std::vector<std::tuple<int, int, int>>> adjList(n + 1, std::vector<std::tuple<int, int, int>>());
    for (int i = 0; i < m; ++i) {
        int from, to, cost, bound;
        std::scanf("%d %d %d %d", &from, &to, &cost, &bound);
        bound = std::max(0, bound - 3000000);
        adjList[to].push_back({from, cost, bound});
        adjList[from].push_back({to, cost, bound});
    }
    int left = 1, right = 10000001, output = 0;
    while (left <= right) {
        int middle = left + ((right - left) >> 1);
        if (check(middle, adjList, n)) {
            output = middle;
            left = middle + 1;
        } else right = middle - 1;
    }
    std::printf("%d\n", output);
}


int main() {
    solution();
}