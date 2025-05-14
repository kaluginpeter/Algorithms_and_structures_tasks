# You are given a string s consisting of lowercase English letters, an integer t representing the number of transformations to perform, and an array nums of size 26. In one transformation, every character in s is replaced according to the following rules:
#
# Replace s[i] with the next nums[s[i] - 'a'] consecutive characters in the alphabet. For example, if s[i] = 'a' and nums[0] = 3, the character 'a' transforms into the next 3 consecutive characters ahead of it, which results in "bcd".
# The transformation wraps around the alphabet if it exceeds 'z'. For example, if s[i] = 'y' and nums[24] = 3, the character 'y' transforms into the next 3 consecutive characters ahead of it, which results in "zab".
# Return the length of the resulting string after exactly t transformations.
#
# Since the answer may be very large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
#
# Output: 7
#
# Explanation:
#
# First Transformation (t = 1):
#
# 'a' becomes 'b' as nums[0] == 1
# 'b' becomes 'c' as nums[1] == 1
# 'c' becomes 'd' as nums[2] == 1
# 'y' becomes 'z' as nums[24] == 1
# 'y' becomes 'z' as nums[24] == 1
# String after the first transformation: "bcdzz"
# Second Transformation (t = 2):
#
# 'b' becomes 'c' as nums[1] == 1
# 'c' becomes 'd' as nums[2] == 1
# 'd' becomes 'e' as nums[3] == 1
# 'z' becomes 'ab' as nums[25] == 2
# 'z' becomes 'ab' as nums[25] == 2
# String after the second transformation: "cdeabab"
# Final Length of the string: The string is "cdeabab", which has 7 characters.
#
# Example 2:
#
# Input: s = "azbk", t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
#
# Output: 8
#
# Explanation:
#
# First Transformation (t = 1):
#
# 'a' becomes 'bc' as nums[0] == 2
# 'z' becomes 'ab' as nums[25] == 2
# 'b' becomes 'cd' as nums[1] == 2
# 'k' becomes 'lm' as nums[10] == 2
# String after the first transformation: "bcabcdlm"
# Final Length of the string: The string is "bcabcdlm", which has 8 characters.
#
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists only of lowercase English letters.
# 1 <= t <= 109
# nums.length == 26
# 1 <= nums[i] <= 25
# Solution
# Python O(N * log(T) * 26^3) O(26^2) DynamicProgramming Matrix Math
MOD = 10**9 + 7
class Matrix:
    def __init__(self, other: 'Matrix' = None) -> None:
        self.a: list[list[int]] = [[0] * 26 for _ in range(26)]
        if not other: return
        for i in range(L):
            for j in range(L):
                self.a[i][j] = other.a[i][j]

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        output: Matrix = Matrix()
        for i in range(26):
            for j in range(26):
                for k in range(26):
                    output.a[i][j] = (output.a[i][j] + self.a[i][k] * other.a[k][j]) % MOD
        return output

    @staticmethod
    def create() -> 'Matrix':
        output: 'Matrix' = Matrix()
        for i in range(26): output.a[i][i] = 1
        return output

    @staticmethod
    def multiplication(x: 'Matrix', y: int) -> 'Matrix':
        output: Matrix = Matrix.create()
        cur: Matrix = x
        while y:
            if y & 1: output = output * cur
            cur = cur * cur
            y >>= 1
        return output

class Solution:
    def lengthAfterTransformations(
        self, s: str, t: int, nums: List[int]
    ) -> int:
        T: Matrix = Matrix()
        for i in range(26):
            for step in range(1, nums[i] + 1):
                T.a[(i + step) % 26][i] = 1

        output: Matrix = Matrix.multiplication(T, t)
        hashmap: list[int] = [0] * 26
        for letter in s: hashmap[ord(letter) - 97] += 1
        total = 0
        for i in range(26):
            for j in range(26):
                total = (total + output.a[i][j] * hashmap[j]) % MOD
        return total

# C++ O(N * log(T) * 26^3) O(26^2) DynamicProgramming Math Matrix
static constexpr int L = 26;
static constexpr int MOD = 1000000007;

struct Mat {
    int a[L][L];
    Mat() { memset(a, 0, sizeof(a)); }
    Mat(const Mat &that) {
        for (int i = 0; i < L; ++i) {
            for (int j = 0; j < L; ++j) a[i][j] = that.a[i][j];
        }
    }
    Mat& operator=(const Mat &that) {
        if (this != &that) {
            for (int i = 0; i < L; ++i) {
                for (int j = 0; j < L; ++j) a[i][j] = that.a[i][j];
            }
        }
        return *this;
    }
};

Mat operator*(const Mat &u, const Mat &v) {
    Mat w;
    for (int i = 0; i < L; ++i) {
        for (int j = 0; j < L; ++j) {
            for (int k = 0; k < L; ++k) {
                w.a[i][j] = (w.a[i][j] + static_cast<long long>(u.a[i][k]) * v.a[k][j]) % MOD;
            }
        }
    }
    return w;
}

Mat init() {
    Mat w;
    for (int i = 0; i < L; ++i) w.a[i][i] = 1;
    return w;
}

Mat multiplication(const Mat &x, int y) {
    Mat output = init(), cur = x;
    while (y) {
        if (y & 1) output = output * cur;
        cur = cur * cur;
        y >>= 1;
    }
    return output;
}

class Solution {
public:
    int lengthAfterTransformations(string s, int t, vector<int>& nums) {
        Mat T;
        for (int i = 0; i < 26; ++i) {
            for (int step = 1; step <= nums[i]; ++step) T.a[(i + step) % 26][i] = 1;
        }
        Mat res = multiplication(T, t);
        int output = 0;
        vector<int> hashmap(26, 0);
        for (char &letter : s) ++hashmap[letter - 'a'];
        for (int i = 0; i < 26; ++i) {
            for (int j = 0; j < 26; ++j) {
                output = (output + static_cast<long long>(res.a[i][j]) * hashmap[j]) % MOD;
            }
        }
        return output;
    }
};