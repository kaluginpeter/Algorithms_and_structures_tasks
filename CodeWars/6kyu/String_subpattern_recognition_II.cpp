/*
Similarly to the previous kata, you will need to return a boolean value if the base string can be expressed as the repetition of one subpattern.

This time there are two small changes:

if a subpattern has been used, it will be present at least twice, meaning the subpattern has to be shorter than the original string;
the strings you will be given might or might not be created repeating a given subpattern, then shuffling the result.
For example:

"a" --> false; //no repeated shorter sub-pattern, just one character
"aaaa" --> true; //just one character repeated
"abcd" --> false; //no repetitions
"babababababababa" --> true; //repeated "ba"
"bbabbaaabbaaaabb" --> true; //same as above, just shuffled
Strings will never be empty and can be composed of any character (just consider upper- and lowercase letters as different entities) and can be pretty long (keep an eye on performances!).

If you liked it, go for either the previous kata or the next kata of the series!

StringsRegular ExpressionsFundamentals
*/
// Solution
#include <unordered_map>
bool hasSubpattern(const std::string& str){
  if (str.size() == 1) return false;
  std::unordered_map<char, int> hashmap;
  for (const char& ch : str) {
    ++hashmap[ch];
  }
  int y = 0;
  for (auto& p : hashmap) {
    y = std::max(y, p.second);
  }
  for (int d = 1; d <= y; ++d) {
    bool isValid = true;
    for (auto& p : hashmap) {
      if (p.second % d != 0) {
        isValid = false;
        break;
      }
    }
    if (isValid) {
      if (d > 1 || (d == 1 && hashmap.size() == 1)) return true;
    }
  }
  return false;
}