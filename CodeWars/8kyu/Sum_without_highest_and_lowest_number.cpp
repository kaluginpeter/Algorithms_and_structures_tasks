# Task
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.

Example
{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6
Input validation
If an empty value ( null, None, Nothing, nil etc. ) is given instead of an array, or the given array is an empty list or a list with only 1 element, return 0.

FUNDAMENTALS
#include<vector>
using namespace std;

int sum(vector<int> numbers)
{
  if (numbers.size() < 2) {
    return 0;
  }
  int total_sum = 0, min_num = numbers[1], max_num = numbers[1];
  for (size_t index = 0; index < numbers.size(); ++index) {
    total_sum += numbers[index];
    if (min_num > numbers[index]) {
      min_num = numbers[index];
    }
    if (max_num < numbers[index]) {
      max_num = numbers[index];
    }
  }
  return total_sum - min_num - max_num;
}