def merge(arr: list[int], lf: int, mid: int, rg: int) -> list[int]:
    left_part: list[int] = arr[lf:mid]
    right_part: list[int] = arr[mid:rg]
    main_idx: int = lf
    left: int = 0
    right: int = 0
    while left < len(left_part) and right < len(right_part):
        if left_part[left] <= right_part[right]:
            arr[main_idx] = left_part[left]
            left += 1
        else:
            arr[main_idx] = right_part[right]
            right += 1
        main_idx += 1
    while left < len(left_part):
        arr[main_idx] = left_part[left]
        left += 1
        main_idx += 1
    while right < len(right_part):
        arr[main_idx] = right_part[right]
        right += 1
        main_idx += 1
    return arr



def merge_sort(arr, lf, rg):
    """
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    """
    if lf < rg - 1:
        mid: int = (lf + rg) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)
        merge(arr, lf, mid, rg)

def test():
	a = [1, 4, 9, 2, 10, 11]
	b = merge(a, 0, 3, 6)
	expected = [1, 2, 4, 9, 10, 11]
	assert b == expected
	c = [1, 4, 2, 10, 1, 2]
	merge_sort(c, 0 , 6)
	expected = [1, 1, 2, 2, 4, 10]
	assert c == expected

if __name__ == '__main__':
    test()