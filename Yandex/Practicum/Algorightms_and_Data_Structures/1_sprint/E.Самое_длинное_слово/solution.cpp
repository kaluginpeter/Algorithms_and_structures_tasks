#include <iostream>
#include <string>

void solution(int L, std::string& sentence) {
    /*
    Time Complexity O(N)
    Memory Complexity O(L), where L is length of the longest word
    */
    std::string maxWord = "";
    int maxLength = 0;
    std::string curWord = "";
    int curLength = 0;
    for (int index = 0; index < L; ++index) {
        if (sentence[index] == ' ') {
            if (curLength > maxLength) {
                maxLength = curLength;
                maxWord = curWord;
            }
            curLength = 0;
            curWord = "";
        } else {
            ++curLength;
            curWord += sentence[index];
        }
    }
    if (curLength > maxLength) {
        maxLength = curLength;
        maxWord = curWord;
    }
    std::cout << maxWord << "\n" << maxLength << std::endl;
};


int main() {
    int L;
    std::cin >> L;
    std::cin.ignore();
    std::string sentence;
    std::getline(std::cin, sentence);
    solution(L, sentence);
}