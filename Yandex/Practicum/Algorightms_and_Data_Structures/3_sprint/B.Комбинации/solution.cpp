#include <iostream>
#include <string>
#include <unordered_map>


std::unordered_map<char, std::string> keyboard {
    {'2', "abc"}, {'3', "def"}, {'4', "ghi"},
    {'5', "jkl"}, {'6', "mno"}, {'7', "pqrs"},
    {'8', "tuv"}, {'9', "wxyz"}
};


bool printedFirstTime = false;


void backtracking(int index, std::string& buttons, std::string& typing) {
    int n = buttons.size();
    if (index == n) {
        if (printedFirstTime) {
            std::cout << " ";
        }
        std::cout << typing;
        printedFirstTime = true;
    }
    char button = buttons[index];
    for (char key : keyboard[button]) {
        typing += key;
        backtracking(index + 1, buttons, typing);
        typing.pop_back();
    }
}


void solution(std::string& buttons) {
    /*
    Time Complexity O(N**K), where N is length of buttons and K is number of keyboards
    Memory Complexity O(N)
    */
    printedFirstTime = false;
    std::string typing = "";
    backtracking(0, buttons, typing);
}


int main() {
    std::string buttons;
    std::cin >> buttons;
    solution(buttons);
}