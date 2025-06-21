/*
Task
Raj has got into a problem, he solved the triangle pattern but stuck in the codes of "inverse triangle". Help him with the codes and remember to get the output as per given in examples below.

Rules:
Take input as n which is always a natural number
Space between each digit
No space after the rows end
Examples
If n = 5, output should be:

 1 1 1 1 1
  2 2 2 2
   3 3 3
    4 4
     5
If n = 9, output should be:

 1 1 1 1 1 1 1 1 1
  2 2 2 2 2 2 2 2
   3 3 3 3 3 3 3
    4 4 4 4 4 4
     5 5 5 5 5
      6 6 6 6
       7 7 7
        8 8
         9
If n = 16, output should be:

 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
  2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
   3 3 3 3 3 3 3 3 3 3 3 3 3 3
    4 4 4 4 4 4 4 4 4 4 4 4 4
     5 5 5 5 5 5 5 5 5 5 5 5
      6 6 6 6 6 6 6 6 6 6 6
       7 7 7 7 7 7 7 7 7 7
        8 8 8 8 8 8 8 8 8
         9 9 9 9 9 9 9 9
          0 0 0 0 0 0 0
           1 1 1 1 1 1
            2 2 2 2 2
             3 3 3 3
              4 4 4
               5 5
                6
ASCII ArtFundamentals
*/
// Solution
std::string pattern(int n)
{
    std::string output = "";
    for (int i = 1; i <= n; ++i) {
        std::string row = "", identation = " ";
        for (int j = 0; j < i; ++j) row += identation;
        bool flag = true;
        int count = 0;
        while (count < n - (i - 1)) {
          if (flag) {
            ++count;
            row += std::to_string(i % 10);
          } else row += identation;
          flag = !flag;
        }
        output += (i == 1 ? "" : "\n") + row;
    }
    return output;
}