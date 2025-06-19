#include <iostream>
#include <vector>
#include <cstdint>

class SegmentTreeNode {
public:
    int l = 0, r = 0;
    SegmentTreeNode *left = nullptr, *right = nullptr;
    long long minVal = 0, minValCount = 0, rangeSum = 0, maxVal = 0;
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
            node->maxVal = data[l];
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
        node->rangeSum = node->left->rangeSum + node->right->rangeSum;
        node->maxVal = std::max(node->left->maxVal, node->right->maxVal);
    }
    
    void _update(SegmentTreeNode *node, int pos, int val) {
        if (node->l == node->r) {
            data[node->l] = val;
            node->minVal = val;
            node->minValCount = 1;
            node->maxVal = val;
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
    
    int _leftmostGreater(SegmentTreeNode *node, int x, int l) {
        if (node->r < l) return -1;
        if (node->maxVal < x) return -1;
        if (node->l == node->r) return node->l;
        
        int left_res = _leftmostGreater(node->left, x, l);
        if (left_res != -1) return left_res;
        return _leftmostGreater(node->right, x, l);
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
    int lefmostGreater(int x, int l) {
        return _leftmostGreater(root, x, l);
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
            std::printf("%d\n", st.lefmostGreater(x, y));
        }
    }
}

int main() {
    solution();
    return 0;
}