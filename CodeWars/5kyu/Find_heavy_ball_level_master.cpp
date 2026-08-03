/*
There are 8 balls numbered from 0 to 7. Seven of them have the same weight. One is heavier. Your task is to find its number.

Your function findBall will receive single argument - scales object. The scales object contains an internally stored array of 8 elements (indexes 0-7), each having the same value except one, which is greater. It also has a public method named getWeight(left, right) which takes two arrays of indexes and returns -1, 0, or 1 based on the accumulation of the values found at the indexes passed are heavier, equal, or lighter.

getWeight returns:

-1 if left pan is heavier

1 if right pan is heavier

0 if both pans weigh the same

Examples of scales.getWeight() usage:

scales.getWeight([3], [7]) returns -1 if ball 3 is heavier than ball 7, 1 if ball 7 is heavier, or 0 i these balls have the same weight.

scales.getWeight([3, 4], [5, 2]) returns -1 if weight of balls 3 and 4 is heavier than weight of balls 5 and 2 etc.

So where's the catch, you may ask. Well - the scales is very old. You can use it only TWICE before the scale breaks.

Too hard ? Try lower levels:

novice
conqueror
Still too easy ? Try this kata - ubermaster (made by by bellmyer)

PuzzlesLogicRiddles
*/
// Solution
#include <vector>

unsigned int findBall(Scales scales) {
    std::vector<int> left{0, 1, 2};
    std::vector<int> right{3, 4, 5};
    int res = scales.getWeight(left, right);
    if (res == -1) {
        res = scales.getWeight({0}, {1});
        if (res == -1) return 0;
        if (res == 1) return 1;
        return 2;
    }
    if (res == 1) {
        res = scales.getWeight({3}, {4});
        if (res == -1) return 3;
        if (res == 1) return 4;
        return 5;
    }
    res = scales.getWeight({6}, {7});
    return (res == -1) ? 6 : 7;
}