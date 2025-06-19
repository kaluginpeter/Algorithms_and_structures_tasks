#include <iostream>
#include <vector>
#include <climits>

using namespace std;

class SegmentTree {
private:
    struct Node {
        int l, r;
        long long min_val;
        long long lazy;
        Node *left, *right;
        Node(int l, int r) : l(l), r(r), min_val(0), lazy(0), left(nullptr), right(nullptr) {}
    };

    Node* root;

    void build(Node* node, const vector<long long>& data) {
        if (node->l == node->r) {
            node->min_val = data[node->l];
            return;
        }
        int mid = (node->l + node->r) / 2;
        node->left = new Node(node->l, mid);
        node->right = new Node(mid + 1, node->r);
        build(node->left, data);
        build(node->right, data);
        node->min_val = min(node->left->min_val, node->right->min_val);
    }

    void push(Node* node) {
        if (node->lazy != 0) {
            node->min_val += node->lazy;
            if (node->left) {
                node->left->lazy += node->lazy;
                node->right->lazy += node->lazy;
            }
            node->lazy = 0;
        }
    }

    void range_add(Node* node, int l, int r, long long v) {
        push(node);
        if (node->r < l || node->l > r) return;
        if (l <= node->l && node->r <= r) {
            node->lazy += v;
            push(node);
            return;
        }
        range_add(node->left, l, r, v);
        range_add(node->right, l, r, v);
        node->min_val = min(node->left->min_val, node->right->min_val);
    }

    long long range_min(Node* node, int l, int r) {
        push(node);
        if (node->r < l || node->l > r) return LLONG_MAX;
        if (l <= node->l && node->r <= r) return node->min_val;
        return min(range_min(node->left, l, r), range_min(node->right, l, r));
    }

public:
    SegmentTree(const vector<long long>& data) {
        root = new Node(0, data.size() - 1);
        build(root, data);
    }

    void rangeAdd(int l, int r, long long v) {
        range_add(root, l, r, v);
    }

    long long rangeMin(int l, int r) {
        return range_min(root, l, r);
    }
};


void solution() {
    int n, m;
    cin >> n >> m;
    vector<long long> data(n, 0);
    SegmentTree st(data);

    for (int i = 0; i < m; ++i) {
        int cmd;
        cin >> cmd;
        if (cmd == 1) {
            int l, r, v;
            cin >> l >> r >> v;
            st.rangeAdd(l, r - 1, v);
        } else {
            int l, r;
            cin >> l >> r;
            cout << st.rangeMin(l, r - 1) << '\n';
        }
    }
}


int main() {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    */
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    solution();

    return 0;
}