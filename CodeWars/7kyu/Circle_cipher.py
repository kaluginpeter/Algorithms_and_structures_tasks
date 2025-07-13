# Imagine a circle. To encode the word codewars, we could split the circle into 8 parts (as codewars has 8 letters):
#
# Then add the letters in a clockwise direction:Then remove the circle:
# If we read the result from left to right, we get csordaew.
#
# Decoding is the same process in reverse. If we decode csordaew, we get codewars.
#
# Examples:
# encode "codewars" -> "csordaew"
# decode "csordaew" -> "codewars"
# encode "white" -> "wehti"
# decode "wehti" -> "white"
# CiphersAlgorithms
# Solution
def encode(s: str) -> str:
    output: list[str] = []
    left: int = 0
    right: int = len(s) - 1
    while left < right:
        output.append(s[left])
        output.append(s[right])
        left += 1
        right -= 1
    if left == right: output.append(s[left])
    return ''.join(output)


def decode(s: str) -> str:
    return s[::2] + s[1::2][::-1]