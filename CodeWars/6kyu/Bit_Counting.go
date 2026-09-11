/*
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

BitsAlgorithms
*/
// Solution
package kata

func CountBits(n uint) int {
    if n == 0 { return 0}
    return int(n & 1) + CountBits(n >> 1)
}