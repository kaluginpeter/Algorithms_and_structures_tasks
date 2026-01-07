/*
You have an array or list of coordinates or points (e.g. [ [1, 1], [3, 4], ... , [5, 2] ]), and your task is to find the area under the graph defined by these points (limited by x of the first and last coordinates as left and right borders, y = 0 as the bottom border and the graph as top border).

Notes:

x can be negative;
x of the next pair of coordinates will always be greater than the previous one;
y >= 0;
the array will contain more than 2 points.
Example
x=1 (left border)               x=5 (right border)
|                      x,y      |
|                    /\         |
|                   /  \        |
|    x,y           /    \       |
|   /\            /      \      |
|  /  \    x,y   /        \     |
| /    \  /\    /          \    |
|/      \/  \  /            \   |
|x,y    x,y  \/              \  |
|            x,y              \ |
|_____________________________ \x,y_____ y=0 (bottom border)
The required area:

|                               |
|                    /\         |
|                   /\\\        |
|                  /\\\\\       |
|   /\            /\\\\\\\      |
|  /\\\          /\\\\\\\\\     |
| /\\\\\  /\    /\\\\\\\\\\\    |
|/\\\\\\\/\\\  /\\\\\\\\\\\\\   |
|\\\\\\\\\\\\\/\\\\\\\\\\\\\\\  |
|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ |
|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|
Definition of points
struct Point {
  double x, y;

  Point(double x, double y) : x(x), y(y) {}

  // also, there are two extra utility methods:
  // `toString` and the stream insertion operator (`operator<<`),
  // provided to you for easier debugging.
};
AlgorithmsGraphs
*/