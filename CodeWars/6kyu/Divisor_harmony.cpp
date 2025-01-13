/*
Consider the following:

The divisors of 6 are: 1, 2, 3 & 6 and their sum is 12. Now, 12/6 = 2.
The divisors of 28 are 1, 2, 4, 7, 14 & 28 and their sum is 56. Now, 56/28 = 2.
The divisors of 496 are 1, 2, 4, 8, 16, 31, 62, 124, 248, 496 and their sum is 992. Now, 992/496 = 2.
We shall say that (6,28,496) is a grouping with a ratio of 2.

Similarly, consider the grouping (30,140):

The divisors of 30 are: 1, 2, 3, 5, 6, 10, 15 & 30 and their sum is 72. Now, 72/30 = 12/5 = 2.4.
The divisors of 140 are 1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140 and their sum is 336. Now, 336/140 = 12/5 = 2.4.
We shall say that (30,140) is a grouping with a ratio of 12/5.

(6,28) and (30,140) are the only groupings in which every member of a group is 0 <= n < 200. The sum of the smallest members of each group is 6 + 30 = 36.

Given a range(a,b), return the sum of the smallest members of each group. As illustrated above:

every member of a group must be greater than or equal to a and less than b.
a group must have 2 or more members.
Examples:
solve(1,200) = 36, the sum of [6,30] as explained above
solve(1,250) = 168, the sum of [6, 12, 30, 40, 80]
solve(1,500) = 498, the sum of [6, 12, 30, 40, 66, 78, 80, 84, 102]

As you can see, for "solve(1,500)", we do not include all (6,28) & (6,496) & (28,496). We count the group once by including 6 only.
If there are no groups, return 0. Upper limit is 2000.

Good luck!

if you like this Kata, please try:

Simple division

Sub-array division

Algorithms
*/
double getComposition(int n) {
  int s = 0;
  for (int d = 1; d <= n; ++d) {
    if (n % d == 0) {
      s += d;
    }
  }
  return static_cast<double>(s) / static_cast<double>(n);
}

int solve(int a, int b) {
    int output = 0;
    std::unordered_map<double, std::vector<int>> hashmap;
    for (int i = a; i < b; ++i) {
        double pool = getComposition(i);
        hashmap[pool].push_back(i);
    }
    for (auto& p : hashmap) {
        if (p.second.size() > 1) {
            output += *std::min(p.second.begin(), p.second.end());
        }
    }
    return output;
}