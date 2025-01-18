#ifndef REMOTE_JUDGE
struct Node {
  int value;
  const Node* left = nullptr;
  const Node* right = nullptr;
  Node(int value, Node* left, Node* right) : value(value), left(left), right(right) {}
};
#endif

#ifdef REMOTE_JUDGE
#include "solution_tree.h"
#endif
#include <cmath>
#include <iostream>
#include <cassert>
#include <cstdint>
using namespace std;


int dfs(const Node* root, int& maxSum) {
    if (!root) return INT32_MIN;
    int leftSum = std::max(dfs(root->left, maxSum), 0);
    int rightSum = std::max(dfs(root->right, maxSum), 0);
    maxSum = std::max(
        maxSum, root->value + leftSum + rightSum
    );
    return root->value + std::max(leftSum, rightSum);
}


int Solution(const Node* root) {
    /*
    Time Complexity O(N)
    Memory Complexity O(H)
    */
    int maxSum = INT32_MIN;
    dfs(root, maxSum);
    return maxSum;
}

#ifndef REMOTE_JUDGE
void test() {
    Node node1({5, nullptr, nullptr});
    Node node2({1, nullptr, nullptr});
    Node node3({-3, &node2, &node1});
    Node node4({2, nullptr, nullptr});
    Node node5({2, &node4, &node3});
    assert(Solution(&node5) == 6);
}

int main() {
  test();
}
#endif