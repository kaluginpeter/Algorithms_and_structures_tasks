/*
The number
89
89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number:
89
=
8
1
+
9
2
89=8
1
 +9
2


The next number in having this property is
135
135:

See this property again:
135
=
1
1
+
3
2
+
5
3
135=1
1
 +3
2
 +5
3


Task
We need a function to collect these numbers, that may receive two integers
a
a,
b
b that defines the range
[
a
,
b
]
[a,b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

Examples
Let's see some cases (input -> output):

1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
If there are no numbers of this kind in the range
[
a
,
b
]
[a,b] the function should output an empty list.

90, 100 --> []
Enjoy it!!

FundamentalsMathematics
*/
// Solution
#include <vector>
#include <cmath>

bool isEurika(unsigned int number) {
  unsigned int number_ = number;
  int power = 1;
  while (std::pow(10, power) <= number) {
    ++power;
  }
  unsigned int sumDigits = 0;
  while (power) {
    sumDigits += std::pow(number % 10, power);
    --power;
    number /= 10;
  }
  return sumDigits == number_;
}

std::vector<unsigned int> sumDigPow(unsigned int a, unsigned int b) {
  std::vector<unsigned int> output;
  for (unsigned int number = a; number <= b; ++number) {
    if (isEurika(number)) {
      output.push_back(number);
    }
  }
  return output;
}