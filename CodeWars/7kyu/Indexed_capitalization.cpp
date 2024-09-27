/*
Given a string and an array of integers representing indices, capitalize all letters at the given indices.

For example:

capitalize("abcdef",[1,2,5]) = "aBCdeF"
capitalize("abcdef",[1,2,5,100]) = "aBCdeF". There is no index 100.
The input will be a lowercase string with no spaces and an array of digits.

Good luck!

Be sure to also try:

Alternate capitalization

String array revisal

FUNDAMENTALS
*/
// Solution
std::string capitalize(std::string s, std::vector<int> idxs)
{
  for (int index : idxs) {
    if (index >= s.size()) {
      continue;
    }
    s[index] = std::toupper(s[index]);
  }
  return s;
}