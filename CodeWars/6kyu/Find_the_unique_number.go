/*
There is an array with some numbers. All numbers are equal except for one. Try to find it!

findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

Find the unique number (this kata)
Find the unique string
Find The Unique
FundamentalsAlgorithmsArraysPerformance
*/
// Solution 
package kata

func FindUniq(arr []float32) float32 {
  if arr[0] != arr[1] {
    if arr[1] == arr[2] { return arr[0] }
    return arr[1]
  }
  for i := 2; i < len(arr); i++ {
    if arr[i] != arr[0] { return arr[i] }
  }
  return -1
}