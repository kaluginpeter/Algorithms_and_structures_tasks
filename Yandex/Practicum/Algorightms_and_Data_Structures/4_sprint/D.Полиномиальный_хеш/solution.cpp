#include <iostream>
#include <string>


void solution(int& q, int& m, std::string& s) {
    /*
    Time Complexity O(s)
    Memory Complexity O(1)
    */
    long long h = 0;
    for (int idx = 0; idx < s.size(); ++idx) {
        char ch = s[idx];
        h += (int)ch % m;
        if (idx != s.size() - 1) {
            h = (h % m * q % m) % m;
        }
    }
    std::cout << h % m << "\n";
}


int main() {
    int a, m;
    std::cin >> a >> m;
    std::string s;
    std::cin >> s;
    solution(a, m, s);
}