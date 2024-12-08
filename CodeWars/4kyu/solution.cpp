/*
In mathematics, the factorial of integer n is written as n!. It is equal to the product of n and every integer preceding it. For example: 5! = 1 x 2 x 3 x 4 x 5 = 120

Your mission is simple: write a function that takes an integer n and returns the value of n!.

You are guaranteed an integer argument. For any values outside the non-negative range, return null, nil or None (return an empty string "" in C and C++). For non-negative numbers a full length number is expected for example, return 25! =  "15511210043330985984000000"  as a string.

For more on factorials, see http://en.wikipedia.org/wiki/Factorial

NOTES:

The use of BigInteger or BigNumber functions has been disabled, this requires a complex solution

I have removed the use of require in the javascript language.

AlgorithmsBig Integers
*/
// Solution
#include <string>
void multiply(int n, std::string& digits) {
  long long additional = 0;
  for (size_t index = 0; index < digits.size(); ++index) {
    long long result = (digits[index] - '0') * n + additional;
    additional = result / 10;
    digits[index] = '0' + (result % 10);
  }
  while (additional) {
    digits += std::to_string(additional % 10);
    additional /= 10;
  }
}

std::string getFactorial(int n) {
  std::string digits = "1";
  for (int move = 1; move <= n; ++move) {
    multiply(move, digits);
  }
  return digits;
}

std::string factorial(int n){
  if (n < 0) {
    return "";
  }
  std::string result = getFactorial(n);
  std::reverse(result.begin(), result.end());
  return result;
}