# You are given three arrays of length n that describe the properties of n coupons: code, businessLine, and isActive. The ith coupon has:
#
# code[i]: a string representing the coupon identifier.
# businessLine[i]: a string denoting the business category of the coupon.
# isActive[i]: a boolean indicating whether the coupon is currently active.
# A coupon is considered valid if all of the following conditions hold:
#
# code[i] is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
# businessLine[i] is one of the following four categories: "electronics", "grocery", "pharmacy", "restaurant".
# isActive[i] is true.
# Return an array of the codes of all valid coupons, sorted first by their businessLine in the order: "electronics", "grocery", "pharmacy", "restaurant", and then by code in lexicographical (ascending) order within each category.
#
#
#
# Example 1:
#
# Input: code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [true,true,true,true]
#
# Output: ["PHARMA5","SAVE20"]
#
# Explanation:
#
# First coupon is valid.
# Second coupon has empty code (invalid).
# Third coupon is valid.
# Fourth coupon has special character @ (invalid).
# Example 2:
#
# Input: code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"], businessLine = ["grocery","electronics","invalid"], isActive = [false,true,true]
#
# Output: ["ELECTRONICS_50"]
#
# Explanation:
#
# First coupon is inactive (invalid).
# Second coupon is valid.
# Third coupon has invalid business line (invalid).
#
#
# Constraints:
#
# n == code.length == businessLine.length == isActive.length
# 1 <= n <= 100
# 0 <= code[i].length, businessLine[i].length <= 100
# code[i] and businessLine[i] consist of printable ASCII characters.
# isActive[i] is either true or false.
#
# Solution
# Python O(N + MlogM) O(M) Sorting
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid: list[int] = []
        n: int = len(code)
        order: list[str] = ["electronics", "grocery", "pharmacy", "restaurant"]
        for i in range(n):
            is_valid: bool = all(ch.isalnum() or ch == '_' for ch in code[i]) and bool(code[i])
            is_valid &= businessLine[i] in order and isActive[i]
            if is_valid: valid.append(i)
        valid.sort(key=lambda i: (order.index(businessLine[i]), code[i]))
        return [code[i] for i in valid]

# C++ O(N + MlogM) O(M) Sorting
class Solution {
public:
    vector<string> validateCoupons(vector<string>& code, vector<string>& businessLine, vector<bool>& isActive) {
        std::vector<int> valid;
        int n = code.size();
        std::vector<std::string> order = {"electronics", "grocery", "pharmacy", "restaurant"};
        for (int i = 0; i < n; ++i) {
            bool isValid = !code[i].empty();
            for (char& ch : code[i]) {
                if (!std::isalnum(ch) && ch != '_') {
                    isValid = false;
                    break;
                }
            }
            if (isValid && std::count(order.begin(), order.end(), businessLine[i]) && isActive[i]) valid.push_back(i);
        }

        std::sort(valid.begin(), valid.end(), [&](const int& i, const int& j) {
            int I = std::distance(order.begin(), std::find(order.begin(), order.end(), businessLine[i]));
            int J = std::distance(order.begin(), std::find(order.begin(), order.end(), businessLine[j]));
            if (J != I) return I < J;
            return code[i] < code[j];
        });
        std::vector<std::string> output;
        for (int& i : valid) output.push_back(code[i]);
        return output;
    }
};