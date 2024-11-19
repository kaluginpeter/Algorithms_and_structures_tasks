#include <iostream>
#include <vector>
#include <string>

class Node {
public:
    int value;
    Node* next = nullptr;
    Node* prev = nullptr;
    Node (int value = 0, Node* next = nullptr, Node* prev = nullptr) {
        this->value = value;
        this->next = next;
        this->prev = prev;
    };
};

class Stack {
private:
    Node* head;
    Node* tail;
    Node* maxHead;
    Node* maxTail;
    int size = 0;
public:
    Stack () {
        head = new Node();
        tail = head;
        maxHead = new Node();
        maxTail = maxHead;
    };
    void push(int x) {
        ++size;
        if (size == 1) {
            head->next = new Node(x);
            tail = head->next;
            tail->prev = head;
            maxHead->next = new Node(x);
            maxTail = maxHead->next;
            maxTail->prev = maxHead;
            return;
        }
        tail->next = new Node(x);
        tail->next->prev = tail;
        tail = tail->next;
        maxTail->next = new Node(std::max(x, maxTail->value));
        maxTail->next->prev = maxTail;
        maxTail = maxTail->next;
    }
    void pop() {
        if (!size) {
            std::cout << "error\n";
            return;
        }
        --size;
        tail = tail->prev;
        maxTail = maxTail->prev;
    }
    void get_max() {
        if (!size) {
            std::cout << "None\n";
            return;
        }
        std::cout << maxTail->value << "\n";
    }
    void top() {
        if (!size) {
            std::cout << "error\n";
            return;
        }
        std::cout << tail->value << "\n";
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
            stack.get_max();
        } else if (method == "top") {
            stack.top();
        } else if (method == "pop") {
            stack.pop();
        } else {
            int num;
            std::cin >> num;
            stack.push(num);
        }
    }
}

int main() {
    int t;
    std::cin >> t;
    solution(t);
}