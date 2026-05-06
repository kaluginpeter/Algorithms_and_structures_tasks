# Mirrored Exponential Chunks
# Using a single function provided with an array, create a new one in the following ways:
#
# Separate array elements into chunks. Each chunk will contain 2^abs(n) elements where n is the "distance" to the median chunk.
# The median chunk(s) will have one single element, or will not appear in the output if there is some ambiguity about it.
# If an outlying chunk does not have enough elements to reach the 2^abs(n) requirement, it will contain as many elements as remain.
# Chuncks in mirrored places (compared to the median chunk) should be of the same length.
# You must maintain original element order within each chunk.
# You must maintain original element order from chunk to chunk.
# Example Input/Solution:
#
# input:    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
# solution: [[1,2,3,4,5,6,7,8],[9,10,11,12],[13,14],[15],[16,17],[18,19,20,21],[22,23,24,25,26,27,28,29]]
# ArraysAlgorithms
# Solution
def mirrored_exponential_chunks(arr):
    n = len(arr)
    res = []
    if n % 2 == 1:
        mid = n // 2
        res = [[arr[mid]]]
        left = mid
        right = mid + 1
        step = 1
    else:
        left = n // 2
        right = left
        res = []
        step = 1
    chunks = []
    while left > 0 or right < n:
        size = 2 ** step
        l_start = max(0, left - size)
        left_chunk = arr[l_start:left]
        r_end = min(n, right + size)
        right_chunk = arr[right:r_end]
        if left_chunk: chunks.insert(0, left_chunk)
        if right_chunk: chunks.append(right_chunk)
        left = l_start
        right = r_end
        step += 1
    return chunks[:len(chunks)//2] + res + chunks[len(chunks)//2:]