import heapq

def get_maze_data():
    """
    Defines the grid nodes (A through Y) and their coordinates on a 6x6 grid,
    along with valid connections based on up/down/left/right traversals.
    """
    nodes = {
        'A': (0, 0), 'B': (2, 0), 'C': (3, 0), 'D': (4, 0), 'E': (5, 0),
        'F': (0, 1), 'G': (2, 1),
        'H': (0, 2), 'I': (1, 2), 'J': (2, 2), 'K': (4, 2), 'L': (5, 2),
        'M': (0, 3), 'N': (1, 3), 'O': (3, 3), 'P': (4, 3), 'Q': (5, 3),
        'R': (0, 4), 'S': (1, 4), 'T': (2, 4), 'U': (3, 4), 'V': (5, 4),
        'W': (2, 5), 'X': (4, 5), 'Y': (5, 5)
    }
    
    graph = {
        'A': ['F'],
        'B': ['C', 'G'],
        'C': ['B', 'D'],
        'D': ['C', 'E'],
        'E': ['D'],
        'F': ['A', 'H'],
        'G': ['B', 'J'],
        'H': ['F', 'I', 'M'],
        'I': ['H', 'N'],
        'J': ['G'],
        'K': ['L', 'P'],
        'L': ['K', 'Q'],
        'M': ['H', 'N', 'R'],
        'N': ['M', 'I', 'S'],
        'O': ['P', 'U'],
        'P': ['O', 'Q', 'K'],
        'Q': ['P', 'L', 'V'],
        'R': ['M', 'S'],
        'S': ['N', 'R', 'T'],
        'T': ['S', 'U', 'W'],
        'U': ['T', 'O'],
        'V': ['Q', 'Y'],
        'W': ['T'],
        'X': [],
        'Y': ['V']
    }
    return nodes, graph

def manhattan_distance(node1, node2, nodes):
    """Calculates Manhattan distance h(n) = |x1 - x2| + |y1 - y2|."""
    x1, y1 = nodes[node1]
    x2, y2 = nodes[node2]
    return abs(x1 - x2) + abs(y1 - y2)

def robot_maze_astar(start, goal):
    """
    Performs A* Search on the maze graph with unit edge cost (g = 1 per move).
    """
    nodes, graph = get_maze_data()
    
    open_list = []
    # Priority queue stores tuples: (f_cost, g_cost, current_node)
    h_start = manhattan_distance(start, goal, nodes)
    heapq.heappush(open_list, (h_start, 0, start))
    
    g_cost = {start: 0}
    parent = {start: None}
    closed_set = set()
    
    print(f"\nNavigating robot maze from Start '{start}' to Goal '{goal}' using A*...")
    print("-" * 65)
    print(f"{'Node':<8} | {'g(n)':<5} | {'h(n)':<5} | {'f(n)':<5} | {'Coordinates (x,y)'}")
    print("-" * 65)
    
    while open_list:
        f, g, current = heapq.heappop(open_list)
        
        if current in closed_set:
            continue
            
        h = manhattan_distance(current, goal, nodes)
        print(f"{current:<8} | {g:<5} | {h:<5} | {f:<5} | {nodes[current]}")
        
        if current == goal:
            path = []
            curr = goal
            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            path.reverse()
            return path, g, nodes
            
        closed_set.add(current)
        
        for neighbor in graph.get(current, []):
            if neighbor in closed_set:
                continue
                
            new_g = g + 1
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                h_neighbor = manhattan_distance(neighbor, goal, nodes)
                new_f = new_g + h_neighbor
                parent[neighbor] = current
                heapq.heappush(open_list, (new_f, new_g, neighbor))
                
    return None, float('inf'), nodes

def main():
    print("=" * 65)
    print("Lab 6 Task 3: Robot Maze Navigation Using A* Search")
    print("=" * 65)
    
    start = 'A'
    goal = 'Y'
    
    path, total_cost, nodes = robot_maze_astar(start, goal)
    
    print("-" * 65)
    if path:
        print("\nSUCCESS: Robot successfully navigated out of the maze!")
        print(f"Path Sequence (Nodes): {' -> '.join(path)}")
        
        coord_path = [nodes[node] for node in path]
        print(f"Path Sequence (Coordinates): {coord_path}")
        print(f"Total Path Cost: {total_cost}")
    else:
        print("No path found out of the maze.")
    print("=" * 65)

if __name__ == "__main__":
    main()