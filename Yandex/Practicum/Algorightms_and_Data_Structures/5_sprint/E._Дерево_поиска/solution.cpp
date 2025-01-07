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

bool dfs(const Node* root, int minValue = INT32_MIN, int maxValue = INT32_MAX) {
    if (!root) {
        return true;
    } else if (root->value <= minValue || root->value >= maxValue) {
        return false;
    }
    return dfs(root->left, minValue, root->value) && dfs(root->right, root->value, maxValue);
};

bool Solution(const Node* root) {
    /*
    Time Complexity O(N)
    Memory Complexity O(H)
    */
    return dfs(root);
}


#ifndef REMOTE_JUDGE
void test() {
    {
      Node node1({1, nullptr, nullptr});
      Node node2({4, nullptr, nullptr});
      Node node3({3, &node1, &node2});
      Node node4({8, nullptr, nullptr});
      Node node5({5, &node3, &node4});
      assert(Solution(&node5));
    }
    {
      Node node1({1, nullptr, nullptr});
      Node node2({5, nullptr, nullptr});
      Node node3({3, &node1, &node2});
      Node node4({8, nullptr, nullptr});
      Node node5({5, &node3, &node4});
      assert(!Solution(&node5));
    }
}


int main() {
  test();
}
#endif