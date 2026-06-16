/*
Given a node object representing a binary tree:

struct node
{
  int value;
  node* left;
  node* right;
}
write a function that returns the sum of all values, including the root. Absence of a node will be indicated with a null value.

Examples:

10
| \
1  2
=> 13

1
| \
0  0
    \
     2
=> 3
TreesRecursionBinary TreesBinary Search TreesData StructuresFundamentals
*/
// Solution
// Return the sum of all values in the tree, including the root
void dfs(node* root, int& output) {
    if (!root) return;
    output += root->value;
    dfs(root->left, output);
    dfs(root->right, output);
}
int sumTheTreeValues(node* root) {
    int output = 0;
    dfs(root, output);
    return output;
}