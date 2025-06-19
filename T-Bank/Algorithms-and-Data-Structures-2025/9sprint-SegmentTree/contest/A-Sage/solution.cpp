#include <iostream>
#include <vector>


class SegmentTree {
private:
    std::vector<long long> interval;
    int n;
public:
    SegmentTree(int n_) : n(n_), interval(3 * 100000, 0) {};

    void build(std::vector<int>& sequence) {
        for (int i = 0; i < sequence.size(); ++i) {
            interval[n + i] = static_cast<long long>(sequence[i]);
        }
        for (int i = n - 1; i > 0; --i) {
            interval[i] = interval[i << 1] + interval[i << 1 | 1];
        }
    }
    
    void update(int idx, int val) {
        interval[n + idx] = val;
        for (int i = idx + n; i > 1; i >>= 1) {
            interval[i >> 1] = interval[i] + interval[i ^ 1];
        }
    }
    
    long long getSum(int left, int right) {
        long long output = 0;
        for (int l = left + n, r = right + n; l < r; l >>= 1, r >>= 1) {
            if (l & 1) output += interval[l++];
            if (r & 1) output += interval[--r];
        }
        return output;
    }
};


void solution() {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    */
    int n, m;
    std::scanf("%d %d", &n, &m);
    SegmentTree st(n);
    std::vector<int> sequence(n, 0);
    for (int i = 0; i < n; ++i) std::scanf("%d", &sequence[i]);
    st.build(sequence);
    for (int i = 0; i < m; ++i) {
        int op, x, y;
        std::scanf("%d %d %d", &op, &x, &y);
        if (op == 1) st.update(x, y);
        else std::printf("%lld\n", st.getSum(x, y));
    }
}


int main() {
    solution();
}