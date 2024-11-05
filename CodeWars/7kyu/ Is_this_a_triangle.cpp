/*
Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

Examples:

Input -> Output
1,2,2 -> true
4,2,3 -> true
2,2,2 -> true
1,2,3 -> false
-5,1,3 -> false
0,2,3 -> false
1,2,9 -> false
MathematicsFundamentals
*/
// Solution
namespace Triangle
{
  bool isTriangle(int a, int b, int c)
  {
    if (a == 0 || b == 0 || c == 0) {
      return false;
    }
    if (a + b > c && a + c > b && b + c > a) {
      return true;
    }
    return false;
  }
};