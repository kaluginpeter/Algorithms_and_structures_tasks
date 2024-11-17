/*
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice

StringsFundamentals
*/
// Solution
#include <string>
#include <unordered_map>

std::size_t duplicateCount(const std::string& in)
{
  std::unordered_map<char, int> hashmap;
  for (char letter : in) {
    ++hashmap[std::tolower(letter)];
  }
  int duplicates = 0;
  for (auto& pair : hashmap) {
    if (pair.second > 1) {
      ++duplicates;
    }
  }
  return duplicates;
}