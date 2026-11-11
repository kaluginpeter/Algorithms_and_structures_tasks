/*
John has invited some friends. His list is:

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
Could you make a program that

makes this string uppercase
gives it sorted in alphabetical order by last name.
When the last names are the same, sort them by first name. Last name and first name of a guest come in the result between parentheses separated by a comma.

So the result of function meeting(s) will be:

"(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"
It can happen that in two distinct families with the same family name two people have the same first name too.

Notes
You can see another examples in the "Sample tests".
Fundamentals
*/
// Solution
package kata

import (
	"sort"
	"strings"
)

func Meeting(s string) string {
	s = strings.ToUpper(s)
	var n, ptr int = len(s), 0
	var entries []string

	for ptr < n {
		start := ptr
		for s[ptr] != ':' {
			ptr++
		}
		first := s[start:ptr]
		ptr++

		start = ptr
		for ptr < n && s[ptr] != ';' {
			ptr++
		}
		last := s[start:ptr]
		ptr++

		entries = append(entries, "("+last+", "+first+")")
	}

	sort.Strings(entries)
	return strings.Join(entries, "")
}