#include <iostream>
#include <string>


void solution(std::string& a, std::string& b) {
    /*
    Time Complexity O(N)
    Memory Complexity O(1)
    */
    bool isValid = true;
    int aLeft = 0, bLeft = 0;
    int aRight = 0, bRight = 0;
    while (aRight < a.size() && bRight < b.size()) {
        while (aRight < a.size() && a[aLeft] == a[aRight]) {
            ++aRight;
        }
        while (bRight < b.size() && b[bLeft] == b[bRight]) {
            ++bRight;
        }
        if (aRight - aLeft != bRight - bLeft) {
            isValid = false;
            break;
        } else {
            aLeft = aRight;
            bLeft = bRight;
        }
    }
    std::cout << (isValid && aRight == a.size() && bRight == b.size()? "YES" : "NO") << "\n";
}


int main() {
    std::string a, b;
    std::cin >> a >> b;
    solution(a, b);
}