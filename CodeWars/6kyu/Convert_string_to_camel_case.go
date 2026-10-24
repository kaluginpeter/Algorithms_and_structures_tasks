/*
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"

Regular ExpressionsAlgorithmsStrings
*/
// Solution
package kata

import "unicode"

func ToCamelCase(s string) string {
	var output, bucket []byte = []byte{}, []byte{}
  for _, ch := range s {
    if ch == '_' || ch == '-' {
      output = append(output, bucket...)
      bucket = bucket[:0]
    } else {
      if len(output) == 0 || len(bucket) > 0 {
        bucket = append(bucket, byte(ch))
      } else { bucket = append(bucket, byte(unicode.ToUpper(ch)))}
    }
  }
  output = append(output, bucket...)
  return string(output)
}