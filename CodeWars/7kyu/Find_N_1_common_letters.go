/*
This kata is the small part of Quine-McCluskey algorithm.

All you have to do here is find prime implicants. Here 0 and 1 are replaced with lower/uppercase letters, "a" - truth, "A" - negation

Basically, towards this kata, it means to find all N-1 common characters between two terms(words) in string, where N is the length of term(word), so for "ABCDe ABcde abCDe" N will be 4, for "ABCD ABCd AbCD" N will be 3, etc. Every string will have the same number arguments(letters) in each word.

Examples and details:

Common letters in "ABCD ABCd" will be [ABC], for "ABCD ABCd AbCD" it will be [ABC ACD] etc. Also you should process exception when there's no N-1 common letters "AbCD Abcd aBCd abcD" -> []string{}. Repetitions in the initial s string don't count, so "ABCD ABCD aBcd" doesn't equal ["ABCD"], but equals []string{} There will not be empty strings. Final array should be sorted in alphabetical order, uppercase letters first, all repetitions in the final array should be deleted.

Algorithms

*/
// Solution
package kata

import (
	"sort"
	"strings"
)

func MinQuine(s string) []string {
	words := strings.Fields(s)

	seen := map[string]bool{}
	unique := make([]string, 0, len(words))
	for _, w := range words {
		if !seen[w] {
			seen[w] = true
			unique = append(unique, w)
		}
	}

	resultSet := map[string]bool{}
	for i := 0; i < len(unique); i++ {
		for j := i + 1; j < len(unique); j++ {
			a, b := unique[i], unique[j]
			if len(a) != len(b) {
				continue
			}
			diffCount := 0
			diffPos := -1
			for k := 0; k < len(a); k++ {
				if a[k] != b[k] {
					diffCount++
					diffPos = k
					if diffCount > 1 {
						break
					}
				}
			}
			if diffCount == 1 {
				merged := a[:diffPos] + a[diffPos+1:]
				resultSet[merged] = true
			}
		}
	}

	result := make([]string, 0, len(resultSet))
	for k := range resultSet {
		result = append(result, k)
	}
	sort.Strings(result)
	return result
}