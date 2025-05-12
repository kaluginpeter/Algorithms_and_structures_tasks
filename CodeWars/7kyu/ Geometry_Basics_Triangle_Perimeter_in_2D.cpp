/*
This series of katas will introduce you to basics of doing geometry with computers.

Point objects have x, y attributes. Triangle objects have attributes a, b, c describing their corners, each of them is a Point.

Write a function calculating perimeter of a Triangle defined this way.

GeometryFundamentals
*/
// Solution
#include <cmath>
#include <iostream>
double triangle_perimeter(const Triangle& t){
  double first = std::sqrt(std::pow(t.a.x - t.b.x, 2) + std::pow(t.a.y - t.b.y, 2));
  double second = std::sqrt(std::pow(t.b.x - t.c.x, 2) + std::pow(t.b.y - t.c.y, 2));
  double third = std::sqrt(std::pow(t.a.x - t.c.x, 2) + std::pow(t.a.y - t.c.y, 2));
  return first + second + third;
}