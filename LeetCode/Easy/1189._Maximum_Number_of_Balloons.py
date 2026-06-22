# Given a string text, you want to use the characters of text
# to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.
#
# Example 1:
#
#
# Input: text = "nlaebolko"
# Output: 1
# Example 2:
#
# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:
#
# Input: text = "leetcode"
# Output: 0
#
# Constraints:
# 1 <= text.length <= 104
# text consists of lower case English letters only.
# Solution
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word, l, count, flag = '', ['b', 'a', 'l', 'l', 'o', 'o', 'n'], 0, False
        for i in text:
            if i in 'balloon':
                word += i
        while word:
            for i in l:
                if i in word:
                    count +=1
                    word = word[:word.index(i)] + word[word.index(i)+1:]
                    continue
                if i not in word:
                    flag = True
                    break
            if flag:
                break
        return count // 7


# Python O(N) O(D) HashMap
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap: dict[str, int] = defaultdict(int)
        for ch in text: hashmap[ch] += 1
        mx: int = float('inf')
        mx = min(mx, hashmap['b'])
        mx = min(mx, hashmap['a'])
        mx = min(mx, hashmap['l'] >> 1)
        mx = min(mx, hashmap['o'] >> 1)
        mx = min(mx, hashmap['n'])
        return mx

# C++ O(N) O(D) HashMap
class Solution {
public:
    int maxNumberOfBalloons(string text) {
        std::array<int, 26> hashmap{};
        for (char& ch : text) ++hashmap[ch - 'a'];
        int mx = INT32_MAX;
        mx = std::min(mx, hashmap['b' - 'a']);
        mx = std::min(mx, hashmap['a' - 'a']);
        mx = std::min(mx, hashmap['l' - 'a'] >> 1);
        mx = std::min(mx, hashmap['o' - 'a'] >> 1);
        mx = std::min(mx, hashmap['n' - 'a']);
        return mx;
    }
};