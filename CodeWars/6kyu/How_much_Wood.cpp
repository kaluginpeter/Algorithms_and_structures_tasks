/*
You're a fantastic woodworker and you love to make picture frames. You want to know exactly what length of trim will be required in order to make a specified frame.

You are given the inside height and length of the desired frame as well as the width of the trim. We will assume you have the best blade ever made, to cut the wood up. It's so good, the blade has no width, so it doesn't remove any extra material with each cut.

Since you want the frame to look good, you'll be cutting 45° miter joints on each piece.

Frame

You will receive an array of measurements in the following order:

[height, length, width]
The measurements are going to be given to you in string format with some examples below:

[`1' 2 3/8"`, `1' 6"`, `1"`]
[`4"`, `1 1/2"`, `5/32"`]
Your job is to return a string that gives the length of trim required. We will use normal measuring tape denominations of 2,4,8,16,32 if any fractions are needed. Remember that the interior edge must be from the same side of the trim.

Expected Output Format:
Like the input, your output should show any feet followed by the ' symbol then any inches including the fractions followed by the " symbol. Use the lowest denominator for the fraction (i.e. 1/2 instead of 16/32). For those not familiar with imperial measurements, 12" = 1'.

FundamentalsRegular ExpressionsStrings
*/
// Solution
#include <bits/stdc++.h>
using ll = long long;
struct Fraction {
    ll num, den;
    Fraction(ll n = 0, ll d = 1) : num(n), den(d) {
        ll g = std::gcd(num, den);
        num /= g; den /= g;
    }
    Fraction operator+(const Fraction& o) const {
        return Fraction(num * o.den + o.num * den, den * o.den);
    }
    Fraction operator*(ll k) const {
        return Fraction(num * k, den);
    }
};
Fraction parse(const std::string& s) {
    ll feet = 0, inches = 0, fn = 0, fd = 1;
    std::istringstream iss(s);
    std::string token;
    while (iss >> token) {
        if (token.back() == '\'') feet = std::stoll(token);
        else if (token.back() == '"') {
            token.pop_back();
            auto pos = token.find('/');
            if (pos != std::string::npos) {
                fn = std::stoll(token.substr(0, pos));
                fd = std::stoll(token.substr(pos + 1));
            } else inches = std::stoll(token);
        }
        else if (token.find('/') != std::string::npos) {
            auto pos = token.find('/');
            fn = std::stoll(token.substr(0, pos));
            fd = std::stoll(token.substr(pos + 1));
        }
        else inches = std::stoll(token);
    }

    Fraction total(feet * 12 + inches, 1);
    return total + Fraction(fn, fd);
}
std::string format(Fraction f) {
    ll feet = f.num / (f.den * 12);
    f.num %= (f.den * 12);
    ll inches = f.num / f.den;
    f.num %= f.den;
    std::ostringstream out;
    if (feet) out << feet << "'";
    if (inches || f.num) {
        if (feet) out << " ";
        if (inches) {
            out << inches;
            if (f.num) out << " " << f.num << "/" << f.den;
        } else if (f.num) out << f.num << "/" << f.den;
        out << "\"";
    }
    return out.str();
}
std::string wood_length(const std::array<std::string, 3>& dimensions) {
    Fraction H = parse(dimensions[0]);
    Fraction L = parse(dimensions[1]);
    Fraction W = parse(dimensions[2]);
    Fraction total = H * 2 + L * 2 + W * 8;
    return format(total);
}