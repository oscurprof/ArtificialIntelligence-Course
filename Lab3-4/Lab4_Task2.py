# Lab 4 - Lab Task 2: BFS route finding on Romania map (Arad -> Bucharest)

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

print("Graph (adjacency list):")
for city, nbrs in romania.items():
    print(f"  {city:15s} -> {nbrs}")

def bfs_route(graph, start, goal):
    frontier = [start]
    parent = {start: None}
    cost = {start: 0}
    while frontier:
        node = frontier.pop(0)
        if node == goal:
            path = []
            n = node
            while n is not None:
                path.append(n)
                n = parent[n]
            return path[::-1], cost[goal]
        for nbr, d in graph[node]:
            if nbr not in parent:
                parent[nbr] = node
                cost[nbr] = cost[node] + d
                frontier.append(nbr)
    return None, None

path, dist = bfs_route(romania, "Arad", "Bucharest")
print("\nBFS Path       :", " -> ".join(path))
print("Total distance :", dist, "km")
