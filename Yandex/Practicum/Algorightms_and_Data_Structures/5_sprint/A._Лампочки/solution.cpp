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
#include <vector>
#include <cstdint>

using namespace std;


int Solution(const Node* root) {
    /*
    Time Complexity O(N)
    Memory Complexity O(H)
    */
    int maxVal = INT32_MIN;
    std::vector<const Node*> curNodes = {root};
    std::vector<const Node*> nextNodes;
    while (curNodes.size() > 0) {
        for (const Node* node : curNodes) {
            maxVal = std::max(maxVal, node->value);
            if (node->left) {
                nextNodes.push_back(node->left);
            }
            if (node->right) {
                nextNodes.push_back(node->right);
            }
        }
        curNodes = nextNodes;
        nextNodes = {};
    }
    return maxVal;
}

#ifndef REMOTE_JUDGE
void test() {
    Node node1({1, nullptr, nullptr});
    Node node2({-5, nullptr, nullptr});
    Node node3({3, &node1, &node2});
    Node node4({2, &node3, nullptr});
    assert(Solution(&node4) == 3);
}

int main() {
  test();
}
#endif