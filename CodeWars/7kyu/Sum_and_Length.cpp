/*
Sum and Length
In this kata you must return a string value, where the first part is the sum of positive numbers and the second part is the number of negative numbers.

Knowing that the first 0 is negative, the second is positive, the third is negative, and so on...

Examples
[-1,2,3,4,0,1,0,-2,0,-3]

==> '10 5'

sum of positives: 10 = 2 + 3 + 4 + 0 (second) + 1
count of negatives: 5 ( -1, 0 (first), -2, 0 (third), -3 )
Fundamentals
*/
// Solution
#include<vector>

std::string sumLength(std::vector<int> input)
{
    uint32_t positive = 0, negative = 0, shouldCount = 1;
    for (int& num : input) {
        if (num < 0) ++negative;
        else if (!num) {
            negative += shouldCount;
            shouldCount = (shouldCount + 1) % 2;
        }
        else positive += num;
    }
    return std::to_string(positive) + " " + std::to_string(negative);
}