/*
We need to sum big numbers and we require your help.

Write a function that returns the sum of two numbers. The input numbers are strings and the function must return a string.

Example
add("123", "321"); -> "444"
add("11", "99");   -> "110"
Notes
The input numbers are big.
The input is a string of only digits
The numbers are positives
MathematicsBig IntegersAlgorithms
*/
// Solution
#include <string>

std::string add(const std::string& a, const std::string& b) {
  int aN = a.size();
  int bN = b.size();
  std::string x = a;
  std::string y = b;
  if (aN < bN) {
    std::string temp = y;
    int tempN = bN;
    y = x;
    x = temp;
    bN = aN;
    aN = tempN;
  }
  std::string output = "";
  int additional = 0;
  int bIdx = bN - 1;
  for (int aIdx = aN - 1; aIdx >= 0; --aIdx) {
    if (bIdx >= 0) {
      int sum = (x[aIdx] - '0') + (y[bIdx] - '0') + additional;
      additional = 0;
      if (sum > 9) {
        additional = sum / 10;
      }
      output += std::to_string(sum % 10);
      --bIdx;
    } else {
      int sum = (x[aIdx] - '0') + additional;
      additional = 0;
      if (sum > 9) {
        additional = sum / 10;
      }
      output += std::to_string(sum % 10);
    }
  }
  if (additional) {
    output += std::to_string(additional);
  }
  int left = 0;
  int right = output.size() - 1;
  while (left < right) {
    char temp = output[right];
    output[right] = output[left];
    output[left] = temp;
    ++left;
    --right;
  }
  return output;
}