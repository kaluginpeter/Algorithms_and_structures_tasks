/*
Write the following function:

func AreaOfPolygonInsideCircle(circleRadius float64, numberOfSides int) float64
It should calculate the area of a regular polygon of numberOfSides, number-of-sides, or number_of_sides sides inside a circle of radius circleRadius, circle-radius, or circle_radius which passes through all the vertices of the polygon (such circle is called circumscribed circle or circumcircle).

The answer should be a number rounded to 3 decimal places.

Input :: Output Examples

AreaOfPolygonInsideCircle(3, 3) // returns 11.691

AreaOfPolygonInsideCircle(5.8, 7) // returns 92.053

AreaOfPolygonInsideCircle(4, 5) // returns 38.042
Note: if you need to use Pi in your code, use the native value of your language unless stated otherwise.

MathematicsGeometryFundamentals
*/
// Solution
package kata

import "math"

const PI = 3.141592653589793 
func AreaOfPolygonInsideCircle(r float64, n int) float64 {
	fn := float64(n)
	area := math.Sin(2.0*PI/fn) * r * r * fn / 2
	return math.Round(area*1000) / 1000
}