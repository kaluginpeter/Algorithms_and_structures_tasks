/*
Toggle, Set, and Clear Bits
Your task is to implement a collection of utility functions that perform common bitwise operations on integers. All bit positions are zero-based, meaning position 0 refers to the least significant bit.

Toggles (flips) the bit at the given position. If the bit is 0, it becomes 1; if it is 1, it becomes 0.

toggleBit(5, 1) => 7
Sets the bit at the given position to 1, without modifying other bits.

setBit(5, 1) => 7
Clears (sets to 0) the bit at the given position, leaving all other bits unchanged.

clearBit(7, 1) => 5
Checks whether the bit at the given position is set to 1. Returns true if it is set, otherwise false.

isBitSet(5, 0) => true
Sets all bits to 1 wherever the mask has 1s.

setMultipleBits(5, 3) => 7
Clears all bits wherever the mask has 1s.

clearMultipleBits(7, 2) => 5
Toggles all bits wherever the mask has 1s.

toggleMultipleBits(5, 3) => 6
Notes
All functions should return the resulting number (or a boolean for isBitSet).
Bits
*/
// Solution
int toggle_bit(int n, unsigned pos)
{
    return n ^ (1 << pos);
}

int set_bit(int n, unsigned pos)
{
    return n | (1 << pos);
}

int clear_bit(int n, unsigned pos)
{
    return n & ~(1 << pos);
}

bool is_bit_set(int n, unsigned pos)
{
    return (n & (1 << pos)) != 0;
}

int set_multiple_bits(int n, unsigned mask)
{
    return n | mask;
}

int clear_multiple_bits(int n, unsigned mask)
{
    return n & ~mask;
}

int toggle_multiple_bits(int n, unsigned mask)
{
    return n ^ mask;
}