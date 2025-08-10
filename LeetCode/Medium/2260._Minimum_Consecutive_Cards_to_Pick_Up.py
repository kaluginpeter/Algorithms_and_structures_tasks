# You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.
#
# Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.
#
#
#
# Example 1:
#
# Input: cards = [3,4,2,3,4,7]
# Output: 4
# Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.
# Example 2:
#
# Input: cards = [1,0,5,3]
# Output: -1
# Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.
#
#
# Constraints:
#
# 1 <= cards.length <= 105
# 0 <= cards[i] <= 106
# Solution
# Python O(N) O(D) HashMap SlidingWindow
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hashmap: list[int] = [-1] * (10**6 + 1)
        output: int = -1
        for right in range(len(cards)):
            if hashmap[cards[right]] != -1:
                if output == -1 or (right - hashmap[cards[right]] + 1 < output):
                    output = right - hashmap[cards[right]] + 1
            hashmap[cards[right]] = right
        return output

# C++ O(N) O(D) HashMap SlidingWindow
class Solution {
public:
    int minimumCardPickup(vector<int>& cards) {
        std::vector<int> hashmap(1e6 + 1, -1);
        int output = -1;
        for (int right = 0; right < cards.size(); ++right) {
            if (hashmap[cards[right]] != -1) {
                if (output == -1 || (right - hashmap[cards[right]] + 1 < output)) {
                    output = right - hashmap[cards[right]] + 1;
                }
            }
            hashmap[cards[right]] = right;
        }
        return output;
    }
};