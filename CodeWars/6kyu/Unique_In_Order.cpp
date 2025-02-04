/*
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

uniqueInOrder("AAAABBBCCDAABBB") == {'A', 'B', 'C', 'D', 'A', 'B'}
uniqueInOrder("ABBCcAD")         == {'A', 'B', 'C', 'c', 'A', 'D'}
uniqueInOrder([1,2,2,3,3])       == {1,2,3}
AlgorithmsFundamentals
*/
// Solution
#include <string>
#include <vector>

template <typename T> std::vector<T> uniqueInOrder(const std::vector<T>& iterable){
  std::vector<T> output;
  int n = iterable.size();
  for (int i = 0; i < n; ++i) {
    if (!i || iterable[i - 1] != iterable[i]) output.push_back(iterable[i]);
  }
  return output;
}
std::vector<char> uniqueInOrder(const std::string& iterable){
  std::vector<char> output;
  int n = iterable.size();
  for (int i = 0; i < n; ++i) {
    if (!i || iterable[i - 1] != iterable[i]) output.push_back(iterable[i]);
  }
  return output;
}