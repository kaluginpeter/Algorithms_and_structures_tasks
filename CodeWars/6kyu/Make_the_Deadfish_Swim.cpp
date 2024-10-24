/*
Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
Invalid characters should be ignored.

parse("iiisdoso") => [ 8, 64 ]
PARSINGALGORITHMS
*/
// Solution
#include <vector>
#include <string>

std::vector<int> parse(const std::string &data) {
  std::vector<int> output;
  int startValue = 0;
  for (char letter : data) {
    if (letter == 'i') {
      ++startValue;
    } else if (letter == 'd') {
      --startValue;
    } else if (letter == 's') {
      startValue *= startValue;
    } else if (letter == 'o') {
      output.push_back(startValue);
    }
  }
  return output;
}