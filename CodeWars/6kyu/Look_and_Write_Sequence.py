# You are tasked with a variant of the "look-and-write" sequence. The sequence is built iteratively according to the following rules. Start with the sequence "11". After looking at the current sequence, for each digit 0–9, check how many times it appears. For every digit that occurs at least once, append its count followed by the digit to the end of the sequence. The new sequence is formed by adding all these pairs in order to the current sequence.
#
# Your task is to compute the length of the sequence after n looks on the sequence.
#
# Input: n, the number of times you look at the sequence (0 ≤ n ≤ 7*10^5) for Javascript, for Python: (0 ≤ n ≤ 2*10^5)
#
# Output: An integer representing the length of the sequence after n looks
#
# Examples:
#
# n = 1
#
# Start with "11". Then, for the first look, it’s "11" + there are two 1s, so "21". Concatenating gives "1121", and the length is 4.
#
# n = 3
#
# Start with "11". Then, for the first look, it’s "11" + there are two 1s, so "21". Concatenating gives "1121". For the second look, there are three 1s and one 2, so concatenate "1121" + "31" + "12" → "11213112". For the last look, in "11213112" there are five 1s, two 2s, and one 3, so concatenate "11213112" + "51" + "22" + "13" → "11213112512213". The length is 14.
#
# LogicMathematicsPerformance
# Solution
dp: list[list[int]] = [[0, 2, 0, 0, 0, 0, 0, 0, 0, 0]]
def look_and_write(n: int):
    while n >= len(dp):
        tmp: list[int] = dp[-1]
        new_tmp: list[int] = [0] * 10
        for i in range(10):
            if not tmp[i]: continue
            count: int = tmp[i]
            while count:
                new_tmp[count % 10] += 1
                count //= 10
            new_tmp[i] += 1 + tmp[i]
        dp.append(new_tmp)
    return sum(dp[n])