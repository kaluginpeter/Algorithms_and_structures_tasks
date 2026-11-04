/*
Consider a sequence u where u is defined as follows:

The number u(0) = 1 is the first one in u.
For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
There are no other numbers in u.
Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

Task:
Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).

Example:
dbl_linear(10) should return 22

Note:
Focus attention on efficiency

MathematicsAlgorithms
*/
// Solution
package kata

import "container/heap"

type MinHeap []int

func (h MinHeap) Len() int            { return len(h) }
func (h MinHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func DblLinear(n int) int {
	uSet := map[int]bool{1: true}
	uHeap := &MinHeap{1}
	for i := 0; i < n; i++ {
		sm := heap.Pop(uHeap).(int)
		y := 2*sm + 1
		z := 3*sm + 1
		if !uSet[y] {
			uSet[y] = true
			heap.Push(uHeap, y)
		}
		if !uSet[z] {
			uSet[z] = true
			heap.Push(uHeap, z)
		}
	}
	return (*uHeap)[0]
}