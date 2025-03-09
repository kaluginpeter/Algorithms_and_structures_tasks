#include <iostream>
#include <string>
#include <unordered_map>


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(D)
    */
    int n;
    std::scanf("%d", &n);
    std::unordered_map<std::string, int> gistogram;
    int maxFreq = 0;
    std::string maxFreqWord = "";
    for (int i = 0; i < n; ++i) {
        std::string word;
        std::cin >> word;
        ++gistogram[word];
        if (gistogram[word] > maxFreq) {
            maxFreq = gistogram[word];
            maxFreqWord = word;
        } else if (gistogram[word] == maxFreq && word < maxFreqWord) {
            maxFreqWord = word;
        }
    }
    std::cout << maxFreqWord << "\n";
}


int main() {
    solution();
}