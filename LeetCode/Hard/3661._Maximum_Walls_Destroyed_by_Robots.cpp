/*
There is an endless straight line populated with some robots and walls. You are given integer arrays robots, distance, and walls:
robots[i] is the position of the ith robot.
distance[i] is the maximum distance the ith robot's bullet can travel.
walls[j] is the position of the jth wall.
Every robot has one bullet that can either fire to the left or the right at most distance[i] meters.

A bullet destroys every wall in its path that lies within its range. Robots are fixed obstacles: if a bullet hits another robot before reaching a wall, it immediately stops at that robot and cannot continue.

Return the maximum number of unique walls that can be destroyed by the robots.

Notes:

A wall and a robot may share the same position; the wall can be destroyed by the robot at that position.
Robots are not destroyed by bullets.


Example 1:

Input: robots = [4], distance = [3], walls = [1,10]

Output: 1

Explanation:

robots[0] = 4 fires left with distance[0] = 3, covering [1, 4] and destroys walls[0] = 1.
Thus, the answer is 1.
Example 2:

Input: robots = [10,2], distance = [5,1], walls = [5,2,7]

Output: 3

Explanation:

robots[0] = 10 fires left with distance[0] = 5, covering [5, 10] and destroys walls[0] = 5 and walls[2] = 7.
robots[1] = 2 fires left with distance[1] = 1, covering [1, 2] and destroys walls[1] = 2.
Thus, the answer is 3.
Example 3:
Input: robots = [1,2], distance = [100,1], walls = [10]

Output: 0

Explanation:

In this example, only robots[0] can reach the wall, but its shot to the right is blocked by robots[1]; thus the answer is 0.



Constraints:

1 <= robots.length == distance.length <= 105
1 <= walls.length <= 105
1 <= robots[i], walls[j] <= 109
1 <= distance[i] <= 105
All values in robots are unique
All values in walls are unique
*/
// Solution
// C++ O(NlogN + MlogM) O(N + logM) TwoPointers DynamicProgramming
class Solution {
public:
    int maxWalls(vector<int>& robots, vector<int>& distance, vector<int>& walls) {
        size_t n = robots.size(), m = walls.size();
        std::vector<std::pair<int, int>> robotDist;
        for (int i = 0; i < n; ++i) robotDist.push_back({robots[i], distance[i]});
        std::sort(robotDist.begin(), robotDist.end());
        std::sort(walls.begin(), walls.end());
        int rightPtr = 0, leftPtr = 0, curPtr = 0, robotPtr = 0;
        int prevLeft = 0, prevRight = 0, prevNum = 0;
        int subLeft = 0, subRight = 0;

        for (int i = 0; i < n; ++i) {
            int robotPos = robotDist[i].first;
            int robotDistVal = robotDist[i].second;
            while (rightPtr < m && walls[rightPtr] <= robotPos) ++rightPtr;
            int pos1 = rightPtr;
            while (curPtr < m && walls[curPtr] < robotPos) ++curPtr;
            int pos2 = curPtr;
            int leftBound = (i >= 1) ? std::max(robotPos - robotDistVal, robotDist[i - 1].first + 1) : robotPos - robotDistVal;
            while (leftPtr < m && walls[leftPtr] < leftBound) ++leftPtr;
            int leftPos = leftPtr;
            int currentLeft = pos1 - leftPos;
            int rightBound = (i < n - 1) ? std::min(robotPos + robotDistVal, robotDist[i + 1].first - 1) : robotPos + robotDistVal;
            while (rightPtr < m && walls[rightPtr] <= rightBound) ++rightPtr;
            int rightPos = rightPtr;
            int currentRight = rightPos - pos2;
            int currentNum = 0;
            if (i > 0) {
                while (robotPtr < m && walls[robotPtr] < robotDist[i - 1].first) ++robotPtr;
                int pos3 = robotPtr;
                currentNum = pos1 - pos3;
            }
            if (i == 0) {
                subLeft = currentLeft;
                subRight = currentRight;
            } else {
                int newsubLeft =
                    std::max(subLeft + currentLeft, subRight - prevRight +
                            std::min(currentLeft + prevRight, currentNum));
                int newsubRight = std::max(subLeft + currentRight, subRight + currentRight);
                subLeft = newsubLeft;
                subRight = newsubRight;
            }
            prevLeft = currentLeft;
            prevRight = currentRight;
            prevNum = currentNum;
        }
        return std::max(subLeft, subRight);
    }
};