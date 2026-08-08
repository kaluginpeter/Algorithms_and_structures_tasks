/*
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string (alphabetical ascending), the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
Fundamentals
*/
// Solution
package kata

import "strings"

func TwoToOne(s1 string, s2 string) string {
    var hashmap [26]int
    for _, char := range(s1) {
        hashmap[char - 'a']++
    }
    for _, char := range(s2) {
        hashmap[char - 'a']++
    }
    var output strings.Builder
    for i := 0; i < 26; i++ {
       if (hashmap[i] > 0) {
           output.WriteByte(byte(i + 'a'));
       }
    }
    return output.String()
}