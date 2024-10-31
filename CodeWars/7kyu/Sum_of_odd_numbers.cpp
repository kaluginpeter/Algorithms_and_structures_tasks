/*
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8
ArraysListsMathematicsFundamentals
*/
// Solution
#include <cmath>
long long rowSumOddNumbers(unsigned n){
  unsigned int start = std::pow(n, 2) - (n - 1);
  unsigned int totalSum = 0;
  for (unsigned int num = start; num < start + n * 2; num += 2) {
    totalSum += num;
  }
  return totalSum;
}