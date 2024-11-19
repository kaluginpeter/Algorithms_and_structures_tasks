#ifdef REMOTE_JUDGE
#include "solution.h"
#endif

#ifndef REMOTE_JUDGE
#include <cassert>
#include <string>

struct Node {
    std::string value;
    Node* next;
    Node(const std::string &value, Node* next) : value(value), next(next) {

    }
};
#endif


int solution(Node* head, const std::string& elem) {
    /*
    Time Complexity O(N)
    Memory Complexity O(1)
    */
    int idx = 0;
    while (head) {
        if (head->value == elem) {
            return idx;
        }
        ++idx;
        head = head->next;
    }
    return -1;
}

#ifndef REMOTE_JUDGE
void test() {
    Node node3("node3", nullptr);
    Node node2("node2", &node3);
    Node node1("node1", &node2);
    Node node0("node0", &node1);
    int idx = solution(&node0, "node2");
    assert(idx == 2);
}

int main() {
    test();
}
#endif