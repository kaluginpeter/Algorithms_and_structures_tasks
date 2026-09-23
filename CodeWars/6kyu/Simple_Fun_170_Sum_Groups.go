/*
Task
Given an array of integers, sum consecutive even numbers and consecutive odd numbers. Repeat the process while it can be done and return the length of the final array.

Example
For arr = [2, 1, 2, 2, 6, 5, 0, 2, 0, 5, 5, 7, 7, 4, 3, 3, 9]

The result should be 6.

[2, 1, 2, 2, 6, 5, 0, 2, 0, 5, 5, 7, 7, 4, 3, 3, 9]  -->
         2+2+6       0+2+0     5+5+7+7       3+3+9
[2, 1,   10,    5,    2,        24,     4,   15   ] -->
                               2+24+4
[2, 1,   10,    5,             30,           15   ]
The length of final array is 6
Input/Output
[input] integer array arr

A non-empty array,

1 ≤ arr.length ≤ 1000

0 ≤ arr[i] ≤ 1000

[output] an integer

The length of the final array

ArraysAlgorithmsListsData Structures
*/
// Solution
package kata

func SumGroups(arr []int) int {
  var flag bool = true
  for flag == true {
    flag = false
    var tmp []int = []int{}
    var left, acc int = 0, 0
    for right := 0; right < len(arr); right++ {
      if arr[left] % 2 != arr[right] % 2 {
        if len(tmp) > 0 && tmp[len(tmp) - 1] % 2 == acc % 2 {
          flag = true
        }
        tmp = append(tmp, acc)
        acc = arr[right]
        left = right
      } else { acc += arr[right] }
    }
    if len(tmp) > 0 && tmp[len(tmp) - 1] % 2 == acc % 2 {
      flag = true
    }
    tmp = append(tmp, acc)
    arr = make([]int, len(tmp))
    copy(arr, tmp)
  }
  return len(arr)
}