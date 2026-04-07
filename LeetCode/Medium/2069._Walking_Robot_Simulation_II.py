# A width x height grid is on an XY-plane with the bottom-left cell at (0, 0) and the top-right cell at (width - 1, height - 1). The grid is aligned with the four cardinal directions ("North", "East", "South", and "West"). A robot is initially at cell (0, 0) facing direction "East".
#
# The robot can be instructed to move for a specific number of steps. For each step, it does the following.
#
# Attempts to move forward one cell in the direction it is facing.
# If the cell the robot is moving to is out of bounds, the robot instead turns 90 degrees counterclockwise and retries the step.
# After the robot finishes moving the number of steps required, it stops and awaits the next instruction.
#
# Implement the Robot class:
#
# Robot(int width, int height) Initializes the width x height grid with the robot at (0, 0) facing "East".
# void step(int num) Instructs the robot to move forward num steps.
# int[] getPos() Returns the current cell the robot is at, as an array of length 2, [x, y].
# String getDir() Returns the current direction of the robot, "North", "East", "South", or "West".
#
#
# Example 1:
#
# example-1
# Input
# ["Robot", "step", "step", "getPos", "getDir", "step", "step", "step", "getPos", "getDir"]
# [[6, 3], [2], [2], [], [], [2], [1], [4], [], []]
# Output
# [null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"]
#
# Explanation
# Robot robot = new Robot(6, 3); // Initialize the grid and the robot at (0, 0) facing East.
# robot.step(2);  // It moves two steps East to (2, 0), and faces East.
# robot.step(2);  // It moves two steps East to (4, 0), and faces East.
# robot.getPos(); // return [4, 0]
# robot.getDir(); // return "East"
# robot.step(2);  // It moves one step East to (5, 0), and faces East.
#                 // Moving the next step East would be out of bounds, so it turns and faces North.
#                 // Then, it moves one step North to (5, 1), and faces North.
# robot.step(1);  // It moves one step North to (5, 2), and faces North (not West).
# robot.step(4);  // Moving the next step North would be out of bounds, so it turns and faces West.
#                 // Then, it moves four steps West to (1, 2), and faces West.
# robot.getPos(); // return [1, 2]
# robot.getDir(); // return "West"
#
#
#
# Constraints:
#
# 2 <= width, height <= 100
# 1 <= num <= 105
# At most 104 calls in total will be made to step, getPos, and getDir.
# Solution
# Python O(NMK) O(1) Matrix Math Simulation
class Robot:

    def __init__(self, width: int, height: int):
        self.direction: list[str] = ['East', 'North', 'West', 'South']
        self.moves: list[tuple[int, int]] = [
            (1, 0), (0, 1), (-1, 0), (0, -1)
        ]
        self.n: int = height
        self.m: int = width
        self.ptr: int = 0
        self.x: int = 0
        self.y: int = 0
        self.bound: int = self.n + self.n + self.m + self.m - 4

    def step(self, num: int) -> None:
        overlaps: int = num // self.bound
        if num % self.bound == 0: overlaps -= 1
        num -= overlaps * self.bound
        for i in range(num):
            self.x += self.moves[self.ptr][0]
            self.y += self.moves[self.ptr][1]
            while (self.x < 0 or self.y < 0) or (self.x == self.m or self.y == self.n):
                self.x -= self.moves[self.ptr][0]
                self.y -= self.moves[self.ptr][1]
                self.ptr = (self.ptr + 1) % 4
                self.x += self.moves[self.ptr][0]
                self.y += self.moves[self.ptr][1]

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.direction[self.ptr]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()

# C++ O(NMK) O(1) Simulation Matrix
class Robot {
private:
    std:

:vector < std::string > direction = {
    "East", "North", "West", "South"
};
std::vector < std::pair < int, int >> moves = {
    {1, 0}, {0, 1}, {-1, 0}, {0, -1}
};
size_t
n = 0, m = 0, ptr = 0;
int32_t
x = 0, y = 0, bound = 0;
public:
Robot(int
width, int
height) {
    n = height;
m = width;
bound = n + n + m + m - 4;
}

void
step(int
num) {
    int
overlaps = num / bound;
if (num % bound == 0) - -overlaps;
num -= overlaps * bound;
for (size_t i = 0; i < num; ++i)
{
    x += moves[ptr].first;
y += moves[ptr].second;
while ((x < 0 | | y < 0) | | (x == m | | y == n)) {
x -= moves[ptr].first;
y -= moves[ptr].second;
ptr = (ptr + 1) % 4;
x += moves[ptr].first;
y += moves[ptr].second;
}
}
}

vector < int > getPos()
{
return {x, y};
}

string
getDir()
{
return direction[ptr];
}
};

/ **
*Your
Robot
object
will
be
instantiated and called as such:
*Robot * obj = new
Robot(width, height);
*obj->step(num);
*vector < int > param_2 = obj->getPos();
*string
param_3 = obj->getDir();
* /