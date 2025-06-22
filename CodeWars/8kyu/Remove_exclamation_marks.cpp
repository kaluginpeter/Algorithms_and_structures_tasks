/*
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

FundamentalsStrings
*/
// Solution
#include <string>

std::string removeExclamationMarks(std::string str){
    std::string output = "";
    for (char &letter : str) {
        if (letter == '!') continue;
        output.push_back(letter);
    }
    return output;
}