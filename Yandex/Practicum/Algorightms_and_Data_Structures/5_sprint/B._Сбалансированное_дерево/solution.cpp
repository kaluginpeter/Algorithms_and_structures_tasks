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


int dfs(const Node* root) {
    if (!root) {
        return 0;
    }
    int leftDepth = dfs(root->left);
    int rightDepth = dfs(root->right);
    if (leftDepth == INT32_MIN || rightDepth == INT32_MIN || std::abs(leftDepth - rightDepth) > 1) {
        return INT32_MIN;
    }
    return std::max(leftDepth, rightDepth) + 1;
}

bool Solution(const Node* root) {
    /*
    Time Complexity O(N)
    Memory Complexity O(H)
    */
    return dfs(root) != INT32_MIN;
}


#ifndef REMOTE_JUDGE
void test() {
    Node node1({1, nullptr, nullptr});
    Node node2({-5, nullptr, nullptr});
    Node node3({3, &node1, &node2});
    Node node4({10, nullptr, nullptr});
    Node node5({2, &node3, &node4});
    assert(Solution(&node5));
}

int main() {
  test();
}
#endif