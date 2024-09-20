/*
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.

ARRAYSFUNDAMENTALS
*/
// Solution
#include <vector>

long sumTwoSmallestNumbers(std::vector<int> numbers)
{
    long int first = std::min(numbers[0], numbers[1]);
    long int second = std::max(numbers[0], numbers[1]);
    for (size_t idx = 2; idx < numbers.size(); ++idx) {
      if (first >= numbers[idx]) {
          second = first;
          first = numbers[idx];
      } else if (second > numbers[idx])  {
          second = numbers[idx];
      }
    }
    return first + second;
}