#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

class FenwickTree {
private:
    int size;
    vector<int> tree;

public:
    FenwickTree(int size) : size(size), tree(size + 2, 0) {}

    void update(int index, int delta = 1) {
        while (index <= size) {
            tree[index] += delta;
            index += index & -index;
        }
    }

    int query(int index) {
        int res = 0;
        while (index > 0) {
            res += tree[index];
            index -= index & -index;
        }
        return res;
    }
};


void solution() {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    */
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
    }
    vector<int> sorted_nums = nums;
    sort(sorted_nums.begin(), sorted_nums.end());
    sorted_nums.erase(unique(sorted_nums.begin(), sorted_nums.end()), sorted_nums.end());
    map<int, int> compressed;
    for (int i = 0; i < sorted_nums.size(); ++i) {
        compressed[sorted_nums[i]] = i + 1;
    }
    int max_compressed = sorted_nums.size();
    vector<int> nums_compressed(n);
    for (int i = 0; i < n; ++i) {
        nums_compressed[i] = compressed[nums[i]];
    }
    vector<int> left(n);
    FenwickTree ft_left(max_compressed);
    for (int i = 0; i < n; ++i) {
        left[i] = i - ft_left.query(nums_compressed[i]);
        ft_left.update(nums_compressed[i]);
    }
    vector<int> right(n);
    FenwickTree ft_right(max_compressed);
    for (int i = n - 1; i >= 0; --i) {
        right[i] = ft_right.query(nums_compressed[i] - 1);
        ft_right.update(nums_compressed[i]);
    }
    long long weakness = 0;
    for (int i = 0; i < n; ++i) {
        weakness += static_cast<long long>(left[i]) * right[i];
    }
    cout << weakness << '\n';
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    solution();
}