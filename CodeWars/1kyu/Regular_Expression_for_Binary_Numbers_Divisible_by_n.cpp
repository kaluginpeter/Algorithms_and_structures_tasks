/*
Regular Expression for Binary Numbers Divisible by n
Create a function that will return a regular expression string that is capable of evaluating binary strings (which consist of only 1s and 0s) and determining whether the given string represents a number divisible by n.

Tests
Inputs 1 <= n <= 18 will be tested

Each n will be tested against random invalid tests and random valid tests (which may or may not pass the regex test itself, accordingly).

Notes
Strings that are not binary numbers should be rejected.
Keep your solution under 5000 characters. This means you can't hard-code the answers.
Only these characters may be included in your returned string:
01?:*+^$()[]|

C++ Notes
The second anti-cheat test checks if you used the STL's regex library in your code.
The macro constant _GLIBCXX_REGEX_STATE_LIMIT which limits the maximum size of a regex has been set to 400000, as the default limit would be too constraining for the larger inputs.
AlgorithmsPuzzlesRegular ExpressionsStrings
*/
// Solution
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

using DFA = vector<unordered_map<int, string>>;

static DFA build_dfa(int n) {
    DFA d(n);
    for (int r = 0; r < n; ++r) {
        d[r][(r * 2) % n] = "0";
        d[r][(r * 2 + 1) % n] = "1";
    }
    return d;
}

static string dfa2regex(const DFA& d) {
    int m = (int)d.size() - 1;
    if (m == 0) return "^(" + d[0].at(0) + ")+$";
    auto sub = [&](int s, int e) -> string {
        string sme = d[s].at(m);
        if (d[m].count(m)) sme += "(?:" + d[m].at(m) + ")*";
        sme += d[m].at(e);
        if (d[s].count(e)) return "(?:" + d[s].at(e) + "|" + sme + ")";
        return sme;
    };

    auto link = [&](int s, int e) -> string {
        if (d[s].count(m) && d[m].count(e)) return sub(s, e);
        return d[s].at(e);
    };

    auto ends = [&](int s) -> unordered_set<int> {
        unordered_set<int> result;
        for (auto& p : d[s]) result.insert(p.first);
        if (d[s].count(m)) {
            for (auto& p : d[m]) result.insert(p.first);
        }
        return result;
    };
    DFA new_d;
    for (int s = 0; s < (int)d.size(); ++s) {
        if (s == m) continue;
        unordered_map<int, string> node;
        for (int e : ends(s)) {
            if (e == m) continue;
            node[e] = link(s, e);
        }
        new_d.push_back(move(node));
    }
    return dfa2regex(new_d);
}

std::string regex_divisible_by(int n)
{
    if (n == 1) return "^[10]+$";
    return dfa2regex(build_dfa(n));
}