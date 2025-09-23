# Given two version numbers, version1 and version2, compare them.
#
# Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.
#
# To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.
#
# Return the following:
#
# If version1 < version2, return -1.
# If version1 > version2, return 1.
# Otherwise, return 0.
#
#
# Example 1:
#
# Input: version1 = "1.01", version2 = "1.001"
# Output: 0
# Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
# Example 2:
#
# Input: version1 = "1.0", version2 = "1.0.0"
# Output: 0
# Explanation: version1 does not specify revision 2, which means it is treated as "0".
# Example 3:
#
# Input: version1 = "0.1", version2 = "1.1"
# Output: -1
# Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2.
#
#
# Constraints:
#
# 1 <= version1.length, version2.length <= 500
# version1 and version2 only contain digits and '.'.
# version1 and version2 are valid version numbers.
# All the given revisions in version1 and version2 can be stored in a 32-bit integer.
# Solution O(N) O(N)
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = [int(i) for i in version1.split('.')]
        version2 = [int(i) for i in version2.split('.')]
        v1, v2 = len(version1), len(version2)
        for i in range(min(v1, v2)):
            if version1[i] < version2[i]:
                return -1
            elif version1[i] > version2[i]:
                return 1
        if v1 == v2:
            return 0
        elif v1 > v2:
            return [1, 0][all(version1[i] == 0 for i in range(v2, v1))]
        return [-1, 0][all(version2[i] == 0 for i in range(v1, v2))]

# Python O(max(N, M)) O(1) TwoPointers
class Solution:
    def get_number(self, ptr: int, version: str) -> tuple[int, int]:
        output: int = 0
        while ptr < len(version) and version[ptr] != '.':
            output = output * 10 + int(version[ptr])
            ptr += 1
        if ptr < len(version): ptr += 1
        return (ptr, output)
    def compareVersion(self, version1: str, version2: str) -> int:
        i: int = 0
        j: int = 0
        while i < len(version1) or j < len(version2):
            i, x = self.get_number(i, version1)
            j, y = self.get_number(j, version2)
            if x == y: continue
            return [1, -1][x < y]
        return 0

# C++ O(max(N, M)) O(1) TwoPointers
class Solution {
public:
    int getNumber(size_t& ptr, std::string& version) {
        int output = 0;
        while (ptr < version.size() && version[ptr] != '.') {
            output = output * 10 + (version[ptr] - '0');
            ++ptr;
        }
        if (ptr < version.size()) ++ptr;
        return output;
    }
    int compareVersion(string version1, string version2) {
        size_t i = 0, j = 0;
        while (i < version1.size() || j < version2.size()) {
            int x = getNumber(i, version1);
            int y = getNumber(j, version2);
            if (x == y) continue;
            return (x > y ? 1 : -1);
        }
        return 0;
    }
};