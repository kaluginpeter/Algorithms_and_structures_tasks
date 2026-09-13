/*
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples
HighAndLow("1 2 3 4 5") // return "5 1"
HighAndLow("1 2 -3 4 5") // return "5 -3"
HighAndLow("1 9 3 4 -5") // return "9 -5"
Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
FundamentalsStrings
*/
// Solution
package kata

import "strconv"

func HighAndLow(in string) string {
  var mn, mx, acc int = 1e5, -1e5, 0
  var isNeg bool = false;
  for _, ch := range in {
    if ch == ' ' {
      if isNeg {
        acc *= -1
      }
      mn = min(mn, acc)
      mx = max(mx, acc)
      acc = 0
      isNeg = false
    } else if ch == '-' {
      isNeg = true
    } else {
      acc = acc * 10 + int(ch - '0')
    }
  }
  if isNeg {
    acc *= -1
  }
  mn = min(mn, acc)
  mx = max(mx, acc)
  return strconv.Itoa(mx) + " " + strconv.Itoa(mn)
}