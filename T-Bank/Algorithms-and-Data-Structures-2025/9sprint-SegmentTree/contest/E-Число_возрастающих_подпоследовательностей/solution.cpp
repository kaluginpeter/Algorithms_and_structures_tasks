#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

const int MOD = 1e9 + 7;

struct Node {
    int max_len;
    int count;
    Node() : max_len(0), count(0) {}
    Node(int len, int cnt) : max_len(len), count(cnt) {}
};

Node merge(const Node& a, const Node& b) {
    if (a.max_len > b.max_len) {
        return a;
    } else if (a.max_len < b.max_len) {
        return b;
    } else {
        return Node(a.max_len, (a.count + b.count) % MOD);
    }
}

class SegmentTree {
private:
    int size;
    vector<Node> tree;

    void update(int idx, int l, int r, int pos, const Node& val) {
        if (l == r) {
            tree[idx] = merge(tree[idx], val);
            return;
        }
        int mid = (l + r) / 2;
        if (pos <= mid) {
            update(2 * idx + 1, l, mid, pos, val);
        } else {
            update(2 * idx + 2, mid + 1, r, pos, val);
        }
        tree[idx] = merge(tree[2 * idx + 1], tree[2 * idx + 2]);
    }

    Node query(int idx, int l, int r, int ql, int qr) {
        if (qr < l || ql > r) {
            return Node(0, 0);
        }
        if (ql <= l && r <= qr) {
            return tree[idx];
        }
        int mid = (l + r) / 2;
        Node left = query(2 * idx + 1, l, mid, ql, qr);
        Node right = query(2 * idx + 2, mid + 1, r, ql, qr);
        return merge(left, right);
    }

public:
    SegmentTree(int n) : size(n), tree(4 * n, Node(0, 0)) {}

    void update(int pos, const Node& val) {
        update(0, 0, size - 1, pos, val);
    }

    Node query(int l, int r) {
        return query(0, 0, size - 1, l, r);
    }
};

void solution() {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    */
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<int> sorted_a = a;
    sort(sorted_a.begin(), sorted_a.end());
    sorted_a.erase(unique(sorted_a.begin(), sorted_a.end()), sorted_a.end());
    for (int& num : a) {
        num = lower_bound(sorted_a.begin(), sorted_a.end(), num) - sorted_a.begin();
    }

    int max_compressed = sorted_a.size();
    SegmentTree st(max_compressed);

    vector<int> dp_len(n, 1);
    vector<int> dp_count(n, 1);

    for (int i = 0; i < n; ++i) {
        if (a[i] > 0) {
            Node res = st.query(0, a[i] - 1);
            if (res.max_len + 1 > dp_len[i]) {
                dp_len[i] = res.max_len + 1;
                dp_count[i] = res.count;
            } else if (res.max_len + 1 == dp_len[i]) {
                dp_count[i] = (dp_count[i] + res.count) % MOD;
            }
        }
        st.update(a[i], Node(dp_len[i], dp_count[i]));
    }

    Node total = st.query(0, max_compressed - 1);
    cout << total.count << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    solution();
    return 0;
}