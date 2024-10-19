/*
The vowel substrings in the word codewarriors are o,e,a,io. The longest of these has a length of 2. Given a lowercase string that has alphabetic characters only (both vowels and consonants) and no spaces, return the length of the longest vowel substring. Vowels are any of aeiou.

Good luck!

If you like substring Katas, please try:

Non-even substrings

Vowel-consonant lexicon

STRINGSFUNDAMENTALS
*/
// Solution
#include <unordered_set>
using namespace std;

int solve(string s){
	int answer = 0;
  int curr = 0;
  unordered_set<char> vowels({'a', 'e', 'o', 'u', 'i'});
  for (char letter : s) {
    if (!vowels.count(letter)) {
      curr = 0;
    } else {
      ++curr;
    }
    answer = max(answer, curr);
  }
  return answer;
}