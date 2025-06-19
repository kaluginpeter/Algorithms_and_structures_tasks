#include <iostream>
#include <string>
#include <deque>

using namespace std;

void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    int n;
    scanf("%d", &n);
    deque<int> queue;
    deque<int> output;
    int totalSize = 0;
    for (int i = 0; i < n; ++i) {
        string event;
        cin >> event;
        if (event == "-") {
            --totalSize;
            if (!output.empty()) {
                printf("%d\n", output.front());
                output.pop_front();
            } else {
                printf("%d\n", queue.front());
                queue.pop_front();
            }
            continue;
        }
        int goblinId;
        scanf("%d", &goblinId);
        if (event == "+") {
            queue.push_back(goblinId);
        } else {
            int place = totalSize / 2;
            if (totalSize % 2 != 0) ++place;
            place -= output.size();
            for (int idx = 0; idx < place; ++idx) {
                output.push_back(queue.front());
                queue.pop_front();
            }
            queue.push_front(goblinId);
        }
        ++totalSize;
    }
}


int main() {
    solution();
}