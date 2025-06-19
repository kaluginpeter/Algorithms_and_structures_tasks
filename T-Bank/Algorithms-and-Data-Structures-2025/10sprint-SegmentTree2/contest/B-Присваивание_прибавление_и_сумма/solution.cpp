#include <iostream>
#include <vector>
#include <climits>

using namespace std;


struct Node {
    int l, r;
    long long min_val;
    long long sum;
    long long add_lazy;
    long long assign_lazy;
    bool has_assignment;
    Node *left, *right;

    Node(int l, int r) : l(l), r(r), min_val(0), sum(0), add_lazy(0), assign_lazy(0), has_assignment(false), left(nullptr), right(nullptr) {}
};


class SegmentTree {
private:
    Node* root;

    void build(Node* node, const vector<long long>& data) {
        if (node->l == node->r) {
            node->min_val = data[node->l];
            node->sum = data[node->l];
            return;
        }
        int mid = (node->l + node->r) / 2;
        node->left = new Node(node->l, mid);
        node->right = new Node(mid + 1, node->r);
        build(node->left, data);
        build(node->right, data);
        node->sum = node->left->sum + node->right->sum;
        node->min_val = min(node->left->min_val, node->right->min_val);
    }

    void push(Node* node) {
        if (node->has_assignment) {
            node->min_val = node->assign_lazy;
            node->sum = node->assign_lazy * (node->r - node->l + 1);
            if (node->left) {
                node->left->assign_lazy = node->assign_lazy;
                node->left->add_lazy = 0;
                node->left->has_assignment = true;
                node->right->assign_lazy = node->assign_lazy;
                node->right->add_lazy = 0;
                node->right->has_assignment = true;
            }
            node->has_assignment = false;
        }
        if (node->add_lazy != 0) {
            node->min_val += node->add_lazy;
            node->sum += node->add_lazy * (node->r - node->l + 1);
            if (node->left) {
                node->left->add_lazy += node->add_lazy;
                node->right->add_lazy += node->add_lazy;
            }
            node->add_lazy = 0;
        }
    }

    void range_add(Node* node, int l, int r, long long v) {
        push(node);
        if (node->r < l || node->l > r) return;
        if (l <= node->l && node->r <= r) {
            node->add_lazy += v;
            push(node);
            return;
        }
        range_add(node->left, l, r, v);
        range_add(node->right, l, r, v);
        node->sum = node->left->sum + node->right->sum;
        node->min_val = min(node->left->min_val, node->right->min_val);
    }

    void range_assign(Node* node, int l, int r, long long v) {
        push(node);
        if (node->r < l || node->l > r) return;
        if (l <= node->l && node->r <= r) {
            node->assign_lazy = v;
            node->has_assignment = true;
            node->add_lazy = 0;
            push(node);
            return;
        }
        range_assign(node->left, l, r, v);
        range_assign(node->right, l, r, v);
        node->sum = node->left->sum + node->right->sum;
        node->min_val = min(node->left->min_val, node->right->min_val);
    }

    long long range_min(Node* node, int l, int r) {
        push(node);
        if (node->r < l || node->l > r) return LLONG_MAX;
        if (l <= node->l && node->r <= r) return node->min_val;
        return min(range_min(node->left, l, r), range_min(node->right, l, r));
    }

    long long range_sum(Node* node, int l, int r) {
        push(node);
        if (node->r < l || node->l > r) return 0;
        if (l <= node->l && node->r <= r) return node->sum;
        return range_sum(node->left, l, r) + range_sum(node->right, l, r);
    }

public:
    SegmentTree(const vector<long long>& data) {
        root = new Node(0, data.size() - 1);
        build(root, data);
    }

    void rangeAdd(int l, int r, long long v) {
        range_add(root, l, r, v);
    }

    void rangeAssign(int l, int r, long long v) {
        range_assign(root, l, r, v);
    }

    long long rangeMin(int l, int r) {
        return range_min(root, l, r);
    }

    long long rangeSum(int l, int r) {
        return range_sum(root, l, r);
    }
};


void solution() {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    */
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
            st.rangeAssign(l, r - 1, v);
        } else if (cmd == 2) {
            int l, r, v;
            cin >> l >> r >> v;
            st.rangeAdd(l, r - 1, v);
        } else {
            int l, r;
            cin >> l >> r;
            cout << st.rangeSum(l, r - 1) << '\n';
        } 
    }
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    solution();

    return 0;
}