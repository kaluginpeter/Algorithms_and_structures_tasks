# Design a stack that supports increment operations on its elements.
#
# Implement the CustomStack class:
#
# CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
# void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
# int pop() Pops and returns the top of the stack or -1 if the stack is empty.
# void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, increment all the elements in the stack.
#
#
# Example 1:
#
# Input
# ["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
# [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
# Output
# [null,null,null,2,null,null,null,null,null,103,202,201,-1]
# Explanation
# CustomStack stk = new CustomStack(3); // Stack is Empty []
# stk.push(1);                          // stack becomes [1]
# stk.push(2);                          // stack becomes [1, 2]
# stk.pop();                            // return 2 --> Return top of the stack 2, stack becomes [1]
# stk.push(2);                          // stack becomes [1, 2]
# stk.push(3);                          // stack becomes [1, 2, 3]
# stk.push(4);                          // stack still [1, 2, 3], Do not add another elements as size is 4
# stk.increment(5, 100);                // stack becomes [101, 102, 103]
# stk.increment(2, 100);                // stack becomes [201, 202, 103]
# stk.pop();                            // return 103 --> Return top of the stack 103, stack becomes [201, 202]
# stk.pop();                            // return 202 --> Return top of the stack 202, stack becomes [201]
# stk.pop();                            // return 201 --> Return top of the stack 201, stack becomes []
# stk.pop();                            // return -1 --> Stack is empty return -1.
#
#
# Constraints:
#
# 1 <= maxSize, x, k <= 1000
# 0 <= val <= 100
# At most 1000 calls will be made to each method of increment, push and pop each separately.
# Solution Time complexity: push = O(1); pop = O(1); increment = O(min(k, N)). Memory Complexity: O(N)
class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size: int = maxSize
        self.capacity: int = 0
        self.stack: list[int] = [0] * self.max_size

    def push(self, x: int) -> None:
        if self.capacity < self.max_size:
            self.stack[self.capacity] = x
            self.capacity += 1

    def pop(self) -> int:
        if self.capacity > 0:
            self.capacity -= 1
            x: int = self.stack[self.capacity]
            self.stack[self.capacity] = 0
            return x
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(self.capacity, k)):
            self.stack[i] += val

# C++ O(1) for all operation O(N)
class CustomStack {
public:
    std::vector<int> stack;
    std::vector<int> increase;
    int global_index = -1;
    CustomStack(int maxSize) {
        stack.resize(maxSize);
        increase.resize(maxSize);
    }

    void push(int x) {
        if (global_index + 1 == stack.size()) {
            return;
        };
        global_index += 1;
        stack[global_index] = x;
    }

    int pop() {
        if (global_index < 0) {
            return -1;
        };
        int output = stack[global_index] + increase[global_index];
        if (global_index > 0) {
            increase[global_index - 1] += increase[global_index];
        };
        increase[global_index] = 0;
        global_index -= 1;
        return output;
    }

    void increment(int k, int val) {
        if (global_index < 0) {
            return;
        };
        increase[std::min(global_index, k - 1)] += val;
    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */

# Python O(1) for all operation O(N)
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack: list[int] = [0] * maxSize
        self.capacity: int = maxSize
        self.increase: list[int] = [0] * maxSize
        self.global_index: int = -1

    def push(self, x: int) -> None:
        if self.global_index + 1 == len(self.stack): return
        self.global_index += 1
        self.stack[self.global_index] = x

    def pop(self) -> int:
        if self.global_index < 0: return -1
        output: int = self.stack[self.global_index] + self.increase[self.global_index]
        if self.global_index > 0:
            self.increase[self.global_index - 1] += self.increase[self.global_index]
        self.increase[self.global_index] = 0
        self.global_index -= 1
        return output

    def increment(self, k: int, val: int) -> None:
        if self.global_index < 0: return
        self.increase[min(self.global_index, k - 1)] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)