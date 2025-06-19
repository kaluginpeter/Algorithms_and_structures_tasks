#include <iostream>
#include <vector>

using namespace std;

class Stack {
private:
    vector<int> stack;
    vector<int> minStack;
public:
    Stack() {};
    
    void push(int x) {
        if (stack.empty()) {
            stack.push_back(x);
            minStack.push_back(x);
        } else {
            stack.push_back(x);
            minStack.push_back(min(minStack.back(), x));
        }
    }
    
    void pop() {
        stack.pop_back();
        minStack.pop_back();
    }
    
    int getMin() {
        return minStack.back();
    }
};


void solution() {
    /*
    Time Complexity O(1) for operations
    Memory Complexity O(N) for storage
    */
    Stack stack = Stack();
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        int operation;
        cin >> operation;
        if (operation == 1) {
            int x;
            cin >> x;
            stack.push(x);
        } else if (operation == 2) stack.pop();
        else printf("%d\n", stack.getMin());
    }
}


int main() {
    solution();
}