# There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.
#
# The operation of drinking a full water bottle turns it into an empty bottle.
#
# Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.
#
#
#
# Example 1:
#
#
# Input: numBottles = 9, numExchange = 3
# Output: 13
# Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
# Number of water bottles you can drink: 9 + 3 + 1 = 13.
# Example 2:
#
#
# Input: numBottles = 15, numExchange = 4
# Output: 19
# Explanation: You can exchange 4 empty bottles to get 1 full water bottle.
# Number of water bottles you can drink: 15 + 3 + 1 = 19.
#
#
# Constraints:
#
# 1 <= numBottles <= 100
# 2 <= numExchange <= 100
# Solution Math Simulation O(log(N)) O(1)
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        bottles: int = numBottles
        empty_bottles: int = numBottles
        while empty_bottles >= numExchange:
            can_get: int = empty_bottles // numExchange
            bottles += can_get
            empty_bottles = empty_bottles % numExchange + can_get
        return bottles


# Python O(logN) O(1) Simulation Math
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        output: int = 0
        empty: int = 0
        while numBottles > 0 or empty >= numExchange:
            output += numBottles
            new_empty: int = numBottles + empty % numExchange
            numBottles = empty // numExchange
            empty = new_empty
        return output

# C++ O(logN) O(1) Simulation Math
class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int output = 0, empty = 0;
        while (numBottles > 0 || empty >= numExchange) {
            output += numBottles;
            int newEmpty = numBottles + empty % numExchange;
            numBottles = empty / numExchange;
            empty = newEmpty;
        }
        return output;
    }
};