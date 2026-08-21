/*
The walker

The walker starts from point O, walks along OA, AB and BC. When he is in C (C will be in the upper half-plane), what is the distance CO? What is the angle tOC in positive degrees, minutes, seconds?

Angle tOA is alpha (here 45 degrees), angle hAB is beta (here 30 degrees), angle uBC is gamma(here 60 degrees).

Task
function solve(a, b, c, alpha, beta, gamma) with parameters

a, b, c: positive integers in units of distance (stand for OA, AB, BC)
alpha, beta, gamma: positive integers in degrees (positive angles are anticlockwise)
returns an array:

first element: distance CO (rounded to the nearest integer)
then angle tOC with the 3 following elements:
second element of the array: number of degrees in angle tOC (truncated positive integer)
third element of the array: number of minutes in angle tOC (truncated positive integer)
fourth element of the array: number of seconds in angle tOC (truncated positive integer)
Example:
print(solve(12, 20, 18, 45, 30, 60)) -> [15, 135, 49, 18]
- CO is 14.661... rounded to 15
- angle tOC is 135.821...
so
- degrees = 135
- minutes = 49.308...
- seconds = 18.518...

hence [15, 135, 49, 18]
Note
If you need the constant pi you can use pi = 3.14159265358979323846

FundamentalsGeometry
*/
// Solution
package kata

import "math"
func Solve(a, b, c, alpha, beta, gamma int) []int {
	d1 := degToRad(float64(alpha))
	d2 := degToRad(90 + float64(beta))
	d3 := degToRad(180 + float64(gamma))

	ax, ay := float64(a)*math.Cos(d1), float64(a)*math.Sin(d1)
	bx, by := ax+float64(b)*math.Cos(d2), ay+float64(b)*math.Sin(d2)
	cx, cy := bx+float64(c)*math.Cos(d3), by+float64(c)*math.Sin(d3)

	co := math.Hypot(cx, cy)

	angle := radToDeg(math.Atan2(cy, cx))
	if angle < 0 {
		angle += 360
	}

	degrees := int(angle)
	minutesFloat := (angle - float64(degrees)) * 60
	minutes := int(minutesFloat)
	seconds := int((minutesFloat - float64(minutes)) * 60)

	return []int{int(math.Round(co)), degrees, minutes, seconds}
}

func degToRad(deg float64) float64 { return deg * math.Pi / 180 }
func radToDeg(rad float64) float64 { return rad * 180 / math.Pi }