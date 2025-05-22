/*
Determine the total number of digits in the integer (n>=0) given as input to the function. For example, 9 is a single digit, 66 has 2 digits and 128685 has 6 digits. Be careful to avoid overflows/underflows.

All inputs will be valid.

StringsFundamentals
*/
// Solution
#include <stdint.h>

int digits(uint64_t n) {
  if (!n) return 1;
  int places = 0;
  while (n) {
    ++places;
    n /= 10;
  }
  return places;
}