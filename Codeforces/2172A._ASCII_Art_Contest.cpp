/*
A. ASCII Art Contest
time limit per test1 second
memory limit per test256 megabytes
Three leading AI-powered creative assistants—Gemini, ChatGPT, and Claude—enter the first ever ASCII Art Contest, where they must impress a panel of human judges with their text-based masterpieces.

Each participant receives a score between 80 and 100 (inclusive). The organizers want to announce the final standing only if the judges' opinions are "close enough"; otherwise, they will ask the judges to reconsider.

Given the three integer scores of Gemini, ChatGPT, and Claude, determine the contest result:

If the maximum score and the minimum score differ by at least 10 points, print check again (the judging seems inconsistent, so the panel must re-evaluate).
Otherwise, print final X, where X is the median of the three scores (the score that would be in the middle if all three were sorted in non-decreasing order).
Input
A single line contains three integers g,c,ℓ
, representing the scores of Gemini, ChatGPT, and Claude respectively.

80≤g,c,ℓ≤100
Output
Print the required answer in a line.

Examples
InputCopy
88 94 95
OutputCopy
final 94
InputCopy
100 80 81
OutputCopy
check again
InputCopy
98 99 98
OutputCopy
final 98
InputCopy
95 86 85
OutputCopy
check again
*/
// Solution
// C++ O(1) O(1) Greedy
#include <iostream>
#include <vector>
#include <algorithm>


void solution() {
    int a, b, c;
    std::cin >> a >> b >> c;
    std::vector<int> votes = {a, b, c};
    std::sort(votes.begin(), votes.end());
    if (votes[2] - votes[0] >= 10) std::cout << "check again\n";
    else std::printf("final %d\n", votes[1]);
}


int main() {
    solution();
}