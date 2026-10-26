/*
You are given an m x n matrix grid and a positive integer k. An island is a group of positive integers (representing land) that are 4-directionally connected (horizontally or vertically).

The total value of an island is the sum of the values of all cells in the island.

Return the number of islands with a total value divisible by k.

 

Example 1:


Input: grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5

Output: 2

Explanation:

The grid contains four islands. The islands highlighted in blue have a total value that is divisible by 5, while the islands highlighted in red do not.

Example 2:


Input: grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3

Output: 6

Explanation:

The grid contains six islands, each with a total value that is divisible by 3.

 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
0 <= grid[i][j] <= 106
1 <= k <= 106
*/
// Solution
// Go O(NM) O(NM) DFS Matrix
func dfs(grid *[][]int, start, n, m, k int, output *int) {
    var moves [][]int = [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
    var value int = (*grid)[start / m][start % m]
    (*grid)[start / m][start % m] = 0
    var data []int = []int{start}
    for len(data) > 0 {
        var cell int = data[len(data) - 1]
        data = data[:len(data) - 1]
        var i, j int = cell / m, cell % m
        for _, move := range moves {
            var ni, nj int = i + move[0], j + move[1]
            if ni < 0 || ni == n || nj < 0 || nj == m { continue }
            if (*grid)[ni][nj] == 0 { continue }
            value += (*grid)[ni][nj]
            (*grid)[ni][nj] = 0
            data = append(data, ni * m + nj)
        }
    }
    if value % k == 0 { (*output)++ }
}

func countIslands(grid [][]int, k int) int {
    var n, m, output int = len(grid), len(grid[0]), 0
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            if grid[i][j] > 0 { dfs(&grid, i * m + j, n, m, k, &output) }
        }
    }
    return output
}