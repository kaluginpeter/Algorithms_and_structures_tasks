#include <iostream>
#include <vector>
#include <unordered_map>
#include <stack>
#include <tuple>


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    int n, r;
    std::scanf("%d %d", &n, &r);
    std::vector<std::pair<int, int>> tree;
    for (int node = 0; node < n; ++node) {
        int left, right;
        std::scanf("%d %d", &left, &right);
        tree.push_back({left, right});
    }
    bool isValid = true;
    std::stack<std::tuple<int, int, int, int>> st;
    st.push({r, false, -1000000, 1000000});
    std::vector<int> heights (n, 0);
    while (!st.empty()) {
        auto [node, isVisited, minBound, maxBound] = st.top();
        st.pop();
        if (!isVisited) {
            if (node <= minBound || node >= maxBound) {
                isValid = false;
                break;
            }
            st.push({node, true, minBound, maxBound});
            if (tree[node].first != -1) {
                st.push({tree[node].first, false, minBound, node});
            }
            if (tree[node].second != -1) {
                st.push({tree[node].second, false, node, maxBound});
            }
        } else {
            int leftDepth = (tree[node].first != -1? heights[tree[node].first] : 0);
            int rightDepth = (tree[node].second != -1? heights[tree[node].second] : 0);
            if (std::abs(leftDepth - rightDepth) > 1) {
                isValid = false;
                break;
            }
            heights[node] = std::max(leftDepth, rightDepth) + 1;
        }
    }
    std::cout << (isValid? '1' : '0') << '\n';
}


int main() {
    solution();
}