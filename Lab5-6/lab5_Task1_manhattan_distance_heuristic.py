import heapq

def manhattan_distance(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def main():
    goal = (4, 4)
    positions = [(0, 0), (1, 2), (2, 3), (3, 4), (4, 4)]
    
    print("=" * 60)
    print(f"Lab Task 1: Manhattan Distance as a Heuristic (Goal = {goal})")
    print("=" * 60)
    print(f"{'Position (x,y)':<15} | {'Calculation Formula':<30} | {'h(n)':<5}")
    print("-" * 60)
    
    for pos in positions:
        x1, y1 = pos
        x2, y2 = goal
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        h_val = dx + dy
        calc_str = f"|{x2}-{x1}| + |{y2}-{y1}| = {dx} + {dy}"
        print(f"{str(pos):<15} | {calc_str:<30} | {h_val:<5}")
        
    print("-" * 60)
    
    def get_neighbors(pos):
        x, y = pos
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= 4 and 0 <= ny <= 4:
                neighbors.append((nx, ny))
        return neighbors

    start = (0, 0)
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start, goal), start))
    came_from = {start: None}
    visited = set()
    explored_order = []
    
    print("\nDemonstrating Greedy Best-First Search (GBFS) Pathfinding:")
    while open_list:
        h, current = heapq.heappop(open_list)
        if current in visited:
            continue
        visited.add(current)
        explored_order.append((current, h))
        
        if current == goal:
            break
            
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                if neighbor not in [item[1] for item in open_list]:
                    came_from[neighbor] = current
                    heapq.heappush(open_list, (manhattan_distance(neighbor, goal), neighbor))
                    
    path = []
    curr = goal
    while curr is not None:
        path.append(curr)
        curr = came_from.get(curr)
    path.reverse()
    
    print(f"Start: {start} -> Goal: {goal}")
    print("Explored Nodes Order:")
    for node, h in explored_order:
        print(f"  Node: {node}, h(n) = {h}")
        
    print(f"\nFinal Path: {path}")
    print(f"Total Path Cost (Steps): {len(path) - 1}")
    print("=" * 60)

if __name__ == "__main__":
    main()