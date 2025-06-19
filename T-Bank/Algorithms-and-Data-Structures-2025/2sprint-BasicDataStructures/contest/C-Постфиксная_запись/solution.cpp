#include <iostream>
#include <vector>
#include <string>

using namespace std;


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    vector<int> stack;
    string simbol;
    while (cin >> simbol) {
        if (simbol == "+" || simbol == "-" || simbol == "*" || simbol == "/") {
            int x, y;
            y = stack.back();
            stack.pop_back();
            x = stack.back();
            stack.pop_back();
            stack.push_back(
                (simbol == "+"? x + y : simbol == "-"? x - y : simbol == "*"? x * y : x / y)
            );
        } else stack.push_back(stoi(simbol));
    }
    printf("%d\n", stack.back());  
}


int main() {
    solution();
}