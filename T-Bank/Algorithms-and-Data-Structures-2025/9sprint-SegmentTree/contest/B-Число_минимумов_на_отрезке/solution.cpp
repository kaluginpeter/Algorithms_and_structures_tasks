#include <iostream>
#include <vector>
#include <cstdint>

class SegmentTreeNode {
public:
    int l = 0, r = 0;
    SegmentTreeNode *left = nullptr, *right = nullptr;
    long long minVal = 0, minValCount = 0;
    SegmentTreeNode(int l_, int r_) : l(l_), r(r_) {};
};

class SegmentTree {
private:
    int n;
    std::vector<long long> data;
    SegmentTreeNode *root = nullptr;
    
    SegmentTreeNode *build(int l, int r) {
        SegmentTreeNode* node = new SegmentTreeNode(l, r);
        if (l == r) {
            node->minVal = data[l];
            node->minValCount = 1;
        } else {
            int middle = l + ((r - l) >> 1);
            node->left = build(l, middle);
            node->right = build(middle + 1, r);
            _push_up(node);
        }
        return node;
    }
    
    void _push_up(SegmentTreeNode *node) {
        if (node->left->minVal < node->right->minVal) {
            node->minVal = node->left->minVal;
            node->minValCount = node->left->minValCount;
        } else if (node->left->minVal > node->right->minVal) {
            node->minVal = node->right->minVal;
            node->minValCount = node->right->minValCount;
        } else {
            node->minVal = node->left->minVal;
            node->minValCount = node->left->minValCount + node->right->minValCount;
        }
    }
    
    void _update(SegmentTreeNode *node, int pos, int val) {
        if (node->l == node->r) {
            data[node->l] = val;
            node->minVal = val;
            node->minValCount = 1;
            return;
        }
        int middle = node->l + ((node->r - node->l) >> 1);
        if (pos <= middle) {
            _update(node->left, pos, val);
        } else {
            _update(node->right, pos, val);
        }
        _push_up(node);
    }
    
    std::pair<long long, long long> _minOnRange(SegmentTreeNode *node, int left, int right) {
        if (node->r < left || node->l > right) return {INT64_MAX, 0};
        if (left <= node->l && node->r <= right) return {node->minVal, node->minValCount};
        std::pair<long long, long long> l = _minOnRange(node->left, left, right);
        std::pair<long long, long long> r = _minOnRange(node->right, left, right);
        if (l.first < r.first) return l;
        else if (l.first > r.first) return r;
        else return {l.first, l.second + r.second};
    }
    
public:
    SegmentTree(std::vector<long long> nums) : n(nums.size()), data(nums) {
        root = build(0, n - 1);
    }
    
    void update(int pos, int val) {
        _update(root, pos, val);
    }
    
    std::pair<long long, long long> minOnRange(int left, int right) {
        return _minOnRange(root, left, right - 1);
    }
};

void solution() {
    /*
    Time Complexity O(N + MlogN)
    Memory Complexity O(N)
    */
    int n, m;
    std::scanf("%d %d", &n, &m);
    std::vector<long long> nums(n);
    for (int i = 0; i < n; ++i) std::scanf("%lld", &nums[i]);
    SegmentTree st(nums);
    for (int i = 0; i < m; ++i) {
        int cmd, x, y;
        std::scanf("%d %d %d", &cmd, &x, &y);
        if (cmd == 1) {
            st.update(x, y);
        } else {
            std::pair<long long, long long> p = st.minOnRange(x, y);
            std::printf("%lld %lld\n", p.first, p.second);
        }
    }
}

int main() {
    solution();
    return 0;
}