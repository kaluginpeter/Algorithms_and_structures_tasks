# Design a special dictionary that searches the words in it by a prefix and a suffix.
#
# Implement the WordFilter class:
#
# WordFilter(string[] words) Initializes the object with the words in the dictionary.
# f(string pref, string suff) Returns the index of the word in the dictionary, which has the prefix pref and the suffix suff. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.
#
#
# Example 1:
#
# Input
# ["WordFilter", "f"]
# [[["apple"]], ["a", "e"]]
# Output
# [null, 0]
# Explanation
# WordFilter wordFilter = new WordFilter(["apple"]);
# wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".
#
#
# Constraints:
#
# 1 <= words.length <= 104
# 1 <= words[i].length <= 7
# 1 <= pref.length, suff.length <= 7
# words[i], pref and suff consist of lowercase English letters only.
# At most 104 calls will be made to the function f.
# Solution
# Python Trie HashMap
# General idea
# Insert by the way: word + separator + word slicing by one letter from left to right until we reach separator
#
# Complexity
# Time complexity: O(N * L**2)
#
# Space complexity: O(N * L**2)
class TrieNode:
    def __init__(self) -> None:
        self.childrens: dict[str, TrieNode] = dict()
        self.is_end_of_word: bool = False
        self.idx: int = -1


class Trie:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def insert_word(self, word: str, idx: int) -> None:
        current_node: TrieNode = self.root
        for char in word:
            if char not in current_node.childrens:
                current_node.childrens[char] = TrieNode()
            current_node = current_node.childrens[char]
        current_node.is_end_of_word = True
        current_node.idx = idx

    def all_words_from_this_node(
            self, current_node: TrieNode, start_path: str,
            matched_words: list[tuple[str, int]]
    ) -> None:
        if current_node.is_end_of_word:
            matched_words.append((start_path, current_node.idx))
        for next_node in current_node.childrens:
            self.all_words_from_this_node(current_node.childrens[next_node], start_path + next_node, matched_words)

    def all_mathcing_by_pattern(self, pattern: str) -> list[str]:
        path: str = ''
        current_node: TrieNode = self.root
        current_node_char: str = ''
        for char in pattern:
            if char not in current_node.childrens:
                return []
            path += char
            current_node = current_node.childrens[char]
            current_node_char = char
        valid_words: list[tuple[str, int]] = []
        self.all_words_from_this_node(current_node, path, valid_words, )
        return valid_words


class WordFilter:

    def __init__(self, words: List[str]):
        self.trie: Trie = Trie()
        for idx in range(len(words)):
            word: str = words[idx] + '{' + words[idx]
            for bound in range(len(words[idx])):
                self.trie.insert_word(word[bound:], idx)

    def f(self, pref: str, suff: str) -> int:
        pattern: str = suff + '{' + pref
        matched_by_pattern: list[tuple[str, int]] = self.trie.all_mathcing_by_pattern(pattern)
        answer_idx: int = -1
        for slot in matched_by_pattern:
            answer_idx = max(answer_idx, slot[1])
        return answer_idx

# Python
# General idea
# Insert in the first trie all words, then choose only that match with prefix, then create second trie and add all matched word in reverse order. Then choose only that match by suffix and choose largest possible index from them
#
# Complexity
# Time complexity: O(N * L + M * L)
#
# Space complexity: O(N * L + M * L)
class TrieNode:
    def __init__(self) -> None:
        self.childrens: dict[str, TrieNode] = dict()
        self.is_end_of_word: bool = False
        self.idx: int = -1


class Trie:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def insert_word(self, word: str, idx: int) -> None:
        current_node: TrieNode = self.root
        for char in word:
            if char not in current_node.childrens:
                current_node.childrens[char] = TrieNode()
            current_node = current_node.childrens[char]
        current_node.is_end_of_word = True
        current_node.idx = idx

    def all_words_from_this_node(
            self, current_node: TrieNode, start_path: str,
            matched_words: list[tuple[str, int]], bound: str, current_node_char: str
    ) -> None:
        if current_node.is_end_of_word and current_node_char == bound:
            matched_words.append((start_path, current_node.idx))
        for next_node in current_node.childrens:
            self.all_words_from_this_node(current_node.childrens[next_node], start_path + next_node, matched_words,
                                          bound, next_node)

    def all_mathcing_by_pattern(self, pattern: str, bound: str) -> list[str]:
        path: str = ''
        current_node: TrieNode = self.root
        current_node_char: str = ''
        for char in pattern:
            if char not in current_node.childrens:
                return []
            path += char
            current_node = current_node.childrens[char]
            current_node_char = char
        valid_words: list[tuple[str, int]] = []
        self.all_words_from_this_node(current_node, path, valid_words, bound, current_node_char)
        return valid_words


class WordFilter:

    def __init__(self, words: List[str]):
        self.trie: Trie = Trie()
        for idx in range(len(words)):
            self.trie.insert_word(words[idx], idx)

    def f(self, pref: str, suff: str) -> int:
        matched_by_prefix: list[tuple[str, int]] = self.trie.all_mathcing_by_pattern(pref, suff[-1])
        second_trie: Trie = Trie()
        for slot in matched_by_prefix:
            word, idx = slot
            second_trie.insert_word(word[::-1], idx)
        matched_by_suffix: list[tuple[str, int]] = second_trie.all_mathcing_by_pattern(suff[::-1], pref[0])
        answer_idx: int = -1
        for slot in matched_by_suffix:
            answer_idx = max(answer_idx, slot[1])
        return answer_idx

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)