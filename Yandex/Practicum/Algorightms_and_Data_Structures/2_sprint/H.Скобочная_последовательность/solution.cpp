#include <iostream>
#include <string>
#include <unordered_map>
#include <stack>

void solution(std::string& braces) {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    std::stack<char> stack;
    bool isValid = true;
    std::unordered_map<char, char> validOpenBraces = {
        {')', '('}, {']', '['}, {'}', '{'}
    };
    for (char brace : braces) {
        if (brace == '(' || brace == '[' || brace == '{') {
            stack.push(brace);
        } else {
            if (!stack.size() || stack.top() != validOpenBraces[brace]) {
                isValid = false;
                break;
            }
            stack.pop();
        }
    }
    std::cout << (isValid && !stack.size()? "True" : "False") << "\n";
}

int main() {
    std::string braces;
    std::cin >> braces;
    solution(braces);
}