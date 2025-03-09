from __future__ import annotations
import sys


class Trie:
    def __init__(self) -> None:
        self.tree: dict[int, Trie] = dict()
        self.words: dict[str, int] = dict()

    def insert(self, word: str) -> None:
        root: Trie = self
        acronym: str = self.get_acronym(word)
        if not acronym:
            if 91 not in root.tree:
                root.tree[91] = Trie()
                root.tree[91].words[word] = root.tree[91].words.get(word, 0) + 1
                return
        for letter in acronym:
            if ord(letter) not in root.tree:
                root.tree[ord(letter)] = Trie()
            root = root.tree[ord(letter)]
        root.words[word] = root.words.get(word, 0) + 1

    def get_acronym(self, word: str) -> str:
        return ''.join(letter for letter in word if letter.isupper())

    def fill_set(self, root: Trie, commands: list[tuple[str, int]]) -> None:
        for word, freq in root.words.items():
            commands.append((word, freq))
        for idx in range(65, 92):
            if idx not in root.tree: continue
            self.fill_set(root.tree[idx], commands)

    def print_command(self, command: str) -> None:
        root: Trie = self
        for letter in command:
            if ord(letter) not in root.tree: return
            root = root.tree[ord(letter)]
        commands: list[tuple[str, int]] = []
        self.fill_set(root, commands)
        commands.sort()
        for word, freq in commands:
            sys.stdout.write('\n'.join(word for _ in range(freq)))
            sys.stdout.write('\n')


def solution() -> None:
    """
    Time Complexity O(N + MNlog(N))
    Memory Complexity O(L)
    """
    n: int = int(sys.stdin.readline().rstrip())
    trie: Trie = Trie()
    for _ in range(n):
        word: str = sys.stdin.readline().rstrip()
        trie.insert(word)
    m: int = int(sys.stdin.readline().rstrip())
    for _ in range(m):
        command: str = sys.stdin.readline().rstrip()
        trie.print_command(command)


if __name__ == '__main__':
    solution()