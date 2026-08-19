


/*
Transform an array of integers through two distinct phases: first by filling in local "valleys", then by expanding interior "peaks".

Processing Order & Rules
To ensure a completely deterministic result across all implementations:

Left-to-Right Priority: Always process the first valid valley or peak encountered when scanning from left to right (from index 1 to N - 2).
Eager Update & Restart: As soon as an element is modified or absorbed, immediately restart the scan from index 1.
Phase 1: Valley Fill
Scan the array for any interior element X that is strictly smaller than both its immediate left (L) and right (R) neighbors:

Condition: L > X and X < R
Action: Replace X with the sum of its neighbors (L + R).
Process the first match found from left to right, then restart the scan from the beginning. Repeat until no valleys remain.
Phase 2: Peak Inflation
Scan the array for any interior element X that is strictly greater than both its immediate left (L) and right (R) neighbors:

Condition: L < X and X > R
Action: X absorbs both neighbors, replacing the triplet [L, X, R] with a single element L + X + R.
Process the first match found from left to right, then restart the scan from the beginning. Repeat until no peak can absorb its neighbors.
Note: Elements at the boundaries (index 0 and the last index) can never trigger Phase 1 or Phase 2 directly because they lack neighbors on both sides.

Examples
Example 1
Input: [5, 2, 6, 1, 4]

Phase 1: Valley Fill

2 is between 5 and 6 (5 > 2 and 2 < 6) -> replaced by 5 + 6 = 11. [5, 11, 6, 1, 4]
1 is between 6 and 4 (6 > 1 and 1 < 4) -> replaced by 6 + 4 = 10. [5, 11, 6, 10, 4]
6 is between 11 and 10 (11 > 6 and 6 < 10) -> replaced by 11 + 10 = 21. [5, 11, 21, 10, 4] (No valleys remain)
Phase 2: Peak Inflation

21 is between 11 and 10 (11 < 21 and 21 > 10) -> absorbs both: 21 + 11 + 10 = 42. [5, 42, 4]
42 is between 5 and 4 (5 < 42 and 42 > 4) -> absorbs both: 42 + 5 + 4 = 51. [51]
Output: [51]

Example 2
Input: [7, 4, 3, 8, 7]

Phase 1: Valley Fill

3 is between 4 and 8 (4 > 3 and 3 < 8) -> replaced by 4 + 8 = 12. [7, 4, 12, 8, 7]
4 is between 7 and 12 (7 > 4 and 4 < 12) -> replaced by 7 + 12 = 19. [7, 19, 12, 8, 7] (No valleys remain)
Phase 2: Peak Inflation

19 is between 7 and 12 (7 < 19 and 19 > 12) -> absorbs both: 19 + 7 + 12 = 38. [38, 8, 7] (No interior peak exists matching L < X > R)
Output: [38, 8, 7]

Example 3
Input: [10, 10, 10]

Phase 1: Valley Fill

No elements are strictly smaller than both neighbors. Array remains unchanged.
Phase 2: Peak Inflation

No elements are strictly greater than both neighbors. Array remains unchanged.
Output: [10, 10, 10]

AlgorithmsArraysSimulationFundamentals
*/
// Solution
#include <vector>

std::vector<int> mountain(const std::vector<int>& arr_in) {
    std::vector<int> arr = arr_in;

    if (arr.size() >= 3) {
        bool changed = true;
        while (changed) {
            changed = false;
            for (size_t i = 1; i + 1 < arr.size(); ++i) {
                if (arr[i-1] > arr[i] && arr[i] < arr[i+1]) {
                    arr[i] = arr[i-1] + arr[i+1];
                    changed = true;
                    break;
                }
            }
        }
    }
    if (arr.size() >= 3) {
        bool changed = true;
        while (changed) {
            changed = false;
            for (size_t i = 1; i + 1 < arr.size(); ++i) {
                if (arr[i-1] < arr[i] && arr[i] > arr[i+1]) {
                    int newVal = arr[i-1] + arr[i] + arr[i+1];
                    arr.erase(arr.begin() + (i-1), arr.begin() + (i+2));
                    arr.insert(arr.begin() + (i-1), newVal);
                    changed = true;
                    break;
                }
            }
        }
    }

    return arr;
}