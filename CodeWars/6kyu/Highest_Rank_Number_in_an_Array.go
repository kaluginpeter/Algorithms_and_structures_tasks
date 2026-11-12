/*
Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.

Examples
[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3
ArraysFundamentals
*/
// Solution
package kata

func HighestRank(nums []int) int {
  var seen map[int]int = map[int]int{}
  var mx int = 0
  for _, num := range nums {
    seen[num]++
    if seen[num] > seen[mx] {
      mx = num
    } else if seen[num] == seen[mx] && num > mx {
      mx = num
    }
  }
  return mx
}