import heapq

def get_romania_graph():
    """
    Returns the adjacency list representation of the Romania map with path costs.
    """
    return {
        'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
        'Zerind': [('Arad', 75), ('Oradea', 71)],
        'Oradea': [('Zerind', 71), ('Sibiu', 151)],
        'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
        'Timisoara': [('Arad', 118), ('Lugoj', 111)],
        'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
        'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
        'Dobreta': [('Mehadia', 75), ('Craiova', 120)],
        'Craiova': [('Dobreta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
        'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
        'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
        'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
        'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Urziceni', 85), ('Giurgiu', 90)],
        'Giurgiu': [('Bucharest', 90)],
        'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
        'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
        'Eforie': [('Hirsova', 86)],
        'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
        'Iasi': [('Vaslui', 92), ('Neamt', 87)],
        'Neamt': [('Iasi', 87)]
    }

def get_heuristic_to_bucharest():
    """
    Returns straight-line distance heuristic values (h-cost) to Bucharest.
    """
    return {
        'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242,
        'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151,
        'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
        'Oradea': 380, 'Pitesti': 10, 'Rimnicu Vilcea': 193, 'Sibiu': 253,
        'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
    }

def a_star_search(graph, heuristic, start, goal):
    """
    Performs A* Search to find the optimal path from start to goal.
    f(n) = g(n) + h(n)
    """
    open_list = []
    # Priority queue stores tuples: (f_cost, g_cost, current_node)
    h_start = heuristic[start]
    heapq.heappush(open_list, (h_start, 0, start))
    
    g_cost = {start: 0}
    parent = {start: None}
    closed_set = set()
    
    print(f"\nStarting A* Search from '{start}' to '{goal}'...")
    print("-" * 65)
    print(f"{'Node':<15} | {'g(n)':<6} | {'h(n)':<6} | {'f(n)':<6} | {'Status'}")
    print("-" * 65)
    
    while open_list:
        f, g, current = heapq.heappop(open_list)
        
        if current in closed_set:
            continue
            
        print(f"{current:<15} | {g:<6} | {heuristic[current]:<6} | {f:<6} | Expanded")
        
        if current == goal:
            # Reconstruct path
            path = []
            curr = goal
            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            path.reverse()
            return path, g
            
        closed_set.add(current)
        
        for neighbor, weight in graph[current]:
            if neighbor in closed_set:
                continue
                
            new_g = g + weight
            
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                h = heuristic[neighbor]
                new_f = new_g + h
                parent[neighbor] = current
                heapq.heappush(open_list, (new_f, new_g, neighbor))
                
    return None, float('inf')

def main():
    print("=" * 65)
    print("Lab 6 Task 1: A* Search - Romania Map (Arad to Bucharest)")
    print("=" * 65)
    
    graph = get_romania_graph()
    heuristic = get_heuristic_to_bucharest()
    
    start_node = 'Arad'
    goal_node = 'Bucharest'
    
    path, total_cost = a_star_search(graph, heuristic, start_node, goal_node)
    
    print("-" * 65)
    if path:
        print("\nSUCCESS: Optimal Path Found!")
        print(f"Path Sequence: {' -> '.join(path)}")
        print(f"Total Path Cost (g): {total_cost}")
        print("\nObservations & Improvements over Uninformed Methods:")
        print("1. Directed Exploration: A* uses heuristic guidance f(n) = g(n) + h(n),")
        print("   allowing it to focus directly towards Bucharest instead of expanding")
        print("   blindly in all directions like BFS or DFS.")
        print("2. Optimality: Unlike Greedy Best-First Search (which only looks at h(n)")
        print("   and can take suboptimal detours), A* guarantees the absolute shortest")
        print("   path because it accounts for accumulated actual cost g(n).")
    else:
        print("No path found.")
    print("=" * 65)

if __name__ == "__main__":
    main()