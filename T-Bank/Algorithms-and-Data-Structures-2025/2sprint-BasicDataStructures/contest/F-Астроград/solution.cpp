#include <iostream>
#include <deque>
#include <unordered_map>

using namespace std;


void solution() {
    /*
    Time Complexity O(1) for each operation
    Memory Complexity O(N)
    */
    int n;
    scanf("%d", &n);
    deque<int> queue;
    unordered_map<int, pair<int, int>> hashmap;
    int leaved = 0;
    for (int i = 0; i < n; ++i) {
        int event;
        scanf("%d", &event);
        if (event == 1) {
            int manId;
            scanf("%d", &manId);
            queue.push_back(manId);
            hashmap[manId] = {queue.size(), leaved};
        } else if (event == 2) {
            hashmap.erase(queue.front());
            queue.pop_front();
            ++leaved;
        } else if (event == 3) {
            hashmap.erase(queue.back());
            queue.pop_back();
        } else if (event == 4) {
            int q;
            scanf("%d", &q);
            printf("%d\n", hashmap[q].first - (leaved - hashmap[q].second) - 1);
        } else {
            printf("%d\n", queue.front());
        }
    }
}

int main() {
    solution();
}