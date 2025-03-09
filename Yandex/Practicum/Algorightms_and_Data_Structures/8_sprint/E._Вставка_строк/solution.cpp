#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>


void solution() {
    /*
    Time Complexity O(N + M)
    Memory Complexity O(M)
    */
    std::string s;
    std::cin >> s;
    int n;
    std::scanf("%d", &n);
    std::unordered_map<int, std::string> gifts;
    for (int i = 0; i < n; ++i) {
        std::string t;
        std::cin >> t;
        int k;
        std::scanf("%d", &k);
        gifts[k] = t;
    }

    for (int i = 0; i < s.size(); ++i) {
        if (gifts.count(i)) std::cout << gifts[i];
        std::cout << s[i];
    }
    if (gifts.count(s.size())) {
        std::cout << gifts[s.size()];
    }
    std::cout << "\n";
}


int main() {
    solution();
}