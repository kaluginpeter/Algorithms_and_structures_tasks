/*
For "x", determine how many positive integers less than or equal to "x" are odd but not prime. Assume "x" is an integer between 1 and 10000.

Example: 5 has three odd numbers (1,3,5) and only the number 1 is not prime, so the answer is 1

Example: 10 has five odd numbers (1,3,5,7,9) and only 1 and 9 are not prime, so the answer is 2

Algorithms
*/
// Solution
#include <cmath>

bool isPrime(unsigned int n) {
  if (n % 2 == 0) return false;
  else if (n == 1) return false;
  unsigned int bound = std::sqrt(n) + 1;
  for (unsigned int d = 3; d < bound; d += 2) {
    if (n % d == 0) return false;
  }
  return true;
}

unsigned int oddNotPrime(unsigned int n){
  int output = 0;
  for (unsigned int number = 1; number <= n; number += 2) {
    if (!isPrime(number)) ++output;
  }
  return output;
}