/*
Your task is to return an output string that translates an input string s by replacing each character in s with a number representing the number of times that character occurs in s and separating each number with the sep character(s).

Example (s, sep --> Output)

"hello world", "-" --> "1-1-3-3-2-1-1-2-1-3-1"
"19999999"   , ":" --> "1:7:7:7:7:7:7:7"
"^^^**$"     , "x" --> "3x3x3x2x2x1"
StringsFundamentals
*/
// Solution
package kata

func FreqSeq(str string, sep string) string {
  var hashmap map[rune]int = map[rune]int{}
  for _, ch := range str {
    hashmap[ch]++
  }
  var output []byte = []byte{}
  for _, ch := range str {
    output = append(output, byte(rune(hashmap[ch]) + '0'))
    for _, ch := range sep { output = append(output, byte(ch)) }
  }
  if len(output) > 0 { output = output[:len(output) - len(sep)]}
  return string(output)
}