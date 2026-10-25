/*
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
*/
// Solution
// Go O(NM) O(NM) Dfs Matrix
func dfs(grid *[][]int, start int, output *int) {
    var n, m int = len(*grid), len((*grid)[0])
    var seen []int = []int{start}
    var moves [][]int = [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
    var isValid bool = true
    (*grid)[start / m][start % m] = 1
    for len(seen) > 0 {
        var cur int = seen[len(seen) - 1]
        seen = seen[:len(seen) - 1]
        var i, j int = cur / m, cur % m
        for _, move := range moves {
            var ni, nj int = i + move[0], j + move[1]
            if ni < 0 || ni == n || nj < 0 || nj == m {
                isValid = false 
                continue
            }
            if (*grid)[ni][nj] == 1 { continue }
            (*grid)[ni][nj] = 1
            seen = append(seen, ni * m + nj)
        }
    }
    if isValid { (*output)++ }
}

func closedIsland(grid [][]int) int {
    var output, n, m int = 0, len(grid), len(grid[0])
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            if grid[i][j] == 0 { dfs(&grid, i * m + j, &output) }
        }
    }
    return output
}
