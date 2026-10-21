/*
You are given a string s consisting of lowercase English letters.

In one operation, you can select any substring of s that is not the entire string and sort it in non-descending alphabetical order.

Return the minimum number of operations required to make s sorted in non-descending order. If it is not possible, return -1.

 

Example 1:

Input: s = "dog"

Output: 1

Explanation:​​​​​​​

Sort substring "og" to "go".
Now, s = "dgo", which is sorted in ascending order. Thus, the answer is 1.
Example 2:

Input: s = "card"

Output: 2

Explanation:

Sort substring "car" to "acr", so s = "acrd".
Sort substring "rd" to "dr", making s = "acdr", which is sorted in ascending order. Thus, the answer is 2.
Example 3:

Input: s = "gf"

Output: -1

Explanation:

It is impossible to sort s under the given constraints. Thus, the answer is -1.
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
 


*/
// Solution
// Go O(NlogN) O(N) Sorting Greedy
import "slices"
func minOperations(s string) int {
    var tmp, targetByte []byte = []byte(s), []byte(s)
    slices.Sort(targetByte)
    var target string = string(targetByte)
    if s == target { return 0 } // already sorted
    var n int = len(s)
    if n == 2 {
        if s[0] > s[1] { return -1 }
        return 0
    }
    var first, second []byte = make([]byte, n - 1), make([]byte, n - 1)
    copy(first, tmp[1:])
    copy(second, tmp[:n - 1])
    slices.Sort(first)
    slices.Sort(second)
    first = slices.Insert(first, 0, tmp[0])
    second = append(second, tmp[n - 1])
    if string(first) == target || string(second) == target { return 1 }

    var firstBefore, secondBefore byte = first[n - 1], second[0]
    first = first[:n - 1]
    second = second[1:]
    slices.Sort(first)
    slices.Sort(second)
    first = append(first, firstBefore)
    second = slices.Insert(second, 0, secondBefore)
    if string(first) == target || string(second) == target { return 2 }

    return 3

}
// we can just brute force all possible scenarios
// for 1 operation: (0, n] || [0, n)
// for 2 operations: (0, n] + [0, n) || [0, n) + (0, n]
// for 3 operations: (0, n] + [0, n) + (0, n] || [0, n) + (0, n] + [0, n)
// Complexity O(KNlogN) where the K is 5 -> O(5NlogN)
// Space complexity O(N)