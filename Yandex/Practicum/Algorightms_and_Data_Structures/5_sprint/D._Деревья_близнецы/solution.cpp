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

using namespace std;


bool Solution(const Node* root1, const Node* root2) {
    /*
    Time Complexity O(N)
    Memory Complexity O(H)
    */
    if (!root1 && !root2) return true;
    if (
        (root1 && !root2)
        || (!root1 && root2)
        || (root1->value != root2->value)
    ) return false;
    return Solution(root1->left, root2->left) && Solution(root1->right, root2->right);
}

#ifndef REMOTE_JUDGE
void test() {

    Node node1({1, nullptr, nullptr});
    Node node2({2, nullptr, nullptr});
    Node node3({3, &node1, &node2});

    Node node4({1, nullptr, nullptr});
    Node node5({2, nullptr, nullptr});
    Node node6({3, &node4, &node5});
    assert(Solution(&node3, &node6));
}

int main() {
  test();
}
#endif