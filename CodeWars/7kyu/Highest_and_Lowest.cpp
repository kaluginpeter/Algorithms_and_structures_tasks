/*
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples
Input: "1 2 3 4 5"   =>  Output: "5 1"
Input: "1 2 -3 4 5"  =>  Output: "5 -3"
Input: "1 9 3 4 -5"  =>  Output: "9 -5"
Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
FUNDAMENTALSSTRINGS
*/
// Soliution
#include <string>
#include <sstream>

std::string highAndLow(const std::string& numbers){
  std::istringstream iss(numbers);
  int min_number = 10e7;
  int max_number = -10e7;
  int number;
  while (iss >> number) {
    min_number = std::min(min_number, number);
    max_number = std::max(max_number, number);
  }
  return std::to_string(max_number) + " " + std::to_string(min_number);
}