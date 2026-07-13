# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
#
# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
#
#
#
# Example 1:
#
# Input: low = 100, high = 300
# Output: [123,234]
# Example 2:
#
# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
#
#
# Constraints:
#
# 10 <= low <= high <= 10^9
# Solution O(K * 9) where K is high // 10 Memory O(N)
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits: str = '123456789'
        ans: list = []
        n1, n2 = len(str(low)), len(str(high))
        while n1 <= n2:
            for i in range(9 - (n1 - 1)):
                x: int = int(digits[i:i+n1])
                if x < low:
                    continue
                if x <= high:
                    ans.append(x)
                else:
                    break
            n1 += 1
        return ans


# Python O(log10(10^9)) O(log10(10^9)) Math
class Solution:
    def dfs(self, source: int, number: int, low: int, high: int, output: list[int]) -> None:
        if low <= number <= high: output.append(number)
        elif number > high: return
        if source < 9:
            self.dfs(source + 1, number * 10 + (source + 1), low, high, output)

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        output: list[int] = []
        for i in range(1, 10):
            self.dfs(i, i, low, high, output)
        output.sort()
        return output

# C++ O(log10(10^9)) O(log10(10^9)) Math
class Solution {
public:
    void dfs(int source, int number, const int& low, const int& high, std::vector<int>& output) {
        if (number >= low && number <= high) {
            output.push_back(number);
        } else if (number > high) return;
        if (source < 9) dfs(source + 1, number * 10 + (source + 1), low, high, output);
    }
    vector<int> sequentialDigits(int low, int high) {
        std::vector<int> output;
        for (int source = 1; source <= 9; ++source) dfs(source, source, low, high, output);
        std::sort(output.begin(), output.end());
        return output;
    }
};