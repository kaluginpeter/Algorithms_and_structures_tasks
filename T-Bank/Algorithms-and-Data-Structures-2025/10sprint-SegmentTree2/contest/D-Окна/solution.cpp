#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

struct Event {
    int x, y1, y2, type;
    Event(int x, int y1, int y2, int type) : x(x), y1(y1), y2(y2), type(type) {}
    bool operator<(const Event& other) const {
        if (x != other.x) return x < other.x;
        return type > other.type;
    }
};

struct SegmentTree {
    vector<int> max_cnt, cnt, lazy;
    vector<int> max_pos;
    int size;

    SegmentTree(int n) {
        size = 1;
        while (size < n) size <<= 1;
        max_cnt.resize(2 * size, 0);
        cnt.resize(2 * size, 0);
        lazy.resize(2 * size, 0);
        max_pos.resize(2 * size, 0);
        for (int i = 0; i < size; ++i) {
            max_pos[i + size] = i;
        }
        for (int i = size - 1; i > 0; --i) {
            max_pos[i] = max_pos[2 * i];
        }
    }

    void push(int node, int node_l, int node_r) {
        if (lazy[node] == 0) return;
        max_cnt[node] += lazy[node];
        cnt[node] += lazy[node];
        if (node_l != node_r) {
            lazy[2 * node] += lazy[node];
            lazy[2 * node + 1] += lazy[node];
        }
        lazy[node] = 0;
    }

    void update_range(int l, int r, int val, int node = 1, int node_l = 0, int node_r = -1) {
        if (node_r == -1) node_r = size - 1;
        push(node, node_l, node_r);
        if (r < node_l || l > node_r) return;
        if (l <= node_l && node_r <= r) {
            lazy[node] += val;
            push(node, node_l, node_r);
            return;
        }
        int mid = (node_l + node_r) / 2;
        update_range(l, r, val, 2 * node, node_l, mid);
        update_range(l, r, val, 2 * node + 1, mid + 1, node_r);
        if (max_cnt[2 * node] >= max_cnt[2 * node + 1]) {
            max_cnt[node] = max_cnt[2 * node];
            max_pos[node] = max_pos[2 * node];
        } else {
            max_cnt[node] = max_cnt[2 * node + 1];
            max_pos[node] = max_pos[2 * node + 1];
        }
        cnt[node] = max(cnt[2 * node], cnt[2 * node + 1]);
    }

    pair<int, int> get_max() {
        push(1, 0, size - 1);
        return {max_cnt[1], max_pos[1]};
    }
};

void solution() {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    */
    int n;
    cin >> n;
    vector<Event> events;
    int min_y = INT_MAX, max_y = INT_MIN;
    for (int i = 0; i < n; ++i) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        if (y1 > y2) swap(y1, y2);
        events.emplace_back(x1, y1, y2, 1);
        events.emplace_back(x2, y1, y2, -1);
        min_y = min(min_y, y1);
        max_y = max(max_y, y2);
    }
    sort(events.begin(), events.end());
    int y_range = max_y - min_y + 1;
    SegmentTree st(y_range);
    int max_overlap = 0;
    int result_x = 0, result_y = 0;
    for (const auto& event : events) {
        int current_max = st.get_max().first;
        if (current_max > max_overlap) {
            max_overlap = current_max;
            result_x = event.x;
            result_y = st.get_max().second + min_y;
        }
        st.update_range(event.y1 - min_y, event.y2 - min_y, event.type);
    }
    cout << max_overlap << "\n" << result_x << " " << result_y << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    solution();
    return 0;
}