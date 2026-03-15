# Write an API that generates fancy sequences using the append, addAll, and multAll operations.
#
# Implement the Fancy class:
#
# Fancy() Initializes the object with an empty sequence.
# void append(val) Appends an integer val to the end of the sequence.
# void addAll(inc) Increments all existing values in the sequence by an integer inc.
# void multAll(m) Multiplies all existing values in the sequence by an integer m.
# int getIndex(idx) Gets the current value at index idx (0-indexed) of the sequence modulo 109 + 7. If the index is greater or equal than the length of the sequence, return -1.
#
#
# Example 1:
#
# Input
# ["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
# [[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
# Output
# [null, null, null, null, null, 10, null, null, null, 26, 34, 20]
#
# Explanation
# Fancy fancy = new Fancy();
# fancy.append(2);   // fancy sequence: [2]
# fancy.addAll(3);   // fancy sequence: [2+3] -> [5]
# fancy.append(7);   // fancy sequence: [5, 7]
# fancy.multAll(2);  // fancy sequence: [5*2, 7*2] -> [10, 14]
# fancy.getIndex(0); // return 10
# fancy.addAll(3);   // fancy sequence: [10+3, 14+3] -> [13, 17]
# fancy.append(10);  // fancy sequence: [13, 17, 10]
# fancy.multAll(2);  // fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
# fancy.getIndex(0); // return 26
# fancy.getIndex(1); // return 34
# fancy.getIndex(2); // return 20
#
#
# Constraints:
#
# 1 <= val, inc, m <= 100
# 0 <= idx <= 105
# At most 105 calls total will be made to append, addAll, multAll, and getIndex.
# Solution
# C++ O(4N) O(log2(N)) for each CRUD operation O(4N) SegmentTree
constexpr long long MOD = 1e9 + 7;
constexpr int N = 100000;
class Fancy {
public:
    std::vector<long long> tree, lazyMul, lazyAdd;
    uint32_t size = 0;
    Fancy() {
        tree.resize(4 * N, 0);
        lazyMul.resize(4 * N, 1);
        lazyAdd.resize(4 * N, 0);
    }

    void push(int node, int l, int r) {
        if (lazyMul[node] != 1 || lazyAdd[node] != 0) {
            tree[node] = (tree[node] * lazyMul[node] + (r - l + 1) * lazyAdd[node]) % MOD;
            if (l != r) {
                for (int child : {node * 2, node * 2 + 1}) {
                    lazyMul[child] = (lazyMul[child] * lazyMul[node]) % MOD;
                    lazyAdd[child] = (lazyAdd[child] * lazyMul[node] + lazyAdd[node]) % MOD;
                }
            }
            lazyMul[node] = 1;
            lazyAdd[node] = 0;
        }
    }

    void update(int node, int l, int r, int ql, int qr, long long mul, long long add) {
        push(node, l, r);
        if (r < ql || l > qr) return;
        if (ql <= l && r <= qr) {
            lazyMul[node] = (lazyMul[node] * mul) % MOD;
            lazyAdd[node] = (lazyAdd[node] * mul + add) % MOD;
            push(node, l, r);
            return;
        }
        uint32_t middle = l + ((r - l) >> 1);
        update(node * 2, l, middle, ql, qr, mul, add);
        update(node * 2 + 1, middle + 1, r, ql, qr, mul, add);
        tree[node] = (tree[node * 2] + tree[node * 2 + 1]) % MOD;
    }

    long long query(int node, int l, int r, int idx) {
        push(node, l, r);
        if (l == r) return tree[node];
        uint32_t middle = l + ((r - l) >> 1);
        if (idx <= middle) return query(node * 2, l, middle, idx);
        else return query(node * 2 + 1, middle + 1, r, idx);
    }

    void append(int val) {
        update(1, 0, N - 1, size, size, 1, val);
        ++size;
    }

    void addAll(int inc) {
        if (size) update(1, 0, N - 1, 0, size - 1, 1, inc);
    }

    void multAll(int m) {
        if (size) update(1, 0, N - 1, 0, size - 1, m, 0);
    }

    int getIndex(int idx) {
        if (idx >= size) return -1;
        return query(1, 0, N-1, idx);
    }
};