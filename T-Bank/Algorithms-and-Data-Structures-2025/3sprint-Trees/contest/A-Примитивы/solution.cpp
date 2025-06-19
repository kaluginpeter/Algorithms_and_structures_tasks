#include <iostream>
#include <unordered_map>
#include <vector>
#include <stack>
#include <string>


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    int n;
    std::scanf("%d", &n);
    std::unordered_map<int, std::vector<int>> tree;
    for (int i = 0; i < n - 1; ++i) {
        int parent;
        std::scanf("%d", &parent);
        tree[parent].push_back(i + 1);
    }
    // Calculate depth of the tree and height of each node
    std::vector<int> heights (n, 0);
    std::vector<int> curNodes = {0};
    std::vector<int> nextNodes;
    int treeHeight = -1;
    while (!curNodes.empty()) {
        ++treeHeight;
        for (int& parent : curNodes) {
            for (int& child : tree[parent]) {
                nextNodes.push_back(child);
            }
            heights[parent] = treeHeight;
        }
        curNodes = nextNodes;
        nextNodes.clear();
    }
    // Calculate longest diameter in the tree
    int maxDiameter = 0;
    std::stack<std::pair<int, bool>> st;
    std::vector<int> maxHeights (n + 1, 0);
    st.push({0, false});
    while (!st.empty()) {
        auto [node, isVisited] = st.top(); 
        st.pop();

        if (!isVisited) {
            st.push({node, true});
            for (int child : tree[node]) {
                st.push({child, false});
            }
        } else {
            int leftDepth = 0, rightDepth = 0;
            for (int& child : tree[node]) {
                if (maxHeights[child] > leftDepth) {
                    rightDepth = leftDepth;
                    leftDepth = maxHeights[child];
                } else if (maxHeights[child] > rightDepth) {
                    rightDepth = maxHeights[child];
                }
            }
            maxDiameter = std::max(maxDiameter, leftDepth + rightDepth);
            maxHeights[node] = std::max(leftDepth, rightDepth) + 1;
        }
    }
    // Print the answer
    std::printf("%d %d\n", treeHeight, maxDiameter);
    for (int i = 0; i < n; ++i) {
        if (i) std::printf(" ");
        std::printf("%d", heights[i]);
    }
    std::printf("\n");
}


int main() {
    solution();
}