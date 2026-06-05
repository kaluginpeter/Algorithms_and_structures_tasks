# You are given two integers num1 and num2 representing an inclusive range [num1, num2].
#
# The waviness of a number is defined as the total count of its peaks and valleys:
#
# A digit is a peak if it is strictly greater than both of its immediate neighbors.
# A digit is a valley if it is strictly less than both of its immediate neighbors.
# The first and last digits of a number cannot be peaks or valleys.
# Any number with fewer than 3 digits has a waviness of 0.
# Return the total sum of waviness for all numbers in the range [num1, num2].
#
#
# Example 1:
#
# Input: num1 = 120, num2 = 130
#
# Output: 3
#
# Explanation:
#
# In the range [120, 130]:
#
# 120: middle digit 2 is a peak, waviness = 1.
# 121: middle digit 2 is a peak, waviness = 1.
# 130: middle digit 3 is a peak, waviness = 1.
# All other numbers in the range have a waviness of 0.
# Thus, total waviness is 1 + 1 + 1 = 3.
#
# Example 2:
#
# Input: num1 = 198, num2 = 202
#
# Output: 3
#
# Explanation:
#
# In the range [198, 202]:
#
# 198: middle digit 9 is a peak, waviness = 1.
# 201: middle digit 0 is a valley, waviness = 1.
# 202: middle digit 0 is a valley, waviness = 1.
# All other numbers in the range have a waviness of 0.
# Thus, total waviness is 1 + 1 + 1 = 3.
#
# Example 3:
#
# Input: num1 = 4848, num2 = 4848
#
# Output: 2
#
# Explanation:
#
# Number 4848: the second digit 8 is a peak, and the third digit 4 is a valley, giving a waviness of 2.
#
#
#
# Constraints:
#
# 1 <= num1 <= num2 <= 1015​​​​​​​
# Solution
# C++ O(D^3logN) O(D^2) DynamicProgramming Digit-DP
struct State {
    int prev, curr, tight, lead;
    long long cnt, sum;
};

class Solution {
public:
    long long solve(long long num) {
        if (num < 100) return 0;
        std::string s = std::to_string(num);
        int n = s.size();
        std::vector<State> currStates;
        currStates.push_back({10, 10, 1, 1, 1, 0});
        for (int pos = 0; pos < n; ++pos) {
            int limit = s[pos] - '0';
            long long cnt[2][2][11][11] = {0};
            long long sum[2][2][11][11] = {0};

            for (const auto& st : currStates) {
                int maxDigit = st.tight ? limit : 9;
                for (int digit = 0; digit <= maxDigit; ++digit) {
                    int newLead = st.lead && (digit == 0);
                    int newPrev = st.curr;
                    int newCurr = newLead ? 10 : digit;
                    int newTight = st.tight && (digit == maxDigit);

                    long long add = 0;
                    if (!newLead && st.prev != 10 && st.curr != 10) {
                        if ((st.prev < st.curr && st.curr > digit) ||
                            (st.prev > st.curr && st.curr < digit)) {
                            add = st.cnt;
                        }
                    }

                    cnt[newTight][newLead][newPrev][newCurr] += st.cnt;
                    sum[newTight][newLead][newPrev][newCurr] += st.sum + add;
                }
            }
            vector<State> nextStates;
            for (int tight = 0; tight < 2; ++tight) {
                for (int lead = 0; lead < 2; ++lead) {
                    for (int prev = 0; prev <= 10; ++prev) {
                        for (int curr = 0; curr <= 10; ++curr) {
                            long long c = cnt[tight][lead][prev][curr];
                            long long s = sum[tight][lead][prev][curr];
                            if (c) nextStates.push_back({prev, curr, tight, lead, c, s});
                        }
                    }
                }
            }
            currStates.swap(nextStates);
        }
        long long ans = 0;
        for (const auto& st : currStates) ans += st.sum;
        return ans;
    }

    long long totalWaviness(long long num1, long long num2) {
        return solve(num2) - solve(num1 - 1);
    }
};