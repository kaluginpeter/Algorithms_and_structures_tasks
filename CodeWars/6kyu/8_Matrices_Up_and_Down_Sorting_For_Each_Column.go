/*
You are given a matrix M, of positive and negative integers. It should be sorted in an up and down column way, starting always with the lowest element placed at the top left position finishing with the highest depending on n value: at the bottom right position if the number of columns,n, is odd, or placed at the top right, if n is even.

E.g.:

M = [[-20, -4, -1],
     [  1,  4,  7], 
     [  8, 10, 12]]
     
M_ = [[-20, 7, 8],
      [-4, 4, 10],
      [-1, 1, 12]]
In order to be more understandable we show the directions of the sorting for the new matrix with arrows:

source: imgur.com

Create the function up_down_col_sort() that receives a matrix as an argument and may do this kind of sorting.

Your function will be tested with square or rectangular matrices of m rows and n columns Features of the random tests:

Number of tests = 120
10 <= m <= 200
10 <= n <= 200
-1000 <= M[i,j] <= 1000
The kata is available at Python 2, Typescript, Javascript and Ruby at the moment. Translations into another languages will be released soon.

FundamentalsAlgorithmsData StructuresMathematicsMatrixSorting
*/
// Solution
package kata

import "slices"

func UpDownColSort(matrix [][]int) [][]int {
  var flat []int = []int{}
  for _, row := range matrix {
    for _, num := range row { flat = append(flat, num) }
  }
  slices.Sort(flat)
  var n, m int = len(matrix), len(matrix[0])
  var ptr int = 0
  for j := 0; j < m; j++ {
    for i := 0; i < n; i++ {
      if j % 2 == 0 {
        matrix[i][j] = flat[ptr]
      } else { matrix[n - i - 1][j] = flat[ptr] }
      ptr++
    }
  }
  return matrix
}