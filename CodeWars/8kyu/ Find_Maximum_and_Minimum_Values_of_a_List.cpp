/* Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language ) that receive a list of integers as input, and return the largest and lowest number in that list, respectively.

Examples (Input -> Output)
* [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
* [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
* [42, 54, 65, 87, 0]             -> min = 0, max = 87
* [5]                             -> min = 5, max = 5
Notes
You may consider that there will not be any empty arrays/vectors.
FUNDAMENTALS
*/
// Solution
#include <vector>
using namespace std;

int min(vector<int> list){
    int min_number = list[0];
    for (int number : list) {
      min_number = std::min(min_number, number);
    }
    return min_number;
}

int max(vector<int> list){
    int max_number = list[0];
    for (int number : list) {
      max_number = std::max(max_number, number);
    }
    return max_number;
}