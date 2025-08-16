# You are given a positive integer num consisting only of digits 6 and 9.
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
#
# Example 1:
#
# Input: num = 9669
# Output: 9969
# Explanation:
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.
# Example 2:
#
# Input: num = 9996
# Output: 9999
# Explanation: Changing the last digit 6 to 9 results in the maximum number.
# Example 3:
#
# Input: num = 9999
# Output: 9999
# Explanation: It is better not to apply any change.
#
# Constraints:
# 1 <= num <= 104
# num consists of only 6 and 9 digits.
# Solution
class Solution:
    def maximum69Number (self, num: int) -> int:
        l = []
        l.append(num)
        for k,v in enumerate(str(num)):
            if str(num)[k] == '9': l.append(int(str(num)[:k] + '6' + str(num)[k+1:]))
            else : l.append(int(str(num)[:k] + '9' + str(num)[k+1:]))
        return max(l)

# Python O(log(N)) O(1) Math Greedy
class Solution:
    def maximum69Number (self, num: int) -> int:
        rev_num: int = 0
        place: int = 0
        target: int = 0
        while num:
            rev_num = rev_num * 10 + num % 10
            if num % 10 == 6: target = place
            num //= 10
            place += 1
        target = place - target
        output: int = 0
        while rev_num:
            target -= 1
            if not target: output = output * 10 + 9
            else: output = output * 10 + rev_num % 10
            rev_num //= 10
        return output

# C++ O(log(N)) O(1) Math Greedy
class Solution {
public:
    int maximum69Number (int num) {
        int revNum = 0, place = 0, target = 0;
        while (num) {
            revNum = revNum * 10 + num % 10;
            if (num % 10 == 6) target = place;
            num /= 10;
            ++place;
        }
        target = place - target;
        int output = 0;
        while (revNum) {
            --target;
            if (!target) output = output * 10 + 9;
            else output = output * 10 + revNum % 10;
            revNum /= 10;
        }
        return output;
    }
};