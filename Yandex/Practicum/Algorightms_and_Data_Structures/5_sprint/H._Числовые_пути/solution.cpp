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
#include <string>
#include <cassert>

using namespace std;


void dfs(const Node* root, std::string& path, int& totalSum) {
    path += std::to_string(root->value);
    if (!root->left && !root->right) totalSum += std::stoi(path);
    if (root->left) dfs(root->left, path, totalSum);
    if (root->right) dfs(root->right, path, totalSum);
    path.pop_back();
}


int Solution(const Node* root) {
    /*
    Time Complexity O(N)
    Memory Complexity O(H)
    */
    int totalSum = 0;
    std::string path = "";
    if (root) dfs(root, path, totalSum);
    return totalSum;
}

#ifndef REMOTE_JUDGE
void test() {
    Node node1({2, nullptr, nullptr});
    Node node2({1, nullptr, nullptr});
    Node node3({3, &node1, &node2});
    Node node4({2, nullptr, nullptr});
    Node node5({1, &node4, &node3});
    assert(Solution(&node5) == 275);
}

int main() {
  test();
}
#endif