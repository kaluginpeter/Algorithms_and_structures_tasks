/*
Task
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
FundamentalsArraysSorting
*/
// Solution
class Kata
{
public:
    std::vector<int> sortArray(std::vector<int> array)
    {
        if (!array.size()) {
          return array;
        }
        std::vector<int> oddIdxs;
        std::vector<int> odds;
        for (int index = 0; index <= array.size() - 1; ++index) {
            if (array[index] % 2 != 0) {
              oddIdxs.push_back(index);
              odds.push_back(array[index]);
            }
        }
        std::sort(odds.begin(), odds.end());
        while (oddIdxs.size()) {
          int index = oddIdxs[oddIdxs.size() - 1];
          int number = odds[odds.size() - 1];
          oddIdxs.pop_back();
          odds.pop_back();
          array[index] = number;
        }
        return array;
    }
};