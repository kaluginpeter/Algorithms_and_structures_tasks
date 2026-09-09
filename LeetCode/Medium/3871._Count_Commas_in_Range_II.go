/*
You are given an integer n.

Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.

In standard formatting:

A comma is inserted after every three digits from the right.
Numbers with fewer than 4 digits contain no commas.
 

Example 1:

Input: n = 1002

Output: 3

Explanation:

The numbers "1,000", "1,001", and "1,002" each contain one comma, giving a total of 3.

Example 2:

Input: n = 998

Output: 0

Explanation:

​​​​​​​All numbers from 1 to 998 have fewer than four digits. Therefore, no commas are used.

 

Constraints:

1 <= n <= 1015
*/
// Solution
// Go O(log10(N)) O(1) Math
func countCommas(n int64) int64 {
    var total, cur, step, commas int64 = 0, 1000, 0, 1
    for cur <= n {
        var nextCur int64 = min(cur * 10 - 1, n)
        total += (nextCur - cur + 1) * commas
        step++
        if (step % 3 == 0) {
            commas++
        }
        cur = nextCur + 1
    }
    return total
}

// C++ O(log10(N)) O(1) Math
class Solution {
public:
    long long countCommas(long long n) {
        long long output = 0, cur = 1000, step = 0, commas = 1;
        while (cur <= n) {
            long long nextCur = std::min(cur * 10 - 1, n);
            output += (nextCur - cur + 1) * commas;
            if (++step % 3 == 0) ++commas;
            cur = nextCur + 1;
        }
        return output;
    }
};

// Python O(log10(N)) O(1) Math
class Solution:
    def countCommas(self, n: int) -> int:
        output: int = 0
        cur: int = 1_000
        commas: int = 1
        step: int = 0
        while cur <= n:
            next_cur: int = min(cur * 10 - 1, n)
            output += (next_cur - cur + 1) * commas
            step += 1
            if step % 3 == 0: commas += 1
            cur = next_cur + 1
        return output