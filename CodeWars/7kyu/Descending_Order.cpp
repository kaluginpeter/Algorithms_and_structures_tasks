/*
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321

Fundamentals
*/
// Solution
#include <cinttypes>
#include <array>

uint64_t descendingOrder(uint64_t a)
{
  std::array<short, 10> hashmap = {};
  while (a) {
    ++hashmap[a % 10];
    a /= 10;
  }
  for (int digit = 9; digit >= 0; --digit) {
    for (int freq = 0; freq < hashmap[digit]; ++freq) a = a * 10 + digit;
  }
  return a;
}