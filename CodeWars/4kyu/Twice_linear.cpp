/*
Consider a sequence u where u is defined as follows:

The number u(0) = 1 is the first one in u.
For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
There are no other numbers in u.
Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

Task:
Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).

Example:
dbl_linear(10) should return 22

Note:
Focus attention on efficiency

MathematicsAlgorithms
*/
// Solution
#include <unordered_set>
#include <queue>
#include <vector>
class DoubleLinear
{
public:
    static int dblLinear(int n) {
      std::unordered_set<int> uSet;
      std::priority_queue<int, std::vector<int>, std::greater<int>> uHeap;
      uSet.insert(1);
      uHeap.push(1);
      for (int i = 0; i < n; ++i) {
        int sm = uHeap.top();
        uHeap.pop();
        int y = 2 * sm + 1;
        int z = 3 * sm + 1;
        if (!uSet.count(y)) {
          uSet.insert(y);
          uHeap.push(y);
        }
        if (!uSet.count(z)) {
          uSet.insert(z);
          uHeap.push(z);
        }
      }
      return uHeap.top();
    };
};