/*
Write a function that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zeroth index is even, therefore that character should be upper cased. Indexing resets for each word. In other words, the first letter of every word is index 0 (even), so it must always be uppercase, etc.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

Examples:
"String" => "StRiNg"
"Weird string case" => "WeIrD StRiNg CaSe"
StringsAlgorithms
*/
// Solution
package kata

import (
	"strings"
	"unicode"
)

func toWeirdCase(str string) string {
	var result strings.Builder
	index := 0
	for _, ch := range str {
		if ch == ' ' {
			result.WriteRune(ch)
			index = 0
			continue
		}
		if index%2 == 0 {
			result.WriteRune(unicode.ToUpper(ch))
		} else {
			result.WriteRune(unicode.ToLower(ch))
		}
		index++
	}
	return result.String()
}