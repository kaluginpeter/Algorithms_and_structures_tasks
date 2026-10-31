/*
Write a function that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input "stress", the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase characters are considered the same character, but the function should return the correct case for the initial character. For example, the input "sTreSS" should return "T".

If a string contains only repeating characters, return an empty string ("");

Note: despite its name in some languages, your function should handle any Unicode codepoint:

"@#@@*"    --> "#"
"かか何"   --> "何"
"🐐🦊🐐" --> "🦊"
StringsAlgorithms
*/
package kata

import "unicode"

func FirstNonRepeating(str string) string {
  var seen map[rune]int = map[rune]int{}
  for _, ch := range str {
    seen[unicode.ToLower(ch)]++
  }
	for _, ch := range str {
    if seen[unicode.ToLower(ch)] == 1 { return string(ch) }
  }
	return ""
}