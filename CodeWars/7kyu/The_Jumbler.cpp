/*
Situation
One day Alice was at the casino on her favorite slot machine ("The Jumbler") when she noticed a set of numbers occasionally flashing in one corner of the screen. She found that by treating them as indices, reordering them according to a pattern, and counting the reorderings, she could know how many spins to make before the machine would finally hit a big jackpot payout!


Reordering
The pattern Alice discovers goes as follows:

select the value at index zero
(if the value is 0 do not continue)
elsewise, the value is our search index
go to new value found at the search index
remove this new value from its place in order
reposition this new value onto the front of the list
(if the new value is zero, the reorderings will cease)
elsewise, repeat all instructions with this new ordering

Task
Write a function to help Alice find out the count
of times the given integers have to be reordered
and thus know how many Jumbler spins to make
before betting large and getting a huge payout!!


Input
A(n) array / list / tuple / vector of unsigned integers.

values represent the indices of the collection itself
thus the values are all distinct from one another
and all indices guaranteed to be present
the values will be randomly shuffled

Output
An unsigned integer
        of the count of times the given numbers must be reordered
                according to Alice's Reordering Pattern
                        before the value at index zero actually becomes 0 itself.


Example
    Step 1
        Given the numbers 2, 0, 3, 1, we select 2 as the search index.
        The value 3 is found at that index, so 3 is moved to the front.

    Step 2
        Now with numbers 3, 2, 0, 1, we select 3 as the search index.
        The value 1 is found at that index, so 1 is moved to the front.

    Step 3
        Now with numbers 1, 3, 2, 0, we select 1 as the search index.
        The value 3 is found at that index, so 3 is moved to the front.

    Step 4
        Now with numbers 3, 1, 2, 0, we select 3 as the search index.
        The value 0 is found at that index, so 0 is moved to the front.

    Conclusion
        With zero now finally at the front of the order: 0, 3, 1, 2
        the reordering comes to a close, and we have our answer.

        In this case, it took 4 steps of reordering to jumble zero to the front.


Enjoy!
    ...and please consider one of the following kata to solve next:

Is Sator Square?
Playing With Toy Blocks ~ Can you build a 4x4 square?
Four Letter Words ~ Mutations
Crossword Puzzle! (2x2)
Interlocking Binary Pairs
Setting Places for the Dead
Four Letter Words ~ Anagrams
Shuffle an Integer
Minimum Percentage of Visitors that Ate All Foods
FundamentalsAlgorithmsData Structures
*/