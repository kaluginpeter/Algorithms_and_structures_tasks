#include <iostream>
#include <vector>
#include <cstdint>

class SegmentTreeNode {
public:
    int l = 0, r = 0;
    SegmentTreeNode *left = nullptr, *right = nullptr;
    long long minVal = 0, minValCount = 0, rangeSum = 0;
    SegmentTreeNode(int l_, int r_) : l(l_), r(r_) {};
};

class SegmentTree {
public:
    std::vector<long long> data;
private:
    int n;
    
    SegmentTreeNode *root = nullptr;
    
    SegmentTreeNode *build(int l, int r) {
        SegmentTreeNode* node = new SegmentTreeNode(l, r);
        if (l == r) {
            node->minVal = data[l];
            node->minValCount = 1;
            node->rangeSum = data[l];
        } else {
            int middle = l + ((r - l) >> 1);
            node->left = build(l, middle);
            node->right = build(middle + 1, r);
            _push_up(node);
        }
        return node;
    }
    
    void _push_up(SegmentTreeNode *node) {
        node->rangeSum = node->left->rangeSum + node->right->rangeSum;
    }
    
    void _update(SegmentTreeNode *node, int pos, int val) {
        if (node->l == node->r) {
            data[node->l] = val;
            node->rangeSum = val;
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
    
    int _kOne(SegmentTreeNode *node, int k) {
        if (node->l == node->r) return node->l;
        if (node->left->rangeSum > k) return _kOne(node->left, k);
        return _kOne(node->right, k - node->left->rangeSum);
    }
    
public:
    SegmentTree(std::vector<long long> nums) : n(nums.size()), data(nums) {
        root = build(0, n - 1);
    }
    
    void update(int pos, int val) {
        _update(root, pos, val);
    }
    
    int kOne(int k) {
        return _kOne(root, k);
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
        int cmd, x;
        std::scanf("%d %d", &cmd, &x);
        if (cmd == 1) {
            st.update(x, 1 - st.data[x]);
        } else {
            std::printf("%d\n", st.kOne(x));
        }
    }
}

int main() {
    solution();
    return 0;
}