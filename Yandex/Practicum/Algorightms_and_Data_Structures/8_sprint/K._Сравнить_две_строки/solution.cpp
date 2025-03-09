#include <iostream>
#include <string>


void solution() {
    /*
    Time Complexity O(N + M)
    Memory Complexity O(N + M)
    */
    std::string a, b;
    std::cin >> a >> b;
    std::string aEven = "";
    std::string bEven = "";
    for (char& letter : a) {
        if ((letter - 'a') & 1) aEven.push_back(letter);
    }
    for (char& letter : b) {
        if ((letter - 'a') & 1) bEven.push_back(letter);
    }
    if (aEven == bEven) std::printf("0\n");
    else std::cout << (aEven < bEven? "-1" : "1") << "\n";

}


int main() {
    solution();
}