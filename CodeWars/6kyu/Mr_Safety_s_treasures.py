# Introduction
# Mr. Safety loves numeric locks and his Nokia 3310. He locked almost everything in his house. He is so smart and he doesn't need to remember the combinations. He has an algorithm to generate new passcodes on his Nokia cell phone.
# postimage
#
# Task
# Can you crack his numeric locks? Mr. Safety's treasures wait for you. Write an algorithm to open his numeric locks. Can you do it without his Nokia 3310?
#
# Input
# The str or message (Python) input string consists of lowercase and upercase characters. It's a real object that you want to unlock.
#
# Output
# Return a string that only consists of digits.
# Example
# ``` unlock("Nokia") // => 66542 unlock("Valut") // => 82588 unlock("toilet") // => 864538 ```
# Puzzles
# Solution
#include <string>
using namespace std;

string unlock (string str)
{
  std::string output = "";
  for (char &s : str) {
    int pos = std::tolower(s) - 'a';
    output.push_back(std::min(9, 2 + pos / 3 - (pos == 18 || pos == 21? 1 : 0)) + '0');
  }
  return output;
}