#include <iostream>
#include <vector>
#include <climits>

using namespace std;


struct SegmentInfo {
    int left_color;
    int right_color;
    int count;
    int total_length;
    int length;
};


struct Node {
    int l, r;
    long long min_val;
    long long sum;
    long long add_lazy;
    long long assign_lazy;
    bool has_assignment;
    SegmentInfo info;
    Node *left, *right;

    Node(int l, int r) : l(l), r(r), min_val(0), sum(0), add_lazy(0), assign_lazy(0), has_assignment(false), left(nullptr), right(nullptr) {
        info.left_color = 0;
        info.right_color = 0;
        info.count = 0;
        info.total_length = 0;
        info.length = r - l + 1;
    }
};


class SegmentTree {
private:
    Node* root;

    void build(Node* node, const vector<long long>& data) {
        if (node->l == node->r) {
            node->info.left_color = 0;
            node->info.right_color = 0;
            node->info.count = 0;
            node->info.total_length = 0;
            node->info.length = 1;
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
        node->info = merge(node->left->info, node->right->info);
    }
    
    SegmentInfo merge(const SegmentInfo& left, const SegmentInfo& right) {
        SegmentInfo res;
        res.left_color = left.left_color;
        res.right_color = right.right_color;
        res.total_length = left.total_length + right.total_length;
        res.length = left.length + right.length;
        res.count = left.count + right.count;
        if (left.right_color == 1 && right.left_color == 1) {
            --res.count;
        }
        return res;
    }

    void push(Node* node) {
        if (node->has_assignment) {
            node->info.left_color = node->assign_lazy;
            node->info.right_color = node->assign_lazy;
            node->info.total_length = node->info.length * node->assign_lazy;
            node->info.count = node->assign_lazy;
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
        node->info = merge(node->left->info, node->right->info);
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
    
    SegmentInfo _range_query(Node *node, int l, int r) {
        push(node);
        if (node->l > r || node->r < l) return {0, 0, 0, 0, 0};
        if (node->l <= l && node->r <= r) return node->info;
        SegmentInfo left = _range_query(node->left, l, r);
        SegmentInfo right = _range_query(node->right, l, r);
        return merge(left, right);
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
    
    SegmentInfo getInfo() {
        return _range_query(root, root->l, root->r);
    }
};


void solution() {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    */
    int n;
    cin >> n;
    vector<long long> data(1000000);
    SegmentTree st(data);

    for (int i = 0; i < n; ++i) {
        char cmd;
        int l, r;
        cin >> cmd >> l >> r;
        l += 500000;
        if (cmd == 'W') {
            st.rangeAssign(l, l + r - 1, 0);
        } else {
            st.rangeAssign(l, l + r - 1, 1);
        }
        SegmentInfo output = st.getInfo();
        std::cout << output.count << " " << output.total_length << "\n";
    }
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    solution();

    return 0;
}