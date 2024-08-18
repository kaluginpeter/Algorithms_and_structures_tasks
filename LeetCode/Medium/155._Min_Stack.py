# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
#
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.
#
#
#
# Example 1:
#
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# Output
# [null,null,null,null,-3,null,0,-2]
#
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
#
#
# Constraints:
#
# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.
# Complexity
# Time complexity: All opertaions is O(1), but technically .pop() can made up to O(N) when we delete min element in a stack
#
# Space complexity: O(N)
#
# Code
class MinStack:

    def __init__(self):
        self.stack: list = list()
        self.mn_val: int = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mn_val = min(val, self.mn_val)

    def pop(self) -> None:
        x: int = self.stack.pop()
        if x == self.mn_val:
            self.mn_val = float('inf')
            for i in self.stack:
                self.mn_val = min(self.mn_val, i)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mn_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# Complexity
# Time complexity: All opertaions is O(1)
#
# Space complexity: O(N), but in solution above we use 2x small memory space
#
# Code
class MinStack:

    def __init__(self):
        self.stack: list = list()

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][-1])))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][-1]