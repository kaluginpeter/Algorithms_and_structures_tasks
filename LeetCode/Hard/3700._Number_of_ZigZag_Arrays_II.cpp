/*
You are given three integers n, l, and r.

A ZigZag array of length n is defined as follows:

Each element lies in the range [l, r].
No two adjacent elements are equal.
No three consecutive elements form a strictly increasing or strictly decreasing sequence.
Return the total number of valid ZigZag arrays.

Since the answer may be large, return it modulo 109 + 7.

A sequence is said to be strictly increasing if each element is strictly greater than its previous one (if exists).

A sequence is said to be strictly decreasing if each element is strictly smaller than its previous one (if exists).



Example 1:

Input: n = 3, l = 4, r = 5

Output: 2

Explanation:

There are only 2 valid ZigZag arrays of length n = 3 using values in the range [4, 5]:

[4, 5, 4]
[5, 4, 5]
Example 2:

Input: n = 3, l = 1, r = 3

Output: 10

Explanation:

​​​​​​​There are 10 valid ZigZag arrays of length n = 3 using values in the range [1, 3]:

[1, 2, 1], [1, 3, 1], [1, 3, 2]
[2, 1, 2], [2, 1, 3], [2, 3, 1], [2, 3, 2]
[3, 1, 2], [3, 1, 3], [3, 2, 3]
All arrays meet the ZigZag conditions.



Constraints:

3 <= n <= 109
1 <= l < r <= 75​​​​​​​
*/
// C++ O(M^3logN) O(M^2) DynamicProgramming Math
class Solution {
private:
    static constexpr long long MOD = 1'000'000'007;
    using Matrix = vector<vector<long long>>;
    Matrix mul(const Matrix& a, const Matrix& b) {
        int n = a.size();
        int m = b[0].size();
        Matrix res(n, vector<long long>(m, 0));
        for (int i = 0; i < n; ++i) {
            for (int k = 0; k < a[0].size(); ++k) {
                long long r = a[i][k];
                if (!r) continue;
                for (int j = 0; j < m; ++j) res[i][j] = (res[i][j] + r * b[k][j]) % MOD;
            }
        }
        return res;
    }

    Matrix powMul(Matrix base, long long exp, Matrix res) {
        while (exp > 0) {
            if (exp & 1) res = mul(res, base);
            base = mul(base, base);
            exp >>= 1;
        }
        return res;
    }

public:
    int zigZagArrays(int n, int l, int r) {
        int m = r - l + 1;
        if (n == 1) return m;
        int size = 2 * m;
        Matrix u(size, vector<long long>(size, 0));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < i; ++j) u[i][j + m] = 1;
            for (int j = i + 1; j < m; ++j) u[i + m][j] = 1;
        }
        Matrix dp(1, vector<long long>(size, 1));
        dp = powMul(std::move(u), n - 1, std::move(dp));
        long long ans = 0;
        for (int i = 0; i < size; ++i) ans = (ans + dp[0][i]) % MOD;
        return ans;
    }
};class Solution {
private:
    static constexpr long long MOD = 1'000'000'007;
    using Matrix = vector<vector<long long>>;
    Matrix mul(const Matrix& a, const Matrix& b) {
        int n = a.size();
        int m = b[0].size();
        Matrix res(n, vector<long long>(m, 0));
        for (int i = 0; i < n; ++i) {
            for (int k = 0; k < a[0].size(); ++k) {
                long long r = a[i][k];
                if (!r) continue;
                for (int j = 0; j < m; ++j) res[i][j] = (res[i][j] + r * b[k][j]) % MOD;
            }
        }
        return res;
    }

    Matrix powMul(Matrix base, long long exp, Matrix res) {
        while (exp > 0) {
            if (exp & 1) res = mul(res, base);
            base = mul(base, base);
            exp >>= 1;
        }
        return res;
    }

public:
    int zigZagArrays(int n, int l, int r) {
        int m = r - l + 1;
        if (n == 1) return m;
        int size = 2 * m;
        Matrix u(size, vector<long long>(size, 0));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < i; ++j) u[i][j + m] = 1;
            for (int j = i + 1; j < m; ++j) u[i + m][j] = 1;
        }
        Matrix dp(1, vector<long long>(size, 1));
        dp = powMul(std::move(u), n - 1, std::move(dp));
        long long ans = 0;
        for (int i = 0; i < size; ++i) ans = (ans + dp[0][i]) % MOD;
        return ans;
    }
};

// Python O(M^3logN) O(M^2) Math DynamicProgramming
mod: int = 10**9 + 7
def matmul(A, B):
    d = len(A)
    C = [[0]*d for _ in range(d)]
    for i in range(d):
        for k in range(d):
            if A[i][k]:
                for j in range(d):
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
    return C

def mat_vector_mul(A, vec):
    d = len(A)
    res = [0]*d
    for i in range(d):
        s = 0
        for j in range(d):
            if A[i][j]:
                s += A[i][j] * vec[j]
        res[i] = s % mod
    return res

def matexp(A, power):
    d = len(A)
    res = [[1 if i == j else 0 for j in range(d)] for i in range(d)]
    base = A
    while power:
        if power & 1:
            res = matmul(res, base)
        base = matmul(base, base)
        power >>= 1
    return res

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        segment: int = r - l + 1
        dim: int = 2 * segment
        M: list[list[int]] = [[0] * dim for _ in range(dim)]
        for v in range(segment):
            for u in range(v):
                M[v][u + segment] = 1
            for u in range(v + 1, segment):
                M[v + segment][u] = 1
        dp: list[int] = [0] * dim
        for v in range(segment):
            dp[v] = v
            dp[v + segment] = segment - v - 1
        if n == 2: return sum(dp) % mod
        mat_exp: int = matexp(M, n - 2)
        return sum(mat_vector_mul(mat_exp, dp)) % mod