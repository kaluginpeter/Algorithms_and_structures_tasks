/*
You are given a string num which represents a positive integer, and an integer t.

A number is called zero-free if none of its digits are 0.

Return a string representing the smallest zero-free number greater than or equal to num such that the product of its digits is divisible by t. If no such number exists, return "-1".



Example 1:

Input: num = "1234", t = 256

Output: "1488"

Explanation:

The smallest zero-free number that is greater than 1234 and has the product of its digits divisible by 256 is 1488, with the product of its digits equal to 256.

Example 2:

Input: num = "12355", t = 50

Output: "12355"

Explanation:

12355 is already zero-free and has the product of its digits divisible by 50, with the product of its digits equal to 150.

Example 3:

Input: num = "11111", t = 26

Output: "-1"

Explanation:

No number greater than 11111 has the product of its digits divisible by 26.



Constraints:

2 <= num.length <= 2 * 105
num consists only of digits in the range ['0', '9'].
num does not contain leading zeros.
1 <= t <= 1014
*/
// Solution
// C++ O(N + DlogN) O(N) Prefix Math
class Solution {
public:
    string smallestNumber(string num, long long t) {
        long long temp = t;
        for (int i = 2; i <= 9; ++i) {
            while (temp % i == 0) temp /= i;
        }
        if (temp > 1) return "-1"; // the "t" is the prime number itself
        int n = num.length();
        std::vector<long long> rem(n + 1);
        rem[0] = t;
        int start = n - 1;
        for (int i = 0; i < n; ++i) {
            if (num[i] == '0') {
                start = i;
                break;
            }
            rem[i + 1] = rem[i] / std::gcd(rem[i], num[i] - '0');
        }
        if (rem[n] == 1) return num;
        for (int i = start; i >= 0; --i) {
            for (char d = num[i] + 1; d <= '9'; ++d) {
                num[i] = d;
                long long tmpT = rem[i] / std::gcd(rem[i], d - '0');
                int k = 9;
                for (int j = n - 1; j > i; --j) {
                    while (tmpT % k) --k;
                    tmpT /= k;
                    num[j] = k + '0';
                }
                if (tmpT == 1) return num;
            }
        }
        std::string output = "";
        for (int i = 9; i > 1; --i) {
            while (t % i == 0) {
                output += i + '0';
                t /= i;
            }
        }
        output += std::string(std::max(n - static_cast<int>(output.length()) + 1, 0), '1');
        std::reverse(output.begin(), output.end());
        return output;
    }
};