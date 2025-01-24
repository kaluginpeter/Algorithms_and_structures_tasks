/*
Get the number n to return the sequence from n to 1. The number n can be negative and also large number. (See the range as the following)

Example :
n=5  >> [5,4,3,2,1]
n=-1 >> [-1,0,1]

Range :
Python     -9999 < n < 9999
Javascript -9999 < n < 9999
c++        -9999 < n < 9999
Crystal    -9999 < n < 9999
Ruby       -9999 < n < 9999
Fundamentals
*/
// Solution
std::vector<int> seqToOne(int n) {
  std::vector<int> output;
  if (n < 0) {
    for (int num = n; num <= 1; ++num) {
      output.push_back(num);
    }
  } else {
    for (int num = n; num >= 1; --num) {
      output.push_back(num);
    }
  }
  return output;
}
