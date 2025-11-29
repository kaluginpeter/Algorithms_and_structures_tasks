/*
An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

Note: anagrams are case insensitive

Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

Examples
"foefet" is an anagram of "toffee"

"Buckethead" is an anagram of "DeathCubeK"

StringsFundamentals
*/
// Solution
#include <string>
#include <algorithm>
bool isAnagram(std::string test, std::string original){
  std::transform(test.begin(), test.end(), test.begin(), tolower);
  std::sort(test.begin(), test.end());
  std::transform(original.begin(), original.end(), original.begin(), tolower);
  std::sort(original.begin(), original.end());

  return test == original;
}