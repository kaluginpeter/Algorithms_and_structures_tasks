# You are given an array books where books[i] = [thicknessi, heighti] indicates the thickness and height of the ith book. You are also given an integer shelfWidth.
#
# We want to place these books in order onto bookcase shelves that have a total width shelfWidth.
#
# We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to shelfWidth, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.
#
# Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.
#
# For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.
# Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.
#
#
#
# Example 1:
#
#
# Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4
# Output: 6
# Explanation:
# The sum of the heights of the 3 shelves is 1 + 3 + 2 = 6.
# Notice that book number 2 does not have to be on the first shelf.
# Example 2:
#
# Input: books = [[1,3],[2,4],[3,2]], shelfWidth = 6
# Output: 4
#
#
# Constraints:
#
# 1 <= books.length <= 1000
# 1 <= thicknessi <= shelfWidth <= 1000
# 1 <= heighti <= 1000
# Solution Dynamic Programming O(N**2) O(N)
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        return self.dp_books(books, shelfWidth)

    def dp_books(self, books: list[list[int]], boundary: int) -> int:
        min_heights: list[int] = [float('inf')] * (len(books) + 1)
        min_heights[0] = 0

        for book_idx in range(1, len(books) + 1):
            current_height: int = 0
            current_width: int = 0

            for prev_book in range(book_idx - 1, -1, -1):
                cur_book_width, cur_book_height = books[prev_book]

                if current_width + cur_book_width > boundary: break

                current_width += cur_book_width
                current_height = max(current_height, cur_book_height)

                min_heights[book_idx] = min(min_heights[book_idx], min_heights[prev_book] + current_height)

        return min_heights[len(books)]