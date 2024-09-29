/*
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.

STRINGSFUNDAMENTALS
*/
// Solution
#include <map>
#include <string>

std::map<char, unsigned> count(const std::string& string) {
    std::map<char, unsigned> storage;
    for (char letter : string) {
      storage[letter]++;
    }
    return storage;
}