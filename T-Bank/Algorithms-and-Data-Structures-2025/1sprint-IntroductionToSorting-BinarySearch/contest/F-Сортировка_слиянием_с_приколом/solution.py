import sys

def merge_and_count(arr: list[int], temp_arr: list[int], left: int, mid: int, right: int) -> int:
    i: int = left
    j: int = mid + 1
    k: int = left
    inv_count: int = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1
    while i <= mid:
        temp_arr[k] = arr[i] 
        i += 1
        k += 1
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
    return inv_count

def merge_sort_and_count(arr: list[int], temp_arr: list[int], left: int, right: int) -> int:
    inv_count: int = 0
    if left < right:
        mid: int = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count

def solution() -> None:
    """
    Time Complexity O(NlogN)
    Memory Complexity O(N + logN)"""
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    temp_arr: list[int] = [0] * n
    inv_count = merge_sort_and_count(nums, temp_arr, 0, n - 1)
    
    sys.stdout.write(f"{inv_count}\n")
    sys.stdout.write(' '.join(map(str, nums)) + '\n')

if __name__ == '__main__':
    solution()
