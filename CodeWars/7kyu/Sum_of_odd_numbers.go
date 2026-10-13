/*
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8
ArraysListsMathematicsFundamentals
*/
// Solution
package kata

func RowSumOddNumbers(n int) int {
    var output int = 0
    for i := n * n - (n - 1); i < (n * n - (n - 1)) + n * 2; i += 2 { output += i }
    return output
}