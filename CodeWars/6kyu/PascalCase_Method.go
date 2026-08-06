/*
Write a method (or function, depending on the language) that converts a string to PascalCase, that is, all words must have their first letter capitalized and spaces must be removed.

Examples (input --> output):
"hello case" --> "HelloCase"
"pascal case word" --> "PascalCaseWord"
Don't forget to rate this kata! Thanks :)

Note: for historical reasons, the function is named camelCase() or similar in some languages, but it should actually perform conversion to PascalCase.

FundamentalsAlgorithmsStrings
*/
// Solution
package kata

import (
  "strings"
)

func CamelCase(s string) string {
    var output strings.Builder
    var i int = 0
    for i < len(s) {
        for i < len(s) && s[i] == ' ' {
            i++
        }
        var was bool = false
        for i < len(s) && s[i] != ' ' {
            if !was {
                output.WriteByte(s[i] - 'a' + 'A')
                was = true
            } else {
                output.WriteByte(s[i])
            }
            i++
        }
    }
    return output.String()
}