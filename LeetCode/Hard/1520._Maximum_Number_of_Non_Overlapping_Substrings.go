/*
Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:

The substrings do not overlap, that is for any two substrings s[i..j] and s[x..y], either j < x or i > y is true.
A substring that contains a certain character c must also contain all occurrences of c.
Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in any order.

 

Example 1:

Input: s = "adefaddaccc"
Output: ["e","f","ccc"]
Explanation: The following are all the possible substrings that meet the conditions:
[
  "adefaddaccc"
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.
Example 2:

Input: s = "abbaccd"
Output: ["d","bb","cc"]
Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.
 

Constraints:

1 <= s.length <= 105
s contains only lowercase English letters.
 

*/
// Solution
// Go O(N) O(N) HashMap Greedy
import (
    "slices"
    "cmp"
)
func maxNumOfSubstrings(s string) []string {
    var first, last [26]int = [26]int{}, [26]int{};
    for i := 0; i < 26; i++ {
        first[i] = -1
        last[i] = -1
    }
    // Find first and last occurences of each character in a string
    // 26 possible substrings without validation
    for i, ch := range s {
        var ptr int = int(ch - 'a')
        if first[ptr] == -1 { first[ptr] = i }
        last[ptr] = i
    }
    // Find actual length of substring such start with i'th character
    var substrings [][2]int = [][2]int{}
    for i := 0; i < 26; i++ {
        if first[i] == -1 { continue }
        var start, end int = first[i], last[i]
        var needToStartAgain bool = true
        for needToStartAgain {
            needToStartAgain = false
            for j := start + 1; j < end; j++ {
                var curPtr int = int(s[j] - 'a')
                // If we meet character that firstly occur earlier that our start
                // Can we up to 26 rescanning at all
                if first[curPtr] < start {
                    start = first[curPtr]
                    needToStartAgain = true
                    break
                }
                end = max(end, last[curPtr])
            }
        }
        substrings = append(substrings, [2]int{start, end})
    }
    // Sort by earliest start and minimum length
    slices.SortFunc(substrings, func(x, y [2]int) int {
        if x[1] != y[1] { return cmp.Compare(x[1], y[1]) }
        return cmp.Compare(-x[0], -y[0])
    })
    // Use scheduler selecting events idea
    var ptr int = 0
    var output []string = []string{}
    for i := 0; i < len(substrings); i++ { // Up to 26 possible substrings
        if substrings[ptr][1] < substrings[i][0] {
            output = append(output, s[substrings[ptr][0]: substrings[ptr][1] + 1])
            ptr = i
        }
    }
    // string has always at least one substring(itself)
    output = append(output, s[substrings[ptr][0]: substrings[ptr][1] + 1])
    return output
}

// You can hardcode choosing every alphabet. There at most 26 substrings
// Each character in substring are bounded to maximum between all last 
// occurences of character in that range [startCh:endCh]
// You need to choose only minimum sum of length. For that just precalculate the entire
// substrings and sort them by length. The question now is to how to choose maximum number?
// The answer seems to be like in scheduler problem, where we need to select maximum
// number of earliest events.
// Overall complexity is linear O(N) and the memory is O(N).

// C++ O(N) O(N) Greedy HashMap
class Solution {
public:
    vector<string> maxNumOfSubstrings(string s) {
        std::array<int, 26> first{}, last{};
        std::fill(first.begin(), first.end(), -1);
        std::fill(last.begin(), last.end(), -1);
        for (size_t i = 0; i < s.size(); ++i) {
            if (first[s[i] - 'a'] == -1) first[s[i] - 'a'] = i;
            last[s[i] - 'a'] = i;
        }
        std::vector<std::pair<int, int>> substrings;
        for (size_t i = 0; i < 26; ++i) {
            if (first[i] == -1) continue;
            int start = first[i], end = last[i];
            bool needToStartAgain = true;
            while (needToStartAgain) {
                needToStartAgain = false;
                for (size_t j = start + 1; j < end; ++j) {
                    if (first[s[j] - 'a'] < start) {
                        start = first[s[j] - 'a'];
                        needToStartAgain = true;
                        break;
                    }
                    end = std::max(end, last[s[j] - 'a']);
                }
            }
            substrings.push_back({start, end});
        }
        std::sort(substrings.begin(), substrings.end(), [](const std::pair<int, int>& x, const std::pair<int, int>& y) {
            if (x.second != y.second) return x.second < y.second;
            return -x.first < -y.first;
        });
        size_t ptr = 0;
        std::vector<std::string> output;
        for (size_t i = 0; i < substrings.size(); ++i) {
            if (substrings[ptr].second < substrings[i].first) {
                output.push_back(s.substr(substrings[ptr].first, substrings[ptr].second - substrings[ptr].first + 1));
                ptr = i;
            }
        }
        output.push_back(s.substr(substrings[ptr].first, substrings[ptr].second - substrings[ptr].first + 1));
        return output;
    }
};