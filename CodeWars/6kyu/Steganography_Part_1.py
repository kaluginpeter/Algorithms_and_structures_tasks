# Steganography Part 1
# Part 1 of a series using Steganography on RGB image pixels.
# Part 2: https://www.codewars.com/kata/6251cba4629507b60a041b0e
#
# Steganography is the practice of concealing a message within another medium.
#
# In this case, we'll be taking a message string, and concealing it inside of RGB (Red, Green, Blue) Image Pixels using Least Significant Bit (LSB) Insertion.
#
# Your function will take the string msg and build a Bitmask array that is then applied to the pixels array, returning the modified pixel values.
#
# Notes
# You can assume that the pixels inner arrays always have a length of 3 (for Red, Green, Blue).
# Your code should return nil/None if there aren't enough pixels to conceal the message.
# If the message has been fully concealed and there are remaining pixels, the remaining pixels should be left unmodified.
# Since bytes are 8 bits long and pixels are in groups of 3, the last color of every 3rd array/ group of pixels should not be modified.
# Example
# With the following inputs:
#
# msg = "Hello"
# pixels = [
#   [255, 0, 0],[0, 255, 0],[0, 0, 255],
#   [255, 0, 0],[0, 255, 0],[0, 0, 255],
#   [169, 105, 71],[172, 211, 192],[181, 140, 38],
#   [108, 58, 63],[105, 235, 16],[204, 69, 21],
#   [24, 40, 224],[88, 84, 121],[123, 41, 163],
# ]
# Bitmask Array
# The bitmask array is a binary representation of each string character. For example with "Hello" the first character is H, and the ASCII value of H is 72, which is is 01001000 in binary.
#
# A bitmask array for H will look like:
#
# # 01001000 -> 72 -> 'H'
# bitmask = [0, 1, 0, 0, 1, 0, 0, 0]
# Except for the last color of every third pixel,
# each bit of the bitmask is applied to one color value of the pixels array, using lsb insertion (which could actually be seen as a lsb replacement).
#
# Ex:
#
# The first color in the pixels array is 255 which is 11111111 in binary.
# Our first bit in the bitmask array is 0, we'll need to insert 0 as the LSB of 11111111 giving us 11111110
# Note: you can also think of this as replacing the bit that is already there with a new bit.
# This color has been modified to 254, move on to the next color and next bit in the bitmask array
# Example output:
# output = [
#   [254, 1, 0],[0, 255, 0],[0, 0, 255],           // <- 01001000 <- 72  <- 'H'
#   [254, 1, 1],[0, 254, 1],[0, 1, 255],           // <- 01100101 <- 101 <- 'e'
#   [168, 105, 71],[172, 211, 193],[180, 140, 38], // <- 01101100 <- 108 <- 'l'
#   [108, 59, 63],[104, 235, 17],[204, 68, 21],    // <- 01101100 <- 108 <- 'l'
#   [24, 41, 225],[88, 85, 121],[123, 41, 163],    // <- 01101111 <- 111 <- 'o'
# ]
# Notice how each RGB pixel group contains off-by-one differences, this is the bitmask array applied to the input pixels LSB bit-by-bit.
#
# CryptographyFundamentals
# Solution
def conceal(msg: str, pixels: list[list[int]]):
    bits = []
    for ch in msg:
        x = ord(ch)
        for i in range(7, -1, -1): bits.append((x >> i) & 1)
    writable = []
    for i, pixel in enumerate(pixels):
        for c in range(3):
            if c == 2 and i % 3 == 2: continue
            writable.append((i, c))
    if len(bits) > len(writable): return None
    out = [p[:] for p in pixels]
    for bit, (pi, ci) in zip(bits, writable):
        out[pi][ci] = (out[pi][ci] & ~1) | bit
    return out