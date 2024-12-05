#include <vector>
#include <cassert>

using Iterator = std::vector<int>::iterator;
using CIterator = std::vector<int>::const_iterator;

std::vector<int> merge(
    CIterator left_begin, CIterator left_end,
    CIterator right_begin, CIterator right_end) {

    std::vector<int> merged;
    CIterator left_it = left_begin;
    CIterator right_it = right_begin;
    while (left_it != left_end && right_it != right_end) {
        if (*left_it <= *right_it) {
            merged.push_back(*left_it);
            ++left_it;
        } else {
            merged.push_back(*right_it);
            ++right_it;
        }
    }
    while (left_it != left_end) {
        merged.push_back(*left_it);
        ++left_it;
    }
    while (right_it != right_end) {
        merged.push_back(*right_it);
        ++right_it;
    }

    return merged;
}

void merge_sort(Iterator begin, Iterator end) {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    */
    if (end - begin > 1) {
        Iterator mid = begin + (end - begin) / 2;
        merge_sort(begin, mid);
        merge_sort(mid, end);
        std::vector<int> merged = merge(begin, mid, mid, end);
        std::copy(merged.begin(), merged.end(), begin);
    }
}

void test_merge_sort() {
	std::vector<int> a = {1, 4, 9};
	std::vector<int> b = {2, 10, 11};
	std::vector<int> c = merge(a.cbegin(), a.cend(), b.cbegin(), b.cend());
	std::vector<int> expected = {1, 2, 4, 9, 10, 11};
	assert(c == expected);
	std::vector<int> d = {1, 4, 2, 10, 1, 2};
	std::vector<int> sorted = {1, 1, 2, 2, 4, 10};
	merge_sort(d.begin(), d.end());
	assert(d == sorted);
}
