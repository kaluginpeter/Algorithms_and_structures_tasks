# There are n 1-indexed robots, each having a position on a line, health, and movement direction.
#
# You are given 0-indexed integer arrays positions, healths, and a string directions (directions[i] is either 'L' for left or 'R' for right). All integers in positions are unique.
#
# All robots start moving on the line simultaneously at the same speed in their given directions. If two robots ever share the same position while moving, they will collide.
#
# If two robots collide, the robot with lower health is removed from the line, and the health of the other robot decreases by one. The surviving robot continues in the same direction it was going. If both robots have the same health, they are both removed from the line.
#
# Your task is to determine the health of the robots that survive the collisions, in the same order that the robots were given, i.e. final heath of robot 1 (if survived), final health of robot 2 (if survived), and so on. If there are no survivors, return an empty array.
#
# Return an array containing the health of the remaining robots (in the order they were given in the input), after no further collisions can occur.
#
# Note: The positions may be unsorted.
#
#
#
#
# Example 1:
#
#
#
# Input: positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR"
# Output: [2,17,9,15,10]
# Explanation: No collision occurs in this example, since all robots are moving in the same direction. So, the health of the robots in order from the first robot is returned, [2, 17, 9, 15, 10].
# Example 2:
#
#
#
# Input: positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL"
# Output: [14]
# Explanation: There are 2 collisions in this example. Firstly, robot 1 and robot 2 will collide, and since both have the same health, they will be removed from the line. Next, robot 3 and robot 4 will collide and since robot 4's health is smaller, it gets removed, and robot 3's health becomes 15 - 1 = 14. Only robot 3 remains, so we return [14].
# Example 3:
#
#
#
# Input: positions = [1,2,5,6], healths = [10,10,11,11], directions = "RLRL"
# Output: []
# Explanation: Robot 1 and robot 2 will collide and since both have the same health, they are both removed. Robot 3 and 4 will collide and since both have the same health, they are both removed. So, we return an empty array, [].
#
#
# Constraints:
#
# 1 <= positions.length == healths.length == directions.length == n <= 105
# 1 <= positions[i], healths[i] <= 109
# directions[i] == 'L' or directions[i] == 'R'
# All values in positions are distinct
# Solution Stack
# General idea
# Lets create storage of robots that represent list contains lists and in each list [Number of robot, robot position, robot health, robot direction]. Then sort its storage in ascending order by positions.
# Lets create a stack to store robots. Since we sorted storage in ascending order we only need to check case when left robot have 'R' direction and right robot have 'L' direction. In other cases we can add to the stack current robot.
# Start iterate from storage and check next conditions:
# Stack is empty - append current robot to stack
# Left robot have some direction as current - append current robot to stack
# Left robot not overlaped with right robot - append current robot to stack
# Create while loop and iterate until (stack is not empty AND left robot have 'R' direction AND right robot have 'L' direction AND health of left robot is less than health of right robot) - at each iteration descrease health of right robot and pop left robot from stack. After loop we check some cases:
# 4.1) Stack not empty AND left robot have 'R' direction AND right robot have 'L' direction and they healths equal - pop robot from stack(it means that both current right and left robot destroyed)
# 4.2) Stack not empty AND left robot have 'R' direction AND right robot have 'L' direction and health of left robot is more than health of right robot - just decrease health of left robot(left robot destroy right robot)
# 4.3) Stack is empty OR (stack is not empty and left robot direction equal to right robot direction) - append current robot to stack
# At the end sort in ascending order stack by robot number and return health each of them
# Complexity
# Time complexity: O(NlogN)
# Space complexity: O(N)
# Code
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        line: list[list[int]] = []
        for idx in range(len(positions)):
            line.append([idx + 1, positions[idx], healths[idx], directions[idx]])
        line.sort(key=lambda x: x[1])

        stack: list[list[int]] = []
        for robot in line:
            if not stack: stack.append(robot) # Case 1
            elif stack:
                if stack[-1][-1] == robot[-1]: # Case 2
                    stack.append(robot)
                    continue
                elif stack[-1][-1] == 'L' and robot[-1] == 'R': # Case 3
                    stack.append(robot)
                    continue
                while stack and stack[-1][-1] == 'R' and robot[-1] == 'L' and stack[-1][2] < robot[2]: # Case 4
                    stack.pop()
                    robot[2] -= 1
                if stack and stack[-1][-1] == 'R' and robot[-1] == 'L' and stack[-1][2] == robot[2]: # Case 4.1
                    stack.pop()
                elif stack and stack[-1][-1] == 'R' and robot[-1] == 'L' and stack[-1][2] > robot[2]: # Case 4.2
                    stack[-1][2] -= 1
                elif not stack or (stack and stack[-1][-1] == robot[-1]): # Case 4.3
                    stack.append(robot)

        stack.sort(key=lambda x: x[0])
        return [robot[2] for robot in stack]