import heapq

def is_solvable(state_flat):
    inversions = 0
    flat_no_zero = [tile for tile in state_flat if tile != 0]
    n = len(flat_no_zero)
    for i in range(n):
        for j in range(i + 1, n):
            if flat_no_zero[i] > flat_no_zero[j]:
                inversions += 1
    return inversions % 2 == 0

def calculate_heuristic(state, goal_state):
    misplaced = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0 and tile != goal_state[i][j]:
                misplaced += 1
    return misplaced

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return None

def get_successors(state):
    successors = []
    r, c = find_blank(state)
    directions = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]
    
    for dr, dc, move in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_state = [list(row) for row in state]
            new_state[r][c], new_state[nr][nc] = new_state[nr][nc], new_state[r][c]
            tuple_state = tuple(tuple(row) for row in new_state)
            successors.append((tuple_state, move))
            
    return successors

def gbfs_8puzzle(start_state, goal_state):
    start_tuple = tuple(tuple(row) for row in start_state)
    goal_tuple = tuple(tuple(row) for row in goal_state)
    
    h_start = calculate_heuristic(start_tuple, goal_tuple)
    open_list = []
    heapq.heappush(open_list, (h_start, start_tuple, [start_tuple], []))
    
    visited = set()
    explored_nodes = 0
    
    while open_list:
        h, current_state, path, moves = heapq.heappop(open_list)
        
        if current_state in visited:
            continue
            
        visited.add(current_state)
        explored_nodes += 1
        
        if current_state == goal_tuple:
            return path, moves, explored_nodes
            
        for next_state, move in get_successors(current_state):
            if next_state not in visited:
                h_next = calculate_heuristic(next_state, goal_tuple)
                heapq.heappush(open_list, (h_next, next_state, path + [next_state], moves + [move]))
                
    return None, None, explored_nodes

def print_board(state):
    for row in state:
        print(" ".join([str(x) if x != 0 else "_" for x in row]))

def main():
    print("=" * 60)
    print("Task 3: 8-Puzzle Solver with Solvability Check & User Input")
    print("=" * 60)
    
    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    print("Enter the initial state as 9 numbers (0-8, where 0 is blank),")
    print("separated by spaces or commas (e.g., '1 2 3 4 6 5 7 0 8').")
    user_input = input("Enter start state (or press Enter to use default): ").strip()
    
    if not user_input:
        start_state = [
            [1, 2, 3],
            [4, 6, 5],
            [7, 0, 8]
        ]
        print("Using default start state.")
    else:
        try:
            nums = [int(x) for x in user_input.replace(',', ' ').split()]
            if len(nums) != 9 or set(nums) != set(range(9)):
                raise ValueError("Exactly numbers 0 through 8 required.")
            start_state = [nums[0:3], nums[3:6], nums[6:9]]
        except Exception as e:
            print(f"Invalid input ({e}). Using default start state.")
            start_state = [
                [1, 2, 3],
                [4, 6, 5],
                [7, 0, 8]
            ]
            
    print("\nInitial State:")
    print_board(start_state)
    
    flat_state = [tile for row in start_state for tile in row]
    solvable = is_solvable(flat_state)
    
    print("-" * 60)
    if not solvable:
        print("RESULT: The puzzle configuration is NOT SOLVABLE!")
        print("Reason: Inversion count is odd.")
        print("=" * 60)
        return
    else:
        print("RESULT: The puzzle configuration is SOLVABLE.")
        print("=" * 60)
        
    print("\nRunning Greedy Best-First Search...")
    path, moves, total_explored = gbfs_8puzzle(start_state, goal_state)
    
    if path:
        print("\nSOLUTION FOUND!")
        print(f"Total Steps in Solution: {len(moves)}")
        print(f"Total States Explored: {total_explored}")
        print(f"Move Sequence: {moves}")
        print("\nStep-by-Step State Transitions:")
        for idx, state in enumerate(path):
            print(f"\nStep {idx}:")
            print_board(state)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()