/*
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
FUNDAMENTALSARRAYS
*/
// Solution
#include <vector>
int grow(std::vector<int> nums) {
  int accumulate = 1;
  for (int num : nums) {
    accumulate *= num;
  }
  return accumulate;
}