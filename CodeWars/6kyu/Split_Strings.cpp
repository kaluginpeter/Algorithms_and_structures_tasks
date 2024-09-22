/*
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
REGULAR EXPRESSIONSSTRINGSALGORITHMS
*/
// Solution
#include <string>
#include <vector>

std::vector<std::string> solution(const std::string &s)
{
    std::vector<std::string> storage;
    bool is_odd = s.size() % 2 == 1;
    for (size_t index = 0; index < s.size(); index += 2) {
        std::string pair;
        if (index == s.size() - 1 && is_odd) {
            pair = s[index];
            pair += '_';
        } else {
            pair = s[index];
            pair += s[index + 1];
        }
        storage.push_back(pair);
    }
    return storage;
}