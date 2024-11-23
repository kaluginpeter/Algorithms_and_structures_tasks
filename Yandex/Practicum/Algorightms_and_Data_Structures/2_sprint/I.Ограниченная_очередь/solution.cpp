#include <iostream>
#include <vector>
#include <string>

class MySizedQueue {
private:
    std::vector<int> queue;
    int head = 0;
    int tail = 0;
    int size_ = 0;
    int capacity = 0;
public:
    MySizedQueue(int n) {
        queue.resize(n, 0);
        capacity = n;
    };
    void push(int x) {
        if (size_ == capacity) {
            std::cout << "error\n";
            return;
        }
        queue[tail] = x;
        tail = (tail + 1) % capacity;
        ++size_;
    }
    void pop() {
        if (!size_) {
            std::cout << "None\n";
            return;
        }
        std::cout << queue[head] << "\n";
        queue[head] = 0;
        head = (head + 1) % capacity;
        --size_;
    }
    void peek() {
        if (!size_) {
            std::cout << "None\n";
            return;
        }
        std::cout << queue[head] << "\n";
    }
    void size() {
        std::cout << size_ << "\n";
    }
};


void solution(int t) {
    /*
    Time Complexity O(N) for building queue and O(1) for each operation
    Memory Complexity O(N)
    */
    int n;
    std::cin >> n;
    MySizedQueue queue = MySizedQueue(n);
    for (int i = 0; i < t; ++i) {
        std::string command;
        std::cin >> command;
        if (command == "push") {
            int num;
            std::cin >> num;
            queue.push(num);
        } else if (command == "pop") {
            queue.pop();
        } else if (command == "peek") {
            queue.peek();
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