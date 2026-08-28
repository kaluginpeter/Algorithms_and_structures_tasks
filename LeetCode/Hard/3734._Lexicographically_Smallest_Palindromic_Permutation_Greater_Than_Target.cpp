/*
You are given two strings s and target, each of length n, consisting of lowercase English letters.

Return the lexicographically smallest string that is both a palindromic permutation of s and strictly greater than target. If no such permutation exists, return an empty string.

 

Example 1:

Input: s = "baba", target = "abba"

Output: "baab"

Explanation:

The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
The lexicographically smallest permutation that is strictly greater than target is "baab".
Example 2:

Input: s = "baba", target = "bbaa"

Output: ""

Explanation:

The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
None of them is lexicographically strictly greater than target. Therefore, the answer is "".
Example 3:

Input: s = "abc", target = "abb"

Output: ""

Explanation:

s has no palindromic permutations. Therefore, the answer is "".

Example 4:

Input: s = "aac", target = "abb"

Output: "aca"

Explanation:

The only palindromic permutation of s is "aca".
"aca" is strictly greater than target. Therefore, the answer is "aca".
 

Constraints:

1 <= n == s.length == target.length <= 300
s and target consist of only lowercase English letters.
 

*/
// Solution
// C++ O(N^2) O(N) Greedy
class Solution {
public:
    string isPossible(int n, vector<int> freq, string cur, char &mid, string& target){
        for(int i=25; i>=0; --i){
            while(freq[i]){
                cur += (char)('a'+i);
                --freq[i];
            }
        }
        if(mid!='#'){
            string temp = cur;
            cur += mid;
            reverse(temp.begin(), temp.end());
            cur.append(temp.begin(), temp.end());
        }
        else {
            string temp = cur;
            reverse(temp.begin(), temp.end());
            cur.append(temp.begin(), temp.end());
        }
        return cur>target? cur : "";
    }

    string lexPalindromicPermutation(string s, string target) {
        int n = s.size();
        vector<int> freq(26, 0);
        if(n==1){
            if(s>target) return s;
            else return "";
        }
        for(char c : s) ++freq[c-'a'];
        char mid = '#';
        int oddCount = 0;
        for(int i=0; i<26; ++i){
            if(freq[i]%2){
                mid = (char)('a'+i);
                --freq[i];
                ++oddCount;
            }
            freq[i] /= 2; 
            if(oddCount>=2) return "";
        }

        n /= 2; 
        string res = "", prefix = "";
        for(int i=0; i<n; ++i){
            string cur = prefix;
            bool isThereAny = false;
            for(int j=0; j<26; ++j) {
                if (freq[j]) {
                    --freq[j];
                    cur += (char)('a' + j);
                    string isPos = isPossible(n, freq, cur, mid, target);
                    if(isPos!=""){
                        prefix = cur;
                        isThereAny = true;
                        if(res=="") res = isPos;
                        else res = min(res, isPos);
                        break;
                    }
                    ++freq[j];
                    cur.pop_back();
                }
            }
            if(!isThereAny) return "";
        }
        return res; 
    }
};