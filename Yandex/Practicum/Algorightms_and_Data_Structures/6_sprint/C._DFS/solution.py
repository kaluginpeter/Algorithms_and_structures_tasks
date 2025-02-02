import sys


def dfs(source: int, adj_list: dict[int, list[int]], v: int) -> None:
    colors: list[str] = ['white'] * (v + 1)
    call_stack: list[int] = [source]
    while call_stack:
        cur_vertex = call_stack.pop()
        if colors[cur_vertex] == 'white':
            sys.stdout.write(str(cur_vertex) + ' ')
            colors[cur_vertex] = 'grey'
            call_stack.append(cur_vertex)
            for next_vertex in adj_list.get(cur_vertex, []):
                if colors[next_vertex] == 'white':
                    call_stack.append(next_vertex)
        elif colors[cur_vertex] == 'grey':
            colors[cur_vertex] = 'black'



def solution() -> None:
    """
    Time Complexity O(ElogE + (V + E))
    Memory Complexity O(V + E)
    """
    v, e = map(int, sys.stdin.readline().rstrip().split())
    adj_list: dict[int, list[int]] = dict()
    for _ in range(e):
        source, destination = map(int, sys.stdin.readline().rstrip().split())
        if source not in adj_list: adj_list[source] = []
        adj_list[source].append(destination)
        if destination not in adj_list: adj_list[destination] = []
        adj_list[destination].append(source)
    for vertex, edges in adj_list.items():
        edges.sort(reverse=True)
    start: int = int(sys.stdin.readline().rstrip())
    dfs(start, adj_list, v)


if __name__ == '__main__':
    solution()