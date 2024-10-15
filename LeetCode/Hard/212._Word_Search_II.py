# Given an m x n board of characters and a list of strings words, return all words on the board.
#
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
#
#
# Example 1:
#
#
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# Example 2:
#
#
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
#
#
# Constraints:
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 104
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
# Solution
# Python O(NM4**L) O(MN) Backtracking Trie
class TrieNode:
    def __init__(self) -> None:
        self.childrens: dict[str, TrieNode] = dict()
        self.is_end_of_word: bool = False

class Trie:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def insert_word(self, word: str) -> None:
        current_node: TrieNode = self.root
        for char in word:
            if char not in current_node.childrens:
                current_node.childrens[char] = TrieNode()
            current_node = current_node.childrens[char]
        current_node.is_end_of_word = True

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie: Trie = Trie()
        board_char_count: set[str] = set()
        for row in board:
            for char in row:
                board_char_count.add(char)
        valid_words: list[str] = [
            word for word in words if all(char in board_char_count for char in word)
        ]
        for word in valid_words:
            trie.insert_word(word)
        output: list[str] = []
        rows, cols = len(board), len(board[0])
        visited: set[str] = set()
        def backtrack(row: int, col: int, node: TrieNode, path: str) -> None:
            if (
                not (0 <= row < len(board))
                or not (0 <= col < len(board[0]))
                or (row, col) in visited
                or board[row][col] not in node.childrens
            ):
                return
            node: TrieNode = node.childrens[board[row][col]]
            path += board[row][col]

            if node.is_end_of_word:
                output.append(path)
                node.is_end_of_word = False

            visited.add((row, col))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                backtrack(row + dx, col + dy, node, path)
            visited.remove((row, col))

        for row in range(rows):
            for col in range(cols):
                backtrack(row, col, trie.root, '')
        return output