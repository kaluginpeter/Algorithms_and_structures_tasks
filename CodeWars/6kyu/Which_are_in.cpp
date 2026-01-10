/*
Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

Example 1:
a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]

Example 2:
a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []

Notes:
Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
Beware: In some languages r must be without duplicates.
ArraysListsStringsRefactoring
*/
// Solution
#include <unordered_set>
#include <vector>
#include <algorithm>
#include <string>
class WhichAreIn
{
  public:
  static std::vector<std::string> inArray(std::vector<std::string> &array1, std::vector<std::string> &array2) {
    std::unordered_set<std::string> hashset;
    for (std::string& x : array1) {
      for (std::string& y : array2) {
        if (y.find(x) != std::string::npos) hashset.insert(x);
      }
    }
    std::vector<std::string> output(hashset.begin(), hashset.end());
    std::sort(output.begin(), output.end());
    return output;
  }
};