/*
An array consisting of 0s and 1s, also called a binary array, is given as an input.

Task
Find the length of the longest contiguous subarray which consists of equal number of 0s and 1s.

Example
s = [1,1,0,1,1,0,1,1]
         |_____|
            |
         [0,1,1,0]

         length = 4
Note
0 <= length(array) < 120 000
AlgorithmsDynamic ProgrammingArrays
*/
// Solution
package kata

func Binarray(a []int) int {
	n := len(a)
	first := make([]int, 2*n+1)
	for i := range first {
		first[i] = -1
	}
	first[n] = 0

	sum, best := n, 0
	for i, v := range a {
		if v == 1 {
			sum++
		} else {
			sum--
		}
		if first[sum] == -1 {
			first[sum] = i + 1
		} else if i+1-first[sum] > best {
			best = i + 1 - first[sum]
		}
	}
	return best
}