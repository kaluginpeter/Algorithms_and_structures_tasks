/*
Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

Example 1:
a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]

Example 2:
a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []

Notes:
Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
Beware: In some languages r must be without duplicates.
ArraysListsStringsRefactoring
*/
// Solution
package kata

import (
  "strings"
  "slices"
)

func InArray(array1 []string, array2 []string) []string {
  var output []string = []string{}
  slices.Sort(array1)
  for _, target := range array1 {
    if len(output) > 0 && target == output[len(output) - 1] { continue }
    for _, data := range array2 {
      if strings.Contains(data, target) {
        output = append(output, target)
        break
      }
    }
  }
  return output
}