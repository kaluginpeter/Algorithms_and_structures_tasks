/*
In this Kata, you will be given a string and your task will be to return a list of ints detailing the count of uppercase letters, lowercase, numbers and special characters (everything else), as follows.

The order is: uppercase letters, lowercase letters, numbers and special characters.

"*'&ABCDabcde12345" --> [ 4, 5, 5, 3 ]
More examples in the test cases.

Good luck!

FUNDAMENTALS
*/
// Solution
std::vector<int> solve(std::string s){
    std::vector<int> output(4, 0);
    for (char lt : s) {
      if (lt >= 'A' && lt <= 'Z') {
        output[0] += 1;
      } else if (lt >= 'a' && lt <= 'z') {
        output[1] += 1;
      } else if (lt >= '0' && lt <= '9') {
        output[2] += 1;
      } else {
        output[3] += 1;
      }
    }
  return output;
}