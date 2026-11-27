/*
Task
A rectangle with sides equal to even integers a and b is drawn on the Cartesian plane. Its center (the intersection point of its diagonals) coincides with the point (0, 0), but the sides of the rectangle are not parallel to the axes; instead, they are forming 45 degree angles with the axes.

How many points with integer coordinates are located inside the given rectangle (including on its sides)?

Example
For a = 6 and b = 4, the output should be 23

The following picture illustrates the example, and the 23 points are marked green.



Input/Output
[input] integer a

A positive even integer.

Constraints: 2 ≤ a ≤ 10000.

[input] integer b

A positive even integer.

Constraints: 2 ≤ b ≤ 10000.

[output] an integer

The number of inner points with integer coordinates.

Puzzles
*/
// Solution
package kata

import "math"

func RectangleRotation(a, b int) int {
    A := int(math.Floor(float64(a) / math.Sqrt2))
    B := int(math.Floor(float64(b) / math.Sqrt2))
    evenA := 2*(A/2) + 1
    oddA := 2*((A+1)/2)
    evenB := 2*(B/2) + 1
    oddB := 2*((B+1)/2)
    return evenA*evenB + oddA*oddB
}