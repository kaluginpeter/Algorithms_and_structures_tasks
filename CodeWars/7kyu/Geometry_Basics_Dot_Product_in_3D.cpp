/*
This series of katas will introduce you to basics of doing geometry with computers.

Vector objects have x, y, and z attributes.

Write a function calculating dot product of Vector a and Vector b.

You can read more about dot product on Wikipedia.

Tests round answers to 6 decimal places.

GeometryFundamentals
*/
// Solution
double dot_product(const Vector& a, const Vector& b){
    double output = 0;
    output += a.x * b.x;
    output += a.y * b.y;
    output += a.z * b.z;
    return output;
}