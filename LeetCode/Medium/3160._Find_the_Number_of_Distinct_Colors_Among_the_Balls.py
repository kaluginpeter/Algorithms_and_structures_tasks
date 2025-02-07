# You are given an integer limit and a 2D array queries of size n x 2.
#
# There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored. For every query in queries that is of the form [x, y], you mark ball x with the color y. After each query, you need to find the number of distinct colors among the balls.
#
# Return an array result of length n, where result[i] denotes the number of distinct colors after ith query.
#
# Note that when answering a query, lack of a color will not be considered as a color.
#
#
#
# Example 1:
#
# Input: limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]
#
# Output: [1,2,2,3]
#
# Explanation:
#
#
#
# After query 0, ball 1 has color 4.
# After query 1, ball 1 has color 4, and ball 2 has color 5.
# After query 2, ball 1 has color 3, and ball 2 has color 5.
# After query 3, ball 1 has color 3, ball 2 has color 5, and ball 3 has color 4.
# Example 2:
#
# Input: limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]
#
# Output: [1,2,2,3,4]
#
# Explanation:
#
#
#
# After query 0, ball 0 has color 1.
# After query 1, ball 0 has color 1, and ball 1 has color 2.
# After query 2, ball 0 has color 1, and balls 1 and 2 have color 2.
# After query 3, ball 0 has color 1, balls 1 and 2 have color 2, and ball 3 has color 4.
# After query 4, ball 0 has color 1, balls 1 and 2 have color 2, ball 3 has color 4, and ball 4 has color 5.
#
#
# Constraints:
#
# 1 <= limit <= 109
# 1 <= n == queries.length <= 105
# queries[i].length == 2
# 0 <= queries[i][0] <= limit
# 1 <= queries[i][1] <= 109
# Solution HashTable O(N) O(N)
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls: dict[int, int] = dict() # HashBalls from description
        colors: dict[int, int] = dict() # HashColors from description
        output: list[int] = list() # our list of answers
        count: int = 0 # total count of unique colors
        for i in queries: # iterate from queries and get each query
            x, y = i # x - representing ball, y - representing color
            if x in balls: # if x already exist(first condition)
                if colors[balls[x]] == 1: count -= 1 # if existing ball have unique color
                colors[balls[x]] = max(0, colors[balls[x]] - 1) # delete old color from HashColors
                balls[x] = y # Set new color to existing ball
                colors[y] = colors.get(y, 0) + 1 # increment frequences of given color
                if colors[y] == 1: count += 1 # if value is 1(it means that we got uniuqe color)
            else: # If we got new ball(second condition)
                balls[x] = y # Set new ball in HashBalls
                colors[y] = colors.get(y, 0) + 1 # Increment frequences of given color
                if colors[y] == 1: count += 1 # if value is 1(it means that we got unique color) so just increment count
            output.append(count) # append to the answer list given count of unique colors
        return output


# Python O(N) O(N) HashMap
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        hashmap: dict[int, int] = dict()
        have_color: dict[int, int] = dict()
        output: list[int] = []
        for ball, color in queries:
            if ball in have_color:
                hashmap[have_color[ball]] -= 1
                if not hashmap[have_color[ball]]:
                    del hashmap[have_color[ball]]
            hashmap[color] = hashmap.get(color, 0) + 1
            have_color[ball] = color
            output.append(len(hashmap))
        return output

# C++ O(N) O(N) HashMap
class Solution {
public:
    vector<int> queryResults(int limit, vector<vector<int>>& queries) {
        std::unordered_map<int, int> hashmap;
        std::unordered_map<int, int> haveColor;
        std::vector<int> output;
        for (std::vector<int>& query : queries) {
            int ball = query[0], color = query[1];
            if (haveColor.count(ball)) {
                --hashmap[haveColor[ball]];
                if (!hashmap[haveColor[ball]]) {
                    hashmap.erase(haveColor[ball]);
                    }
            }
            ++hashmap[color];
            haveColor[ball] = color;
            output.push_back(hashmap.size());

        }
        return output;
    }
};