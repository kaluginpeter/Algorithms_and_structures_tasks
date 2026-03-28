# You are given a string of n lines, each substring being n characters long: For example:
#
# s = "abcd\nefgh\nijkl\nmnop"
#
# We will study some transformations of this square of strings.
#
# Symmetry with respect to the main cross diagonal: diag_2_sym (or diag2Sym or diag-2-sym)
#
# diag_2_sym(s) => "plhd\nokgc\nnjfb\nmiea"
# Counterclockwise rotation 90 degrees: rot_90_counter (or rot90Counter or rot-90-counter)
#
# rot_90_counter(s)=> "dhlp\ncgko\nbfjn\naeim"
# selfie_diag2_counterclock (or selfieDiag2Counterclock or selfie-diag2-counterclock) It is initial string + string obtained by symmetry with respect to the main cross diagonal + counterclockwise rotation 90 degrees .
#
# s = "abcd\nefgh\nijkl\nmnop" -->
# "abcd|plhd|dhlp\nefgh|okgc|cgko\nijkl|njfb|bfjn\nmnop|miea|aeim"
# or printed for the last:
#
# selfie_diag2_counterclock
# abcd|plhd|dhlp
# efgh|okgc|cgko
# ijkl|njfb|bfjn
# mnop|miea|aeim
# Task
# Write these functions diag_2_sym, rot_90_counter, selfie_diag2_counterclock
# and
#
# high-order function oper(fct, s) where fct is the function of one variable f to apply to the string s (fct will be one of diag_2_sym, rot_90_counter, selfie_diag2_counterclock)
# Examples
# s = "abcd\nefgh\nijkl\nmnop"
# oper(diag_2_sym, s) => "plhd\nokgc\nnjfb\nmiea"
# oper(rot_90_counter, s) => "dhlp\ncgko\nbfjn\naeim"
# oper(selfie_diag2_counterclock, s) => "abcd|plhd|dhlp\nefgh|okgc|cgko\nijkl|njfb|bfjn\nmnop|miea|aeim"
# Notes
# The form of the parameter fct in oper changes according to the language. You can see each form according to the language in "Your test cases".
# It could be easier to take these katas from number (I) to number (IV)
# Bash Note: The ouput strings should be separated by \r instead of \n. See "Sample Tests".
# AlgorithmsStrings
# Solution
#include <string>
#include <vector>
#include <sstream>
using namespace std;

class Opstrings4 {
public:
    static vector<string> split(const string& s) {
        vector<string> res;
        stringstream ss(s);
        string line;
        while (getline(ss, line)) res.push_back(line);
        return res;
    }
    static string join(const vector<string>& v) {
        string res;
        for (int i = 0; i < v.size(); i++) {
            res += v[i];
            if (i != v.size() - 1) res += '\n';
        }
        return res;
    }
    static string diag2Sym(const string& s) {
        vector<string> a = split(s);
        int n = a.size();
        vector<string> res(n, string(n, ' '));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                res[i][j] = a[n - 1 - j][n - 1 - i];
            }
        }
        return join(res);
    }
    static string rot90Counter(const string& s) {
        vector<string> a = split(s);
        int n = a.size();
        vector<string> res(n, string(n, ' '));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                res[i][j] = a[j][n - 1 - i];
            }
        }
        return join(res);
    }
    static string selfieDiag2Counterclock(const string& s) {
        vector<string> orig = split(s);
        vector<string> d2 = split(diag2Sym(s));
        vector<string> r90 = split(rot90Counter(s));

        int n = orig.size();
        vector<string> res(n);

        for (int i = 0; i < n; i++) {
            res[i] = orig[i] + "|" + d2[i] + "|" + r90[i];
        }
        return join(res);
    }
    template<typename Func>
    static string oper(Func fct, const string& s) {
        return fct(s);
    }
};