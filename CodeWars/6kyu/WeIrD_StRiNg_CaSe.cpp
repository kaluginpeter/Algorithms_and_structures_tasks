/*
Write a function that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zeroth index is even, therefore that character should be upper cased. Indexing resets for each word. In other words, the first letter of every word is index 0 (even), so it must always be uppercase, etc.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

Examples:
"String" => "StRiNg"
"Weird string case" => "WeIrD StRiNg CaSe"
StringsAlgorithms
*/
// Solution
#include <string>
#include <string_view>
#include <cctype>

std::string to_weird_case(std::string_view str) {
    std::string result;
    result.reserve(str.size());

    int idx = 0;

    for (char ch : str) {
        if (ch == ' ') {
            result += ch;
            idx = 0;
        } else {
            if (idx % 2 == 0)
                result += std::toupper(static_cast<unsigned char>(ch));
            else
                result += std::tolower(static_cast<unsigned char>(ch));
            ++idx;
        }
    }

    return result;
}