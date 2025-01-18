/*
Your task is to calculate some different things on a given string. So this kata checks some basics, it's not too difficult.

So what to do?

Input: String which consists of integers and chars separated by ";"

1. Recognize and sum all numbers
2. Calculate average and round it to int
3. Calculate sum of the digits from result of 2.
4. Check if this result is divisible by 5
Return your results as a string containing points 2.,3. and 4., i.e. "2.,3.,4." (comma separated string with single results, see example)

Easy example:

Input: "-500;500;1500;-;+++;;;ABC"
Output: "500,5,TRUE"

Why?
2.=> -500+500+1500=1500 / 3 = 500
3.=> 5+0+0=5
4.=> 5/5=1 => divisible => TRUE (not => FALSE)
i.e. Output= "500,5,TRUE"
First there are some static tests, later on random tests too...


Hope you have fun:-)!
StringsFundamentalsMathematicsArrays
*/
// Solution
#include <bits/stdc++.h>
std::string calculateArray(std::string stringArray)
{
    std::string result = "";
    std::istringstream stream(stringArray);
    std::string item;
    std::vector<int> numbers;

    while (std::getline(stream, item, ';')) {
        if (!item.empty()) {
            if ((item[0] == '-' && item.size() > 1 && std::all_of(item.begin() + 1, item.end(), ::isdigit)) ||
                (std::all_of(item.begin(), item.end(), ::isdigit))) {
                numbers.push_back(std::atoi(item.c_str()));
            }
        }
    }

    int totalSum = std::accumulate(numbers.begin(), numbers.end(), 0);
    int av = (int)std::round((double)totalSum / (double)numbers.size());
    std::string second = std::to_string(av);
    result += second + ',';
    int third = 0;
    for (char& d : second) {
      third += static_cast<int>(d) - 48;
    }
    result += std::to_string(third) + ',';
    result += (third % 5 == 0? "TRUE" : "FALSE");

    return result;
}