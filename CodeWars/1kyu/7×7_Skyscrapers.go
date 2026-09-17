/*
In a grid of 7 by 7 squares you want to place a skyscraper in each square with only some clues:

The height of the skyscrapers is between 1 and 7
No two skyscrapers in a row or column may have the same number of floors
A clue is the number of skyscrapers that you can see in a row or column from the outside
Higher skyscrapers block the view of lower skyscrapers located behind them
Can you write a program that can solve this puzzle in time?

This kata is based on 4 By 4 Skyscrapers and 6 By 6 Skyscrapers by FrankK. By now, examples should be superfluous; you should really solve Frank's kata first, and then probably optimise some more. A naive solution that solved a 4×4 puzzle within 12 seconds might need time somewhere beyond the Heat Death of the Universe for this size. It's quite bad.

Task
Create

func SolvePuzzle(clues []int) [][]int {}
Clues are passed in as a slice of integers []int. The return value is a slice of slice of integers [][]int.

All puzzles have one possible solution.
All this is the same as with the earlier kata.

Caveat: The tests for this kata have been tailored to run in ~10 seconds with the JavaScript reference solution. You'll need to do better than that! Please note the performance tag.

Conceptis Puzzles have heaps of these puzzles, from 4×4 up to 7×7 and unsolvable within CodeWars time constraints. Old puzzles from there were used for the tests. They also have lots of other logic, numbers and mathematical puzzles, and their puzzle user interface is generally nice, very nice.

AlgorithmsGamesPerformance
*/
// Solution
package kata

const gridSize = 7
const dirCount = 4
const allBits = (1 << gridSize) - 1

var lineStart = [dirCount * gridSize]int{
	0, 1, 2, 3, 4, 5, 6,
	6, 13, 20, 27, 34, 41, 48,
	48, 47, 46, 45, 44, 43, 42,
	42, 35, 28, 21, 14, 7, 0,
}

var lineStep = [dirCount * gridSize]int{
	7, 7, 7, 7, 7, 7, 7,
	-1, -1, -1, -1, -1, -1, -1,
	-7, -7, -7, -7, -7, -7, -7,
	1, 1, 1, 1, 1, 1, 1,
}

var cellMask [gridSize * gridSize]int
var finalGrid [gridSize][gridSize]int
var locked [gridSize * gridSize]bool
var cluesData []int

func assignCell(index, value int) {
	forbid := allBits ^ (1 << value)
	rowBase := index - index%gridSize
	colBase := index % gridSize
	for i := 0; i < gridSize; i++ {
		cellMask[rowBase+i] &= forbid
		cellMask[colBase+i*gridSize] &= forbid
	}
	cellMask[index] = 1 << value
}

func propagateUnique() int {
	changes := 0
	for i := 0; i < dirCount/2*gridSize; i++ {
		var valueCells [gridSize][]int
		p := lineStart[i]
		for k := 0; k < gridSize; k++ {
			for v := 0; v < gridSize; v++ {
				if cellMask[p]&(1<<v) != 0 {
					valueCells[v] = append(valueCells[v], p)
				}
			}
			p += lineStep[i]
		}
		for v := 0; v < gridSize; v++ {
			if len(valueCells[v]) == 1 {
				pos := valueCells[v][0]
				if cellMask[pos] != (1 << v) {
					assignCell(pos, v)
					changes++
				}
			}
		}
	}
	return changes
}

func pruneTwoClue() int {
	cnt := 0
	for i := 0; i < dirCount*gridSize; i++ {
		if cluesData[i] != 2 {
			continue
		}
		allowed := allBits
		for v := gridSize - 1; v >= 0; v-- {
			allowed ^= 1 << v
			if cellMask[lineStart[i]]&(1<<v) != 0 {
				break
			}
		}
		p := lineStart[i] + lineStep[i]
		for k := 1; k < gridSize; k++ {
			if cellMask[p]&(1<<(gridSize-1)) != 0 {
				break
			}
			if (cellMask[p] | allowed) != allowed {
				cellMask[p] &= allowed
				cnt++
			}
			p += lineStep[i]
		}
	}
	return cnt
}

func countBits(x int) int {
	c := 0
	for x != 0 {
		c += x & 1
		x >>= 1
	}
	return c
}

func checkConsistency() bool {
	for i := 0; i < dirCount*gridSize; i++ {
		if cluesData[i] == 0 {
			continue
		}
		complete := true
		p := lineStart[i]
		for k := 0; k < gridSize; k++ {
			if countBits(cellMask[p]) != 1 {
				complete = false
				break
			}
			p += lineStep[i]
		}
		if complete {
			tallest, visible := 0, 0
			p := lineStart[i]
			for k := 0; k < gridSize; k++ {
				if cellMask[p] > tallest {
					tallest = cellMask[p]
					visible++
				}
				p += lineStep[i]
			}
			if visible != cluesData[i] {
				return false
			}
		}
	}
	return true
}

func extractSolution() {
	for i := 0; i < gridSize*gridSize; i++ {
		r, c := i/gridSize, i%gridSize
		for v := 0; v < gridSize; v++ {
			if cellMask[i] == (1 << v) {
				finalGrid[r][c] = v + 1
			}
		}
	}
}

func search(depth int) bool {
	chosen, best := -1, 10000
	for i := 0; i < gridSize*gridSize; i++ {
		options := countBits(cellMask[i])
		if options < best && !locked[i] {
			best = options
			chosen = i
		}
	}
	if chosen == -1 {
		if checkConsistency() {
			extractSolution()
			return true
		}
		return false
	}
	backup := cellMask
	for v := gridSize - 1; v >= 0; v-- {
		if cellMask[chosen]&(1<<v) == 0 {
			continue
		}
		locked[chosen] = true
		assignCell(chosen, v)
		if checkConsistency() && search(depth+1) {
			return true
		}
		locked[chosen] = false
		cellMask = backup
	}
	return false
}

func resetState() {
	for i := 0; i < gridSize*gridSize; i++ {
		cellMask[i] = allBits
		locked[i] = true
	}
}

func preprocess() {
	for i := 0; i < dirCount*gridSize; i++ {
		if cluesData[i] == 0 {
			continue
		}
		p := lineStart[i]
		for k := 0; k < gridSize; k++ {
			mask := allBits
			for v := gridSize + k - cluesData[i] + 1; v < gridSize; v++ {
				mask ^= 1 << v
			}
			cellMask[p] &= mask
			p += lineStep[i]
		}
	}
	for propagateUnique() > 0 {
	}
	pruneTwoClue()
}

func SolvePuzzle(clues []int) [][]int {
	resetState()
	cluesData = clues
	preprocess()
	for i := 0; i < gridSize*gridSize; i++ {
		if countBits(cellMask[i]) > 1 {
			locked[i] = false
		}
	}
	search(0)

	result := make([][]int, gridSize)
	for i := 0; i < gridSize; i++ {
		row := make([]int, gridSize)
		for j := 0; j < gridSize; j++ {
			row[j] = finalGrid[i][j]
		}
		result[i] = row
	}
	return result
}