# Lab 3 - Lab Task 1: DFS route finding on Romania map (Arad -> Bucharest)
# Save/rename this file as DFS_REG#.py (your registration number)

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

def dfs_route(graph, start, goal):
    visited = set()
    def recurse(node, path, dist):
        visited.add(node)
        if node == goal:
            return path, dist
        for nbr, d in graph[node]:
            if nbr not in visited:
                result = recurse(nbr, path + [nbr], dist + d)
                if result:
                    return result
        return None
    return recurse(start, [start], 0)

result = dfs_route(romania, "Arad", "Bucharest")
if result:
    path, dist = result
    print("\nDFS Path       :", " -> ".join(path))
    print("Total distance :", dist, "km")
else:
    print("No path found")
