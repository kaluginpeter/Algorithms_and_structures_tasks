/*
Given positive integers a and b as strings, evaluate a / b and return the quotient and the remainder as strings in the form [quotient, remainder].

a and b can be very large (at the order of 10^150 to 10^200)
As usual, your result should not have leading 0s
require is disabled in JavaScript. Do it yourself ;-)
StringsFundamentalsBig IntegersAlgorithms
*/
// Solution
#include <string>
#include <utility>
#include <algorithm>
using std::string;
using std::pair;
string trim(const string& s) {
    size_t pos = s.find_first_not_of('0');
    if (pos == string::npos) return "0";
    return s.substr(pos);
}
bool ge(const string& a, const string& b) {
    string x = trim(a), y = trim(b);
    if (x.size() != y.size()) return x.size() > y.size();
    return x >= y;
}
string subtract(string a, string b) {
    int i = a.size() - 1;
    int j = b.size() - 1;
    int borrow = 0;
    while (i >= 0) {
        int da = (a[i] - '0') - borrow;
        int db = (j >= 0 ? b[j] - '0' : 0);
        if (da < db) {
            da += 10;
            borrow = 1;
        } else borrow = 0;
        a[i] = char('0' + (da - db));
        --i;
        --j;
    }
    return trim(a);
}
string multiply_digit(const string& a, int d) {
    if (d == 0) return "0";
    int carry = 0;
    string res;
    for (int i = a.size() - 1; i >= 0; --i) {
        int val = (a[i] - '0') * d + carry;
        res.push_back(char('0' + (val % 10)));
        carry = val / 10;
    }
    if (carry) res.push_back(char('0' + carry));
    std::reverse(res.begin(), res.end());
    return res;
}

pair<string, string> divide_strings(const string& a, const string& b) {
    string dividend = trim(a);
    string divisor  = trim(b);
    if (dividend == "0") return {"0", "0"};
    string quotient;
    string remainder = "0";
    for (char c : dividend) {
        remainder = trim(remainder + c);
        int q = 0;
        for (int d = 9; d >= 1; --d) {
            if (ge(remainder, multiply_digit(divisor, d))) {
                q = d;
                remainder = subtract(remainder, multiply_digit(divisor, d));
                break;
            }
        }
        quotient.push_back(char('0' + q));
    }
    return { trim(quotient), trim(remainder) };
}