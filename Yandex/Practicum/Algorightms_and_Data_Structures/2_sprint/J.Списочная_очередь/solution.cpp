#include <iostream>
#include <string>

class QueueNode {
public:
    int value;
    QueueNode* next = nullptr;
    QueueNode (int x) {
        value = x;
    };
};

class Queue {
private:
    QueueNode* head = nullptr;
    QueueNode* tail = nullptr;
    int size_ = 0;
public:
    Queue() {};
    void get() {
        if (!size_) {
            std::cout << "error\n";
            return;
        }
        std::cout << head->value << "\n";
        head = head->next;
        --size_;
    }
    void put (int x) {
        ++size_;
        if (size_ == 1) {
            head = new QueueNode(x);
            tail = head;
            return;
        }
        tail->next = new QueueNode(x);
        tail = tail->next;
    }
    void size() {
        std:: cout << size_ << "\n";
    }
};

void solution(int t) {
    /*
    Time Complexity O(1)
    Memory Complexity O(N) for store N items
    */
    Queue queue = Queue();
    for (int i = 0; i < t; ++i) {
        std::string command;
        std::cin >> command;
        if (command == "get") {
            queue.get();
        } else if (command == "put") {
            int num;
            std::cin >> num;
            queue.put(num);
        } else {
            queue.size();
        }
    }
}

int main() {
    int t;
    std::cin >> t;
    solution(t);
}