# Build the sequence which is defined as follows
#
# 1,
# 1, 2, 1,
# 1, 2, 3, 2, 1,
# 1, 2, 3, 4, 3, 2, 1,
# 1, 2, 3, 4, 5, 4, 3, 2, 1,
# 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1,
# 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1,
# 1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1,
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1,
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1,
# ...
# Task
# write a function solve(n, bound) which builds this sequence until an element in the sequnce equals bound (not including bound). Return the sum of every nth element of the sequence (not including the 0th element).
#
# Example
# solve(2, 4) produces the following sequence
#
# 1,
# 1, 2, 1,
# 1, 2, 3, 2, 1,
# 1, 2, 3,
#
# solve(2, 4) = 2 + 1 + 3 + 1 + 2 = 9
# Other examples
# solve(3, 3) = 1
# solve(2, 3) = 2 + 1 = 3
# Note
# bound will always be greater than 1 (bound>1)
#
# ALGORITHMS
# Python
def solve(n, bound):
    output: list[int] = [1]
    init: list[int] = [1]
    for module in range(2, bound):
        output.extend(init + [module] + init[::-1])
        init.append(module)
    output.extend(init)
    return sum(output[n::n])
# C++
#include <vector>

int solve(int n, int bound) {
  std::vector<int> output;
  for (int mod = 1; mod <= bound; ++mod) {
    for (int num = 1; num <= mod; ++num) {
      output.push_back(num);
    }
    if (mod == bound) {
      output.pop_back();
      break;
    }
    for (int num = mod - 1; num > 0; --num) {
      output.push_back(num);
    }
  }
  int sum = 0;
  for (size_t index = n; index < output.size(); index += static_cast<size_t>(n)) {
    sum += output[index];
  }
  return sum;
}