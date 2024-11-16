import sys

def solution(L: int, sentence: str) -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(L), where L is length of the longest word
    """
    max_word: str = ''
    max_length: int = 0
    cur_word: list[str] = list()
    cur_length: int = 0
    for idx in range(L):
        if sentence[idx] == ' ':
            if cur_length > max_length:
                max_length = cur_length
                max_word = ''.join(cur_word)
            cur_length = 0
            cur_word.clear()
        else:
            cur_length += 1
            cur_word.append(sentence[idx])
    if cur_length > max_length:
        max_length = cur_length
        max_word = ''.join(cur_word)
    sys.stdout.write(max_word + '\n' + str(max_length) + '\n')

if __name__ == '__main__':
    L: int = int(sys.stdin.readline().rstrip())
    sentence: str = sys.stdin.readline().rstrip()
    solution(L, sentence)