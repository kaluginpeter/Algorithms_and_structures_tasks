/*
Background
Pat Programmer is worried about the future of jobs in programming because of the advance of AI tools like ChatGPT, and he decides to become a chef instead! So he wants to be an expert at flipping pancakes.

A pancake is characterized by its diameter, a positive integer.
Given a stack of pancakes, you can insert a spatula under any pancake and then flip, which reverses the order of all the pancakes on top of the spatula.

Task
Write a function that takes a stack of pancakes and returns a sequence of flips that arranges them in order by diameter, with the largest pancake at the bottom and the smallest at the top. The pancakes are given as a list of positive integers, with the left end of the list being the top of the stack.

Based on Problem 4.6.2 in Skiena & Revilla, "Programming Challenges".

Example
Consider the stack [1,5,8,3]. One way of achieving the desired order is as follows:

The 8 is the biggest, so it should be at the bottom. Put the spatula under it (position 2 in the list) and flip.
This transforms the stack into [8,5,1,3], with the 8 at the top. Then flip the entire stack (spatula position 3).
This transforms the stack into [3,1,5,8], which has the 8 at the bottom.
And since the 5 is in the correct position as well, now flip the 1 and 3 (spatula position 1).
The stack is now [1,3,5,8], as desired. The function should return [2,3,1].

Note
You don't have to find the shortest sequence of flips. That is a hard problem - see https://en.wikipedia.org/wiki/Pancake_sorting. However, don't include unnecessary flips, in the following sense:

If two consecutive flips leave the stack in the same state, they should be omitted.
For example, [2,3,2,2,1] also arranges [1,5,8,3] correctly, but 2,2 is unnecessary.
Flipping only the top pancake doesn't achieve anything.
Performance should not be a issue. If Pat can flip 1,000 pancakes with diameters between 1 and 1,000, he thinks he can get a job!

ArraysSorting
*/
// Solution
#include <vector>

std::vector<int> flipPancakes(std::vector<int>& stack) {
    std::vector<int> output;
    int bound = stack.size() - 1;
    while (bound > 0) {
        int right = bound - 1;
        for (int middle = right - 1; middle >= 0; --middle) {
            if (stack[middle] >= stack[right]) right = middle;
        }
        if (stack[right] <= stack[bound]) {
            --bound;
            continue;
        }
        output.push_back(right);
        int left = 0;
        while (left < right) {
            std::swap(stack[left], stack[right]);
            ++left;
            --right;
        }
        output.push_back(bound);
        right = bound;
        left = 0;
        while (left < right) {
            std::swap(stack[left], stack[right]);
            ++left;
            --right;
        }
        --bound;
    }
    return output;
}