/*
You are given two strings. In a single move, you can choose any of them, and delete the first (i.e. leftmost) character.

For Example:

By applying a move to the string "where", the result is the string "here".
By applying a move to the string "a", the result is an empty string "".
Implement a function that calculates the minimum number of moves that should be performed to make the given strings equal.

Notes
Both strings consist of lowercase latin letters.
If the string is already empty, you cannot perform any more delete operations.
Fundamentals
*/
// Solution
#include <string>
long long shiftLeft(std::string s, std::string t){
  int left = 0, right = 0;
  int n = s.size(), m = t.size();
  long long output = 0;
  while (left < n && right < m) {
    if (s.substr(left, n - left) != t.substr(right, m - right)) {
      if ((n - left) > (m - right)) ++left;
      else if ((n - left) < (m - right)) ++right;
      else {
        ++output;
        ++left;
        ++right;
      }
      ++output;
    } else break;
  }
  return ((n - left) == (m - right))? output : output + (n - left) + (m - right);
}