/*
In this kata, you need to write a function that takes a string and a letter as input and then returns the index of the second occurrence of that letter in the string. If there is no such letter in the string, or if the letter occurs only once in the string, -1 should be returned.

Examples:

for inputs  "Hello world!!!", 'l'  ->  return 3
for inputs  "Hello world!!!", 'A'  ->  return -1
Good luck ;) And don't forget to rate this kata if you liked it.

FundamentalsStrings
*/
// Solution
#include <string>

int secondSymbol(const std::string& str, char symbol) {
  bool isSeen = false;
  for (int idx = 0; idx < str.size(); ++idx) {
    if (str[idx] == symbol) {
      if (isSeen) {
        return idx;
      }
      isSeen = true;
    }
  }
  return -1;
}