# B. Sort the Array
# time limit per test1 second
# memory limit per test256 megabytes
# Being a programmer, you like arrays a lot. For your birthday, your friends have given you an array a consisting of n distinct integers.
#
# Unfortunately, the size of a is too small. You want a bigger array! Your friends agree to give you a bigger array, but only if you are able to answer the following question correctly: is it possible to sort the array a (in increasing order) by reversing exactly one segment of a? See definitions of segment and reversing in the notes.
#
# Input
# The first line of the input contains an integer n (1 ≤ n ≤ 105) — the size of array a.
#
# The second line contains n distinct space-separated integers: a[1], a[2], ..., a[n] (1 ≤ a[i] ≤ 109).
#
# Output
# Print "yes" or "no" (without quotes), depending on the answer.
#
# If your answer is "yes", then also print two space-separated integers denoting start and end (start must not be greater than end) indices of the segment to be reversed. If there are multiple ways of selecting these indices, print any of them.
#
# Examples
# InputCopy
# 3
# 3 2 1
# OutputCopy
# yes
# 1 3
# InputCopy
# 4
# 2 1 3 4
# OutputCopy
# yes
# 1 2
# InputCopy
# 4
# 3 1 2 4
# OutputCopy
# no
# InputCopy
# 2
# 1 2
# OutputCopy
# yes
# 1 1
# Note
# Sample 1. You can reverse the entire array to get [1, 2, 3], which is sorted.
#
# Sample 3. No segment can be reversed such that the array will be sorted.
#
# Definitions
#
# A segment [l, r] of array a is the sequence a[l], a[l + 1], ..., a[r].
#
# If you have an array a of size n and you reverse its segment [l, r], the array will become:
#
# a[1], a[2], ..., a[l - 2], a[l - 1], a[r], a[r - 1], ..., a[l + 1], a[l], a[r + 1], a[r + 2], ..., a[n - 1], a[n].
# Solution
# C++ O(N) O(1) Two Pointers
#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> nums;
    for (int i = 0; i < n; ++i) {
        int num;
        std::cin >> num;
        nums.push_back(num);
    }
    int start = 0, end = 0;
    int left = 0;
    bool isSeen = false;
    bool isValid = true;
    bool hasBeen = false;
    for (int right = 1; right < n; ++right) {
        if (nums[left] > nums[right]) {
            if (hasBeen) {
                isValid = false;
                break;
            }
            if (!isSeen) {
                isSeen = true;
                start = left;
            }
        } else if (isSeen && nums[left] < nums[right]) {
            if (nums[start] > nums[right]) {
                isValid = false;
                break;
            }
            isSeen = false;
            hasBeen = true;
            end = left;
        }
        ++left;
    }
    if (isSeen) {
        end = n - 1;
    }
    if (start > 0 && nums[end] < nums[start - 1]) {
        isValid = false;
    }
    if (isValid) {
        std::cout << "yes" << std::endl;
        std::cout << start + 1 << " " << end + 1 << std::endl;
    } else {
        std::cout << "no" << std::endl;
    }
}

# Python O(N) O(1) Two Pointers
import sys

def solution(n: int, nums: list) -> None:
    start: int = 0
    end: int = 0
    left: int = 0
    is_seen: bool = False
    has_been: bool = False
    is_valid: bool = True
    for right in range(1, n):
        if nums[left] > nums[right]:
            if has_been:
                is_valid = False
                break
            if not is_seen:
                is_seen = True
                start = left
        elif is_seen and nums[left] < nums[right]:
            if nums[start] > nums[right]:
                is_valid = False
                break
            has_been = True
            is_seen = False
            end = left
        left += 1
    if is_seen:
        end = n - 1
    if start > 0 and nums[end] < nums[start - 1]:
        is_valid = False
    if is_valid:
        sys.stdout.write('yes\n')
        sys.stdout.write(f'{start + 1} {end + 1}')
    else:
        sys.stdout.write('no\n')


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    nums: list = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(n, nums)