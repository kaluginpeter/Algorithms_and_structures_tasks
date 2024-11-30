#include <iostream>
#include <string>


void backtracking(int n, std::string& currentSequence, int openBrackets, int closeBrackets) {
    if (openBrackets + closeBrackets == n) {
        std::cout << currentSequence << "\n";
        return;
    }
    if (openBrackets < n / 2) {
        currentSequence += '(';
        ++openBrackets;
        backtracking(n, currentSequence, openBrackets, closeBrackets);
        --openBrackets;
        currentSequence.pop_back();
    }
    if (closeBrackets < openBrackets) {
        currentSequence += ')';
        ++closeBrackets;
        backtracking(n, currentSequence, openBrackets, closeBrackets);
        --closeBrackets;
        currentSequence.pop_back();
    }
}


void solution(int n) {
    /*
    Time Complexity O(4**N / N**(3 / 2))
    Memory Complexity O(N)
    */
    std::string currentSequence = "";
    backtracking(n * 2, currentSequence, 0, 0);
}


int main() {
    int n;
    std::cin >> n;
    solution(n);
}