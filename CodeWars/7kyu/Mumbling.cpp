/*
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.

FundamentalsStringsPuzzles
*/
// Solution
class Accumul
{
public:
    static std::string accum(const std::string &s) {
      std::string output = "";
      for (int i = 0; i < s.size(); ++i) {
        output.push_back(std::toupper(s[i]));
        for (int j = 0; j < i; ++j) output.push_back(std::tolower(s[i]));
        if (i + 1 != s.size()) output.push_back('-');
      }
      return output;
    };
};