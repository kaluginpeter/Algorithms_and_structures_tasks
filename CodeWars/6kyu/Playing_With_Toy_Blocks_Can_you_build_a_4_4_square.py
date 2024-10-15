# An Invitation
# Most of us played with toy blocks growing up. It was fun and you learned stuff. So what else can you do but rise to the challenge when a 3-year old exclaims, "Look, I made a square!", then pointing to a pile of blocks, "Can you do it?"
#
# Our Blocks
# Just to play along, of course we'll be viewing these blocks in two dimensions. Depth now being disregarded, it turns out the pile has four different sizes of block: 1x1, 1x2, 1x3, and 1x4. The smallest one represents the area of a square, the other three are rectangular, and all differ by their width. Integers matching these four widths are used to represent the blocks in the input.
#
# The Square
# Well, the kid made a 4x4 square from this pile, so you'll have to match that. Noticing the way they fit together, you realize the structure must be built in fours rows, one row at a time, where the blocks must be placed horizontally. With the known types of block, there are five types of row you could build:
#
# 1 four-unit block
# 1 three-unit block plus 1 one-unit bock (in either order)
# 2 two-unit blocks
# 1 two-unit block plus 2 one-unit blocks (in any order)
# 4 one-unit blocks
# Some Notes
# Amounts for all four block sizes will each vary from 0 to 16.
# The total size of the pile will also vary from 0 to 16.
# A valid square doesn't have to use all given blocks.
# The order of rows is irrelevant.
# Some Examples
# Given 1, 3, 2, 2, 4, 1, 1, 3, 1, 4, 2 there are many ways you could construct a square. Here are three possibilities, as described by their four rows:
#
# ONE
#
# 1 four-unit block
# 2 two-unit blocks
# 1 four-unit block
# 4 one-unit blocks
# TWO
#
# 1 three-unit block plus 1 one-unit block
# 2 two-unit blocks
# 1 four-unit block
# 1 one-unit block plus 1 three-unit block
# THREE
#
# 2 two-unit blocks
# 1 three-unit block plus 1 one-unit block
# 1 four-unit block
# 2 one-unit blocks plus 1 two-unit block
# Given 1, 3, 2, 4, 3, 3, 2 there is no way to complete the task, as you could only build three rows of the correct length. The kid will not be impressed.
#
# NONE
#
# 1 four-unit block
# 2 two-unit blocks
# 1 three-unit block plus 1 one-unit block
# (here only sadness)
# Input
# blocks ~ array of random integers (1 <= x <= 4)
# Output
# true or false ~ whether you can build a square
# Enjoy!
# ...and please consider one of the following kata to solve next:
#
# Is Sator Square?
# Four Letter Words ~ Mutations
# Four Letter Words ~ Anagrams
# Crossword Puzzle! (2x2)
# Interlocking Binary Pairs
# Setting Places for the Dead
# LOGICARRAYSGAMESPUZZLESGEOMETRYALGORITHMS
# Solution
#include <vector>
#include <iostream>
bool build_square(const std::vector<int>& blocks) {
  std::unordered_map<int, int> hashmap;
  for (int num : blocks) {
    ++hashmap[num];
  }
  int layer = 0;
  layer += hashmap[4];
  int third = std::min(hashmap[3], hashmap[1]);
  layer += third;
  layer += hashmap[2] / 2;
  int remainder_doubles = std::min(hashmap[2] % 2, hashmap[1] - third);
  layer += remainder_doubles;
  layer += (hashmap[1] - third - remainder_doubles * 2) / 4;
  return layer >= 4;
}