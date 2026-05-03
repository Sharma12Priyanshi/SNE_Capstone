from collections import deque

def bfs_shortest_path(graph, start, end):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return []

def dfs_depth(graph, start, depth):
    result = []
    visited = set()

    def dfs(node, current_depth):
        if current_depth > depth:
            return
        visited.add(node)
        result.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, current_depth + 1)

    dfs(start, 0)
    return result