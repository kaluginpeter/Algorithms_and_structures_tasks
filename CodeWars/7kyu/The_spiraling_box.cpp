//# Task
//# Given two positive integers m (width) and n (height), fill a two-dimensional list (or array) of size m-by-n in the following way:
//#
//# (1) All the elements in the first and last row and column are 1.
//#
//# (2) All the elements in the second and second-last row and column are 2, excluding the elements from step 1.
//#
//# (3) All the elements in the third and third-last row and column are 3, excluding the elements from the previous steps.
//#
//# And so on ...
//#
//# Examples
//# Given m = 5, n = 8, your function should return
//#
//# [[1, 1, 1, 1, 1],
//#  [1, 2, 2, 2, 1],
//#  [1, 2, 3, 2, 1],
//#  [1, 2, 3, 2, 1],
//#  [1, 2, 3, 2, 1],
//#  [1, 2, 3, 2, 1],
//#  [1, 2, 2, 2, 1],
//#  [1, 1, 1, 1, 1]]
//# Given m = 10, n = 9, your function should return
//#
//# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
//#  [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
//#  [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
//#  [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
//#  [1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
//#  [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
//#  [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
//#  [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
//#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
//# Bird mountain generalizes this kata in a fun way.
//#
//# ArraysFundamentals
#include<cmath>
#include<algorithm>

std::vector<std::vector<int>> create_box(int m, int n) {
     std::vector<std::vector<int>> output;
     for (int r = 0; r < n; ++r) {
         std::vector<int> row;
         for(int c = 0; c < m; ++c) {
             row.push_back(std::min({r + 1, c + 1, std::abs(n - r), std::abs(m - c)}));
         }
         output.push_back(row);
     }
     return output;
}