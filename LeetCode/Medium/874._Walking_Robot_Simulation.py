# A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot can receive a sequence of these three possible types of commands:
#
# -2: Turn left 90 degrees.
# -1: Turn right 90 degrees.
# 1 <= k <= 9: Move forward k units, one unit at a time.
# Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, then it will instead stay in its current location and move on to the next command.
#
# Return the maximum Euclidean distance that the robot ever gets from the origin squared (i.e. if the distance is 5, return 25).
#
# Note:
#
# North means +Y direction.
# East means +X direction.
# South means -Y direction.
# West means -X direction.
# There can be obstacle in [0,0].
#
#
# Example 1:
#
# Input: commands = [4,-1,3], obstacles = []
# Output: 25
# Explanation: The robot starts at (0, 0):
# 1. Move north 4 units to (0, 4).
# 2. Turn right.
# 3. Move east 3 units to (3, 4).
# The furthest point the robot ever gets from the origin is (3, 4), which squared is 32 + 42 = 25 units away.
# Example 2:
#
# Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# Output: 65
# Explanation: The robot starts at (0, 0):
# 1. Move north 4 units to (0, 4).
# 2. Turn right.
# 3. Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at (1, 4).
# 4. Turn left.
# 5. Move north 4 units to (1, 8).
# The furthest point the robot ever gets from the origin is (1, 8), which squared is 12 + 82 = 65 units away.
# Example 3:
#
# Input: commands = [6,-1,-1,6], obstacles = []
# Output: 36
# Explanation: The robot starts at (0, 0):
# 1. Move north 6 units to (0, 6).
# 2. Turn right.
# 3. Turn right.
# 4. Move south 6 units to (0, 0).
# The furthest point the robot ever gets from the origin is (0, 6), which squared is 62 = 36 units away.
#
#
# Constraints:
#
# 1 <= commands.length <= 104
# commands[i] is either -2, -1, or an integer in the range [1, 9].
# 0 <= obstacles.length <= 104
# -3 * 104 <= xi, yi <= 3 * 104
# The answer is guaranteed to be less than 231.
# Solution O(N * K), where K is maximum operations O(N)
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        cur_x = cur_y = 0
        max_distance: int = 0
        north: bool = True
        east = south = west = False
        storage: set[tuple[int, int]] = set()
        for obstacle in obstacles:
            storage.add((obstacle[0], obstacle[1]))
        for command in commands:
            if command == -2:
                if north: north, west = False, True
                elif west: west, south = False, True
                elif south: south, east = False, True
                else: east, north = False, True
            elif command == -1:
                if north: north, east = False, True
                elif west: west, north = False, True
                elif south: south, west = False, True
                else: east, south = False, True
            else:
                if north:
                    for new_y in range(cur_y + 1, cur_y + command + 1):
                        if (cur_x, new_y) in storage: break
                        else: cur_y += 1
                elif west:
                    for new_x in range(cur_x - 1, cur_x - command - 1, -1):
                        if (new_x, cur_y) in storage: break
                        else: cur_x -= 1
                elif south:
                    for new_y in range(cur_y - 1, cur_y - command - 1, -1):
                        if (cur_x, new_y) in storage: break
                        else: cur_y -= 1
                else:
                    new_x: int = cur_x + command
                    for new_x in range(cur_x + 1, cur_x + command + 1):
                        if (new_x, cur_y) in storage: break
                        else: cur_x += 1
                max_distance = max(max_distance, cur_x**2 + cur_y**2)

        return max_distance