/*
Overview
We are going to be studying permutations of n distinct elements - for simplicity we shall use the integers from 1 to n.

If we start with the integers 1 to n in ascending order in a list:

[1, 2, 3, ..., n-2, n-1, n]

then, for a given value of n, how many permutations of this list are there in which each element's index changes by AT MOST 1 after the permutation?

Inputs
You will be given an integer, n, representing the number of distinct elements that we want to permute.

As mentioned, for definiteness, you can think of the integers from 1 to n in a starting list given by [1, 2, ..., n]

Performance requirement: Values from 0 up to 200 may be tested.

Output
You must return an integer representing the total number of possible permutations of the list [1, 2, ..., n] that satisfy the requirement.

Important notes
The identity permutation, where no element changes its index, is a valid permutation according to the definition, so make sure you include it in your total.
You cannot wrap-around the list, so changing element 1 with element n is not allowed (except for the case n = 2 of course).
Walk-through Example
Let's consider the case n = 4; so concretely we are looking at permutations of the list [1,2,3,4]

There are in total n! = 4! = 24 possible permutations of this list.

If you write out all of these 24 possible permutations, you will find that only 5 satisfy the above requirement:

[1,2,3,4] - no element changes index.

[2,1,3,4] - elements 1&2 change indices by +1 and -1 respectively.

[1,3,2,4] - elements 2&3 change indices by +1 and -1 respectively.

[1,2,4,3] - elements 3&4 change indices by +1 and -1 respectively.

[2,1,4,3] - elements 1&2 change indices by +1 and -1 respectively and elements 3&4 change indices by +1 and -1 respectively.

In all of the 5 above permutations, the elements' indices have indeed changed by at most 1.

So for the input n = 4 you should return the answer 5.

Explanation of an INVALID permutation for n = 4

To be clear, let's consider another permutation which does not satisfy the kata's requirement, and therefore should not be included in your total:

[3,4,2,1] - element 1 has changed index by +3, element 2 by +1, element 3 by -2, element 4 by -2.

The above permutation is therefore not allowed, since at least one element has changed index by more than 1.

FundamentalsAlgorithmsPuzzlesMathematicsDiscrete MathematicsCombinatorics
*/