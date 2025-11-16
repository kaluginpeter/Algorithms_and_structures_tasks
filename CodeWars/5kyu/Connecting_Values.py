# Given a two-dimensional array of non negative integers arr, a value val, and a coordinate coord in the form (row, column), return an iterable (depending on the language) of all of the coordinates that contain the given value and are connected to the original coordinate by the given value. Connections may be made horizontally, vertically, and diagonally. If the value of arr at coord is not equal to val, return an empty iterable. The coordinates must include the original coordinate and may be in any order.
#
# Examples:
# With the following array:
#
#     [1,0,2,0,2,1]
#     [1,0,2,1,5,7]
#     [4,1,1,0,1,9]
# With val 1 and coord (0, 0), the output should contain (the order doesn't matter and the actual data structure depends on the language):
#
# [(2, 4), (2, 1), (0, 0), (2, 2), (1, 0), (1, 3)]
# With value 2 and coord (0,  2):
#
# [(0, 2), (1, 2)]
# With value 0 and coord (0, 0), the output should be empty.
#
# ArraysAlgorithms
# Solution
Coord = tuple[int,int]
moves: list[Coord] = [
    (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)
]

def connected_values(arr: list[list[int]], val: int, coord: Coord) -> set[Coord]:
    output: set[Coord] = set()
    if arr[coord[0]][coord[1]] != val: return output
    n: int = len(arr)
    m: int = len(arr[0])
    cur_nodes: list[Coord] = [coord]
    next_nodes: list[Coord] = []
    seen: set[Coord] = set()
    while cur_nodes:
        for i, j in cur_nodes:
            output.add((i, j))
            for x, y in moves:
                r: int = i + x
                c: int = j + y
                if not (0 <= r < n) or not (0 <= c < m) or arr[r][c] != val or (r, c) in seen:
                    continue
                seen.add((r, c))
                next_nodes.append((r, c))
        cur_nodes = next_nodes
        next_nodes = []
    return output