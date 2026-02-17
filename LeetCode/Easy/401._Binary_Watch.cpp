/*
A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

For example, the below binary watch reads "4:51".


Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.

The hour must not contain a leading zero.

For example, "01:00" is not valid. It should be "1:00".
The minute must consist of two digits and may contain a leading zero.

For example, "10:2" is not valid. It should be "10:02".


Example 1:

Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
Example 2:

Input: turnedOn = 9
Output: []


Constraints:

0 <= turnedOn <= 10
*/
// Solution
// C++ O(1) O(1) BitManipulation
class Solution {
public:
    vector<string> readBinaryWatch(int turnedOn) {
        std::vector<std::string> output;
        for (int mask = 0; mask < (1 << 10); ++mask) {
            if (__builtin_popcount(mask) != turnedOn) continue;
            int hours = mask >> 6;
            int minutes = mask & 0b111111;
            if (hours < 12 && minutes < 60) {
                char buf[6];
                std::sprintf(buf, "%d:%02d", hours, minutes);
                output.push_back(buf);
            }
        }
        return output;
    }
};