/*
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
Notes
Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

STRINGSARRAYSFUNDAMENTALS
*/
// Solution
#include <string>
#include <unordered_map>
std::string duplicate_encoder(const std::string& word){
  std::unordered_map<char, int> hashmap;
  for (char letter : word) {
    ++hashmap[std::tolower(letter)];
  }
  std::string output = word;
  for (size_t index = 0; index < output.size(); ++index) {
    if (hashmap[std::tolower(output[index])] == 1) {
      output[index] = '(';
    } else {
      output[index] = ')';
    }
  }
  return output;
}