# Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

STRINGSFUNDAMENTALS
// Solution
#include <string>

using namespace std;

int getCount(const string& inputStr){
  int num_vowels = 0;
  string vowels = "aeoiu";
  for (auto letter : inputStr) {
    auto index_of_element = find(vowels.begin(), vowels.end(), letter);
    if (index_of_element != vowels.end()) {
      num_vowels += 1;
    }
  }
  return num_vowels;
}