#include <iostream>
#include <vector>


class MaxHeap {
private:
    std::vector<int> arr;
public:
    MaxHeap() {
        arr.push_back(0);
    };
    
    void insert(int x) {
        arr.push_back(x);
        int xIdx = arr.size() - 1;
        while (xIdx > 1) {
            int parentIdx = xIdx >> 1;
            if (arr[xIdx] <= arr[parentIdx]) break;
            std::swap(arr[xIdx], arr[parentIdx]);
            xIdx = parentIdx;
        }
    };
    
    int extract() {
        int lastIdx = arr.size() - 1;
        std::swap(arr[1], arr[lastIdx]);
        int outputValue = arr.back();
        arr.pop_back();
        int upperBound = lastIdx - 1;
        int topIdx = 1;
        while (true) {
            int leftChildIdx = topIdx << 1;
            int rightChildIdx = leftChildIdx + 1;
            if (leftChildIdx > upperBound) break;
            int childIdx = leftChildIdx;
            if (rightChildIdx <= upperBound && arr[rightChildIdx] > arr[childIdx]) {
                childIdx = rightChildIdx;
            }
            if (arr[topIdx] >= arr[childIdx]) break;
            std::swap(arr[topIdx], arr[childIdx]);
            topIdx = childIdx;
        }
        return outputValue;
        
    }
};


void solution() {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    */
    int n;
    std::scanf("%d", &n);
    MaxHeap maxHeap;
    for (int i = 0; i < n; ++i) {
        int command;
        std::scanf("%d", &command);
        if (command == 0) {
            int x;
            std::scanf("%d", &x);
            maxHeap.insert(x);
        } else std::printf("%d\n", maxHeap.extract());
    }
}


int main() {
    solution();
}