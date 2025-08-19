# For a stream of integers, implement a data structure that checks if the last k integers parsed in the stream are equal to value.
#
# Implement the DataStream class:
#
# DataStream(int value, int k) Initializes the object with an empty integer stream and the two integers value and k.
# boolean consec(int num) Adds num to the stream of integers. Returns true if the last k integers are equal to value, and false otherwise. If there are less than k integers, the condition does not hold true, so returns false.
#
#
# Example 1:
#
# Input
# ["DataStream", "consec", "consec", "consec", "consec"]
# [[4, 3], [4], [4], [4], [3]]
# Output
# [null, false, false, true, false]
#
# Explanation
# DataStream dataStream = new DataStream(4, 3); //value = 4, k = 3
# dataStream.consec(4); // Only 1 integer is parsed, so returns False.
# dataStream.consec(4); // Only 2 integers are parsed.
#                       // Since 2 is less than k, returns False.
# dataStream.consec(4); // The 3 integers parsed are all equal to value, so returns True.
# dataStream.consec(3); // The last k integers parsed in the stream are [4,4,3].
#                       // Since 3 is not equal to value, it returns False.
#
#
# Constraints:
#
# 1 <= value, num <= 109
# 1 <= k <= 105
# At most 105 calls will be made to consec.
# Solution
# Python O(1) O(1) Design TwoPointers
class DataStream:

    def __init__(self, value: int, k: int):
        self.size: int = 0
        self.window_size: int = k
        self.target: int = value

    def consec(self, num: int) -> bool:
        if num != self.target: self.size = 0
        else: self.size += 1
        return self.size >= self.window_size


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)

# C++ O(1) O(1) Design TwoPointers
class DataStream {
private:
    unsigned int size = 0;
    int target, windowSize;
public:
    DataStream(int value, int k) {
        this->target = value;
        this->windowSize = k;
    }

    bool consec(int num) {
        if (num != target) this->size = 0;
        else ++this->size;
        return this->size >= windowSize;
    }
};

/**
 * Your DataStream object will be instantiated and called as such:
 * DataStream* obj = new DataStream(value, k);
 * bool param_1 = obj->consec(num);
 */