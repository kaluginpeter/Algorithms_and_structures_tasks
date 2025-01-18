#ifndef REMOTE_JUDGE
struct Node {
  Node* left;
  Node* right;
  int value;
  int size;
};
#endif

#ifdef REMOTE_JUDGE
#include "solution.h"
#endif
#include <cassert>
#include <utility>

int getSize(Node* node) {
  if (node == nullptr) {
    return 0;
  }
  return node->size;
}

std::pair<Node*, Node*> split(Node* root, int k) {
    /*
    Time Complexity O(H)
    Memory Complexity O(H)
    */
    if (!k) return {nullptr, root};
    int leftSize = getSize(root->left);
    if (leftSize < k) {
        auto [leftPart, rightPart] = split(root->right, k - leftSize - 1);
        root->right = leftPart;
        root->size = getSize(leftPart) + getSize(root->left) + 1;
        return {root, rightPart};
    }
    else {
        auto [leftPart, rightPart] = split(root->left, k);
        root->left = rightPart;
        root->size = getSize(rightPart) + getSize(root->right) + 1;
        return {leftPart, root};
    }
}

#ifndef REMOTE_JUDGE
void test() {
    Node node1({nullptr, nullptr, 3, 1});
    Node node2({nullptr, &node1, 2, 2});
    Node node3({nullptr, nullptr, 8, 1});
    Node node4({nullptr, nullptr, 11, 1});
    Node node5({&node3, &node4, 10, 3});
    Node node6({&node2, &node5, 5, 6});
    std::pair<Node*, Node*> res = split(&node6, 4);
    assert(res.first->size == 4);
    assert(res.second->size == 2);
}


int main() {
  test();
}
#endif