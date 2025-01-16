/*
Ore Numbers (also called Harmonic Divisor Numbers) are numbers for which the harmonic mean of all their divisors (including the number itself) equals an integer.

For example, 6 is an Ore Number because its harmonic mean is exactly 2:

H(6) = 4 / (1/1 + 1/2 + 1/3 + 1/6) = 2
Your task is to complete the function returns true if the given number is an Ore Number and false otherwise.

You can assume all inputs will be valid positive integers.

Hint: The harmonic mean is the total number of divisors divided by the sum of their reciprocals.

MathematicsFundamentalsAlgorithms
*/
// Solution
#include <cmath>

bool isOre(unsigned int n){
    if (n == 0) return false;
    double totalSum = 0;
    int count = 0;
    for (unsigned int i = 1; i <= sqrt(n); ++i) {
        if (n % i == 0) {
            totalSum += (double)1 / (double)i;
            count++;
            if (i != n / i) {
                totalSum += (double)1 / (double)(n / i);
                count++;
            }
        }
    }
    double result = (double)count / totalSum;
    return fabs(result - round(result)) < 1e-9;
}