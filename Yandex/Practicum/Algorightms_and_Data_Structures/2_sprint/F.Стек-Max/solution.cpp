#include <iostream>
#include <string>
#include <vector>

class Stack {
private:
    std::vector<int> stack;
    std::vector<int> maxStack;
public:
    Stack() {};
    void getMax() {
        if (stack.size()) {
            std::cout << maxStack[maxStack.size() - 1] << "\n";
            return;
        }
        std::cout << "None\n";
    }
    void push(int x) {
        maxStack.push_back((stack.size()? std::max(x, maxStack[maxStack.size() - 1]) : x));
        stack.push_back(x);
    }
    void pop() {
        if (stack.size()) {
            maxStack.pop_back();
            stack.pop_back();
            return;
        }
        std::cout << "error\n";
    }
};
void solution(int t) {
    /*
    Time Complexity O(1)
    Memory Complexity O(N)
    */
    Stack stack = Stack();
    for (int i = 0; i < t; ++i) {
        std::string method;
        std::cin >> method;
        if (method == "get_max") {
            stack.getMax();
        } else if (method == "push") {
            int num;
            std::cin >> num;
            stack.push(num);
        } else {
            stack.pop();
        }
    }
}


int main() {
    int t;
    std::cin >> t;
    solution(t);
}