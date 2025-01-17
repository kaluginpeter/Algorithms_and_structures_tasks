/*
It started as a discussion with a friend, who didn't fully grasp some way of setting defaults, but I thought the idea was cool enough for a beginner kata: binary OR each matching element of two given arrays (or lists, if you do it in Python; vectors in c++) of integers and give the resulting ORed array [starts to sound like a tonguetwister, doesn't it?].

If one array is shorter than the other, use the optional third parameter (defaulted to 0) to OR the unmatched elements.

For example:

orArrays([1,2,3],[1,2,3]) == [1,2,3]
orArrays([1,2,3],[4,5,6]) == [5,7,7]
orArrays([1,2,3],[1,2]) == [1,2,3]
orArrays([1,2],[1,2,3]) == [1,2,3]
orArrays([1,2,3],[1,2,3],3) == [1,2,3]
ArraysListsBinaryFundamentals
*/
// Solution
#include <vector>

std::vector<int> orArrays(const std::vector<int>& arr1, const std::vector<int>& arr2, int separator = 0){
  unsigned long left = 0;
  unsigned long right = 0;
  std::vector<int> output;
  while (left < arr1.size() && right < arr2.size()) {
    output.push_back(arr1[left] | arr2[right]);
    ++left;
    ++right;
  }
  if (arr1.size() != arr2.size()) {
    while (right < arr2.size()) {
      output.push_back(separator | arr2[right]);
      ++right;
    }
    while (left < arr1.size()) {
      output.push_back(separator | arr1[left]);
      ++left;
    }
  }
  return output;
}