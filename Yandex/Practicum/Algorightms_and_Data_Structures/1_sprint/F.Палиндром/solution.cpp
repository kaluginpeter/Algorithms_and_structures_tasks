#include <iostream>
#include <string>

void solution(std::string& sentence) {
    /*
    Time Complexity O(N)
    Memory Complexity O(1)
    */
    bool isValid = true;
    int left = 0;
    int right = sentence.size() - 1;
    while (left < right) {
        while (left < right && !std::isalnum(sentence[left])) {
            ++left;
        }
        while (left < right && !std::isalnum(sentence[right])) {
            --right;
        }
        if (left < right && (char)std::tolower(sentence[left]) != (char)std::tolower(sentence[right])) {
            isValid = false;
            break;
        }
        ++left;
        --right;
    }
    std::cout << (isValid? "True" : "False");
};

int main() {
    std::string sentence;
    std::getline(std::cin, sentence);
    solution(sentence);
}