#include <iostream>
#include <string>
#include <unordered_map>


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(K), where K is length of distinct characters
    */
    std::string sentence;
    std::cin >> sentence;
    std::unordered_map<char, int> hashmap;
    int maxSub = 0;
    int left = 0;
    for (int right = 0; right < sentence.size(); ++right) {
        ++hashmap[sentence[right]];
        if (hashmap.size() != right - left + 1) {
            --hashmap[sentence[left]];
            if (!hashmap[sentence[left]]) {
                hashmap.erase(sentence[left]);
            }
            ++left;
        }
        maxSub = std::max(maxSub, right - left + 1);
    }
    std::cout << maxSub << "\n";
}


int main() {
    solution();
}