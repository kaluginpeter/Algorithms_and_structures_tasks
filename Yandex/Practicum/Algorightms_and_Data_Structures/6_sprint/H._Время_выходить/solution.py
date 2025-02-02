import sys


def solution() -> None:
    """
    Time Complexity O(V + E)
    Memory Complexity O(V + E)
    """
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adj_list: dict[int, list[int]] = dict()
    for _ in range(m):
        source, destination = map(int, sys.stdin.readline().rstrip().split())
        if source not in adj_list: adj_list[source] = []
        adj_list[source].append(destination)
    for vertex, edges in adj_list.items():
        edges.sort(reverse=True)
    enter: list[int] = [0] * (n + 1)
    leave: list[int] = [0] * (n + 1)
    colors: list[str] = ['white'] * (n + 1)
    call_stack: list[int] = [1]
    current_time: int = -1
    while call_stack:
        vertex = call_stack.pop()
        if colors[vertex] != 'black': current_time += 1
        if colors[vertex] == 'white':
            enter[vertex] = current_time
            colors[vertex] = 'grey'
            call_stack.append(vertex)
            for neighbor in adj_list.get(vertex, []):
                if colors[neighbor] == 'white':
                    call_stack.append(neighbor)
        elif colors[vertex] == 'grey':
            colors[vertex] = 'black'
            leave[vertex] = current_time
    for vertex in range(1, n + 1):
        sys.stdout.write(f'{enter[vertex]} {leave[vertex]}\n')


if __name__ == '__main__':
    solution()