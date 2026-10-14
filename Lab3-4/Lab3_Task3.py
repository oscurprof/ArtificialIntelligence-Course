# Lab 3 - Lab Task 3: Nodes visited, BFS vs DFS on Romania map

edges = [
    ("Arad", "Zerind", 75), ("Arad", "Sibiu", 140), ("Arad", "Timisoara", 118),
    ("Zerind", "Oradea", 71), ("Oradea", "Sibiu", 151),
    ("Sibiu", "Fagaras", 99), ("Sibiu", "Rimnicu Vilcea", 80),
    ("Timisoara", "Lugoj", 111), ("Lugoj", "Mehadia", 70),
    ("Mehadia", "Drobeta", 75), ("Drobeta", "Craiova", 120),
    ("Craiova", "Rimnicu Vilcea", 146), ("Craiova", "Pitesti", 138),
    ("Rimnicu Vilcea", "Pitesti", 97),
    ("Fagaras", "Bucharest", 211), ("Pitesti", "Bucharest", 101),
    ("Bucharest", "Giurgiu", 90), ("Bucharest", "Urziceni", 85),
    ("Urziceni", "Hirsova", 98), ("Hirsova", "Eforie", 86),
    ("Urziceni", "Vaslui", 142), ("Vaslui", "Iasi", 92), ("Iasi", "Neamt", 87),
]

romania = {}   # city -> list of (neighbour, distance)
for a, b, d in edges:
    romania.setdefault(a, []).append((b, d))
    romania.setdefault(b, []).append((a, d))

def dfs_count(graph, start, goal):
    visited, stack, seen = [], [start], set()
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        visited.append(node)
        if node == goal:
            return len(visited)
        for nbr, _ in reversed(graph[node]):
            if nbr not in seen:
                stack.append(nbr)
    return None

def bfs_count(graph, start, goal):
    visited, queue, seen = [], [start], {start}
    while queue:
        node = queue.pop(0)
        visited.append(node)
        if node == goal:
            return len(visited)
        for nbr, _ in graph[node]:
            if nbr not in seen:
                seen.add(nbr)
                queue.append(nbr)
    return None

bfs_better = dfs_better = None
for s in romania:
    for g in romania:
        if s == g:
            continue
        b, d = bfs_count(romania, s, g), dfs_count(romania, s, g)
        if bfs_better is None and b < d:
            bfs_better = (s, g, b, d)
        if dfs_better is None and b > d:
            dfs_better = (s, g, b, d)

print("BFS visits FEWER nodes than DFS:")
print("  start=%s goal=%s  BFS=%d  DFS=%d" % bfs_better)
print("BFS visits MORE nodes than DFS:")
print("  start=%s goal=%s  BFS=%d  DFS=%d" % dfs_better)
