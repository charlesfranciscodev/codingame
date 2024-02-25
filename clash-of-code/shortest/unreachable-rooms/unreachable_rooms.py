from collections import deque


def find_unreachable_rooms(n, keys):
    graph = {i: set(keys[i]) for i in range(n)}
    visited = set([0])
    queue = deque([0])

    while queue:
        room = queue.popleft()
        for key in graph[room]:
            if key not in visited:
                visited.add(key)
                queue.append(key)

    unreachable_rooms = n - len(visited)
    return unreachable_rooms


# Read input
n = int(input())
keys = [list(map(int, input().split())) for _ in range(n)]

# Call the function and print the result
unreachable_rooms = find_unreachable_rooms(n, keys)
print(unreachable_rooms)
