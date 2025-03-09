#include <iostream>
#include <vector>
#include <string>


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(1)
    */
    std::vector<std::string> words;
    std::string word = "";
    while (std::cin >> word) {
        words.push_back(word);
    }
    int left = 0;
    int right = words.size() - 1;
    while (left < right) {
        std::swap(words[left], words[right]);
        ++left;
        --right;
    }
    for (size_t i = 0; i < words.size(); ++i) {
        if (i) std::printf(" ");
        std::cout << words[i];
    }
    std::printf("\n");
}


int main() {
    solution();
}