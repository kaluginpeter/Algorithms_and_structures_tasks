/*
You are given an array of digits called digits. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.

Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.

 

Example 1:

Input: digits = [1,2,3,4]

Output: 12

Explanation: The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 cannot be formed because there is only 1 copy of the digit 2.

Example 2:

Input: digits = [0,2,2]

Output: 2

Explanation: The only 3-digit even numbers that can be formed are 202 and 220. Note that the digit 2 can be used twice because it appears twice in the array.

Example 3:

Input: digits = [6,6,6]

Output: 1

Explanation: Only 666 can be formed.

Example 4:

Input: digits = [1,3,5]

Output: 0

Explanation: No even 3-digit numbers can be formed.

 

Constraints:

3 <= digits.length <= 10
0 <= digits[i] <= 9
*/
// Solution
// Go O(N + D^2) O(D) HashMap Math
func totalNumbers(digits []int) int {
	var freq [10]int = [10]int{}
	for _, d := range digits { freq[d]++ }
	var overall int = 0
	for d := 0; d <= 8; d += 2 {
		if freq[d] == 0 { continue }
		freq[d]--
		var distinct, duplicates int = 0, 0
		for digit := 0; digit < 10; digit++ {
			if freq[digit] > 0 {
				distinct++
				if freq[digit] >= 2 { duplicates++ }
			}
		}
		overall += distinct * (distinct - 1) + duplicates
		if freq[0] > 0 {
			var invalid int = distinct - 1
			if freq[0] >= 2 { invalid++ }
			overall -= invalid
		}
		freq[d]++
	}
	return overall
}