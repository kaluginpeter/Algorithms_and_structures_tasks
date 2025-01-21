/*
How can you tell an extrovert from an introvert at NSA?
Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

Test examples:

"EBG13 rknzcyr." -> "ROT13 example."

"This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"
StringsCiphersRegular ExpressionsAlgorithms
*/
// Solution
#include <string>
char rot13(char ch) {
    if ('a' <= ch && ch <= 'z') {
        // Shift lowercase letters
        return (ch - 'a' + 13) % 26 + 'a';
    } else if ('A' <= ch && ch <= 'Z') {
        // Shift uppercase letters
        return (ch - 'A' + 13) % 26 + 'A';
    } else {
        // Non-alphabetical characters remain unchanged
        return ch;
    }
}
std::string rot13(const std::string& str) {
  std::string output = "";
  for (unsigned long idx = 0; idx < str.size(); ++idx) {
    output += rot13(str[idx]);
  }
  return output;
}
