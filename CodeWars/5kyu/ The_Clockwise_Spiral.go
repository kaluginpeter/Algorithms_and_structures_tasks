/*
Do you know how to make a spiral? Let's test it!
Classic definition: A spiral is a curve which emanates from a central point, getting progressively farther away as it revolves around the point.

Your objective is to complete a function createSpiral(N) that receives an integer N and returns an NxN two-dimensional array with numbers 1 through NxN represented as a clockwise spiral.

Return an empty array if N < 1 or N is not int / number

Examples:

N = 3 Output: [[1,2,3],[8,9,4],[7,6,5]]

1    2    3
8    9    4
7    6    5
N = 4 Output: [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]

1   2   3   4
12  13  14  5
11  16  15  6
10  9   8   7
N = 5 Output: [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]]

1   2   3   4   5
16  17  18  19  6
15  24  25  20  7
14  23  22  21  8
13  12  11  10  9
ArraysPuzzles
*/
// Solution
package kata

func CreateSpiral(n int) [][]int {
	if n < 1 {
		return [][]int{}
	}

	result := make([][]int, n)
	for i := range result {
		result[i] = make([]int, n)
	}

	top, bottom := 0, n-1
	left, right := 0, n-1
	num := 1

	for top <= bottom && left <= right {
		for col := left; col <= right; col++ {
			result[top][col] = num
			num++
		}
		top++
		for row := top; row <= bottom; row++ {
			result[row][right] = num
			num++
		}
		right--
		if top <= bottom {
			for col := right; col >= left; col-- {
				result[bottom][col] = num
				num++
			}
			bottom--
		}
		if left <= right {
			for row := bottom; row >= top; row-- {
				result[row][left] = num
				num++
			}
			left++
		}
	}

	return result
}