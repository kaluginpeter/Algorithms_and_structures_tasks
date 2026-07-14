/*
Story
You want to play a spinning wheel with your friend. Unfortunately, you have used all of your money to buy things that are more useful than a spinning wheel. So you have to create the rule and the spinning wheel yourself.

Task
Your spinning wheel consists of sections which could be either "Win" or "Not Win". If you get "Win", you win right away. But If you get "Not Win", it's now your friend's turn to spin the wheel. This goes on forever until someone wins. You will be given a string which each character represent a section of the wheel. (Imagine getting that string up into the real world, and wrap it around a spinning wheel. The first character of the string is connected with the last character.) the "Win" section is transform to 'W' and the "Not Win" section is transform to 'N'. Find the probability of you winning the game if you go first in percentage, rounding down.

Example
Ex.1
Given a string "WWWWWW", all of the section is "Win". If you go first, you will always win. So in this example, you have to return 100 for 100% winning probability.

Ex.2
Given a string "NNN", all of the section is "Not Win". In this scenario, no one will ever win. So your probability of winning is 0%. So you have to return 0.

Ex.3
If you calculate the probability and get 31.6%, you have to return 31 because .6% gets round down.

Extra
>The probability can never be more than 100% or less than 0%.
>The string will only consists of 'W' or 'N'.
Note about rounding
For any valid input string there exists one and only one correct integer answer. Hint: it is possible to solve this problem without floating-point arithmetic.

MathematicsGamesPuzzlesProbability
*/
// Solution
#include <string>
#include <algorithm>

int spinning_wheel(std::string wheel) {
    int num = 0, denom = 0;
    for (char& ch : wheel) {
        if (ch == 'W') ++num;
        else ++denom;
    }
    if (!num) return 0;
    return (num + denom) * 100 / (num + (denom << 1));
}