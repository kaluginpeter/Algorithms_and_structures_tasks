/*
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.

Happy Coding!

MATHEMATICSFUNDAMENTALS
*/
// Solution
#include <string>
#include <iostream>
#include <sstream>

int square_digits(int num) {
    std::string num_str = std::to_string(num);
    std::ostringstream output;
    for (char digit : num_str) {
        int digit_int = digit - '0';
        output << (digit_int * digit_int);
    }
    std::string result_str = output.str();
    std::cout << result_str << std::endl;
    return std::stoi(result_str);
}