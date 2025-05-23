/*
Task
Given a string str, reverse it and omit all non-alphabetic characters.

Example
For str = "krishan", the output should be "nahsirk".

For str = "ultr53o?n", the output should be "nortlu".

Input/Output
[input] string str
A string consists of lowercase latin letters, digits and symbols.

[output] a string
Fundamentals
*/
// Solution
std::string reverse_letter(const std::string &str)
{
    std::string output = "", strCopy = str;;
    std::reverse(strCopy.begin(), strCopy.end());
    for (std::string::size_type i = 0; i < str.size(); ++i) {
      if (std::isalpha(strCopy[i])) output.push_back(strCopy[i]);
    }
    return output;
}