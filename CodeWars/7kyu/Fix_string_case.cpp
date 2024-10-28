/*
In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:

make as few changes as possible.
if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
For example:

solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
solve("coDE") = "code". Upper == lowercase. Change all to lowercase.
More examples in test cases. Good luck!

Please also try:

Simple time difference

Simple remove duplicates

Fundamentals
*/
// Solution
#include <string>

std::string solve(const std::string& str){
  std::string str_ = str;
  int upperCount = 0;
  int lowerCount = 0;
  for (char letter : str_) {
    if (std::isupper(letter)) {
      ++upperCount;
    } else {
      ++lowerCount;
    }
  }
  bool toLower = lowerCount >= upperCount;
  for (size_t index = 0; index < str_.size(); ++index) {
    if (toLower) {
      str_[index] = std::tolower(str_[index]);
    } else {
      str_[index] = std::toupper(str_[index]);
    }
  }
  return str_;
}