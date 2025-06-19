#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>
#include <algorithm>

using namespace std;


void solution() {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    */
    int n;
    cin >> n;

    vector<int> a(n);
    for (int &x : a) cin >> x;

    vector<int> d(n);
    for (int &x : d) cin >> x;

    set<int> alive;
    for (int i = 0; i < n; ++i) alive.insert(i);

    vector<int> result(n, 0);
    unordered_set<int> current_candidates;
    for (int i = 0; i < n; ++i) current_candidates.insert(i);

    for (int round = 0; round < n; ++round) {
        if (current_candidates.empty()) break;
        unordered_set<int> to_die;
        unordered_set<int> next_candidates;
        for (int j : current_candidates) {
            if (alive.find(j) == alive.end()) continue;

            auto it = alive.find(j);
            int left_alive = -1, right_alive = -1;

            if (it != alive.begin()) {
                auto left_it = prev(it);
                left_alive = *left_it;
            }
            if (next(it) != alive.end()) {
                auto right_it = next(it);
                right_alive = *right_it;
            }

            int damage = 0;
            if (left_alive != -1) damage += a[left_alive];
            if (right_alive != -1) damage += a[right_alive];

            if (damage > d[j]) to_die.insert(j);
        }

        for (int j : to_die) {
            alive.erase(j);
            result[round]++;
            auto it = alive.lower_bound(j);
            if (it != alive.begin()) next_candidates.insert(*prev(it));
            if (it != alive.end()) next_candidates.insert(*it);
        }
        current_candidates = next_candidates;
    }

    for (int i = 0; i < n; ++i) cout << result[i] << ' ';
    cout << '\n';
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solution();
}