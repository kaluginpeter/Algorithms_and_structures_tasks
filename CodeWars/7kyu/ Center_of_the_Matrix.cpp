/*
Create a method that returns the center of a 2-dim array.

It should return std::nullopt if there is no single center element.

You can assume all inputs will be rectangular matricies in array form. ex: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

FundamentalsMatrix
*/
// Solution
#include <vector>
#include <optional>

using opt_int_t = std::optional<int>;
using matrix_t = std::vector<std::vector<int>>;

opt_int_t center(const matrix_t& mat) {
    int n = mat.size();
    if (!(n & 1)) return std::nullopt;
    int m = mat[0].size();
    if (!(m & 1)) return std::nullopt;
    return mat[n / 2][m / 2];
}