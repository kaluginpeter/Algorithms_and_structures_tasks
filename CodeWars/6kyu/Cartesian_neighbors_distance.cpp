/*
Previous Cartesian neighbors kata
In the previous kata we have been searching for all the neighboring points in a Cartesian coordinate system. As we know, each point in a coordinate system has eight neighboring points when we search them within a range of 1, but now we will change the range through the third argument of our function (range is always greater than zero).

For example if range = 2, count of neighboring points = 24.

You shall write a function that returns an array of unique distances between the given point and all neighboring points within range.

Distances inside your result need not be sorted (any order is valid).

Do not round the distances; tests will use approximate equality.

For Example:

 x  y range
(3, 2, 1) --> {1.4142135624, 1.0}
(0, 0, 2) --> {1.0, 1.4142135624, 2.0, 2.2360679775, 2.8284271247}
FundamentalsMathematics
*/
// Solution
#include <vector>
#include <set>
#include <cmath>

using std::vector;

vector<double> cartesianNeighborsDistance(int x, int y, int range)
{
    std::set<int> squares;
    for (int dx = -range; dx <= range; ++dx) {
        for (int dy = -range; dy <= range; ++dy) {
            if (dx == 0 && dy == 0) continue;
            squares.insert(dx * dx + dy * dy);
        }
    }

    vector<double> result;
    for (int d2 : squares) result.push_back(std::sqrt(static_cast<double>(d2)));
    return result;
}