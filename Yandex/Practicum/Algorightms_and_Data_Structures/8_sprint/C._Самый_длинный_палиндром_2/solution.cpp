#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(M) => O(1)
    */
    std::string sequence;
    std::cin >> sequence;
    std::unordered_map<int, int> histogram;
    for (char& letter : sequence) ++histogram[(int)letter];
    char median = '0';
    std::string part = "";
    for (int idx = 97; idx <= 122; ++idx) {
        if (!histogram.count(idx)) continue;
        for (int i = 0; i < histogram[idx] / 2; ++i) part.push_back((char)idx);
        if (histogram[idx] % 2 != 0 && median == '0') median = (char)idx;
    }
    std::string palindrome = part;
    if (median != '0') palindrome.push_back(median);
    std::reverse(part.begin(), part.end());
    palindrome += part;
    std::cout << palindrome << "\n";
}


int main() {
    solution();
}