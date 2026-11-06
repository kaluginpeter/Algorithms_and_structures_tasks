/*
The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).

If the sum of a chunk's digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.

If

sz is <= 0 or if str == "" return ""
sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".
Examples:
("123456987654", 6) --> "234561876549"
("123456987653", 6) --> "234561356789"
("66443875", 4) --> "44668753"
("66443875", 8) --> "64438756"
("664438769", 8) --> "67834466"
("123456779", 8) --> "23456771"
("", 8) --> ""
("123456779", 0) --> "" 
("563000655734469485", 4) --> "0365065073456944"
Example of a string rotated to the left by one position:
s = "123456" gives "234561".
AlgorithmsStrings
*/
// Solution
package kata

import "strings"

func Revrot(s string, n int) string {
	if n <= 0 || n > len(s) || len(s) == 0 {
		return ""
	}
	var sb strings.Builder
	for i := 0; i+n <= len(s); i += n { 
		chunk := s[i : i+n]

		sum := 0
		for _, ch := range chunk {
			d := int(ch - '0')
			sum += d * d * d
		}

		if sum%2 == 0 {
			for j := n - 1; j >= 0; j-- {
				sb.WriteByte(chunk[j])
			}
		} else {
			sb.WriteString(chunk[1:])
			sb.WriteByte(chunk[0])
		}
	}
	return sb.String()
}