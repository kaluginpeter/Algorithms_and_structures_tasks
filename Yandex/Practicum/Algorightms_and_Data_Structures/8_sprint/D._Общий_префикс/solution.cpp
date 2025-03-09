#include <iostream>
#include <string>


void solution() {
    /*
    Time Complexity O(L)
    Memory Complexity O(M)
    */
    int n;
    std::scanf("%d", &n);
    std::string pattern;
    int pN = 0;
    for (int i = 0; i < n; ++i) {
        std::string word;
        std::cin >> word;
        if (!i) {
            pattern = word;
            pN = pattern.size();
        }
        else {
            int idx = 0;
            while (idx < std::min(pN, (int)word.size())) {
                if (pattern[idx] == word[idx]) ++idx;
                else break;
            }
            pN = idx;
        }
    }
    std::cout << pN << "\n";
}


int main() {
    solution();
}