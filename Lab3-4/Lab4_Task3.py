import customtkinter as ctk

# Set up CustomTkinter theme and appearance
ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")

class MazeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Maze Solver using BFS - CustomTkinter")
        self.geometry("850x550")
        self.minsize(700, 450)
        
        # Initial Maze data
        self.initial_maze = [
            "S.#.....",
            ".##.###.",
            "....#...",
            "##.##.#.",
            "...#..#.",
            ".#...##.",
            ".#.#...G",
        ]
        self.maze = [list(row) for row in self.initial_maze]
        self.rows = len(self.maze)
        self.cols = len(self.maze[0])
        
        # Configure grid layout (Left: Maze, Right: Controls & Stats)
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)
        
        # UI Frames
        self.maze_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.maze_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        self.control_frame = ctk.CTkFrame(self)
        self.control_frame.grid(row=0, column=1, padx=(0, 20), pady=20, sticky="nsew")
        
        self.create_control_widgets()
        self.create_maze_grid()
        
    def create_maze_grid(self):
        """Builds or updates the visual grid representation of the maze."""
        for widget in self.maze_frame.winfo_children():
            widget.destroy()
            
        for r in range(self.rows):
            self.maze_frame.grid_rowconfigure(r, weight=1)
            for c in range(self.cols):
                self.maze_frame.grid_columnconfigure(c, weight=1)
                
                cell_type = self.maze[r][c]
                bg_color, text_color = self.get_cell_style(cell_type)
                
                lbl = ctk.CTkLabel(
                    self.maze_frame, 
                    text=cell_type if cell_type in ('S', 'G', '*') else "", 
                    fg_color=bg_color,
                    text_color=text_color,
                    corner_radius=6,
                    font=("Helvetica", 16, "bold")
                )
                lbl.grid(row=r, column=c, padx=4, pady=4, sticky="nsew")

    def get_cell_style(self, char):
        """Returns colors for different tile types."""
        if char == '#':
            return "#1e293b", "#ffffff"  # Wall (Dark Slate)
        elif char == 'S':
            return "#2563eb", "#ffffff"  # Start (Blue)
        elif char == 'G':
            return "#16a34a", "#ffffff"  # Goal (Green)
        elif char == '*':
            return "#eab308", "#000000"  # Path (Yellow/Gold)
        else:
            return "#f1f5f9", "#000000"  # Empty tile (Light Gray)

    def create_control_widgets(self):
        """Creates the sidebar controls and action displays."""
        title_lbl = ctk.CTkLabel(self.control_frame, text="BFS Maze Solver", font=("Helvetica", 20, "bold"))
        title_lbl.pack(padx=20, pady=(20, 10))
        
        self.solve_btn = ctk.CTkButton(self.control_frame, text="Solve Maze", command=self.solve, font=("Helvetica", 14, "bold"), height=40)
        self.solve_btn.pack(padx=20, pady=10, fill="x")
        
        self.reset_btn = ctk.CTkButton(self.control_frame, text="Reset Maze", command=self.reset_maze, fg_color="#64748b", hover_color="#475569", font=("Helvetica", 14), height=40)
        self.reset_btn.pack(padx=20, pady=10, fill="x")
        
        self.stats_label = ctk.CTkLabel(self.control_frame, text="Steps: 0\nStatus: Ready", justify="left", font=("Helvetica", 13, "bold"))
        self.stats_label.pack(padx=20, pady=(15, 10), anchor="w")
        
        # Textbox for actions log
        self.actions_box = ctk.CTkTextbox(self.control_frame, font=("Courier", 12))
        self.actions_box.pack(padx=20, pady=(0, 20), fill="both", expand=True)
        self.actions_box.insert("0.0", "Actions will appear here after solving...")
        self.actions_box.configure(state="disabled")

    def solve(self):
        """Triggers the BFS solver and updates the UI."""
        cells, actions = self.solve_maze_algo()
        
        if cells is None:
            self.stats_label.configure(text="Steps: 0\nStatus: No path out!")
            self.actions_box.configure(state="normal")
            self.actions_box.delete("0.0", "end")
            self.actions_box.insert("0.0", "No path found.")
            self.actions_box.configure(state="disabled")
        else:
            self.stats_label.configure(text=f"Steps: {len(actions)}\nStatus: Solved Successfully!")
            
            # Display actions in textbox
            self.actions_box.configure(state="normal")
            self.actions_box.delete("0.0", "end")
            self.actions_box.insert("0.0", "Actions:\n" + ", ".join(actions))
            self.actions_box.configure(state="disabled")
            
            # Apply path markers to the grid
            for r, c in cells[1:-1]:
                self.maze[r][c] = '*'
            
            self.create_maze_grid()

    def reset_maze(self):
        """Resets the maze back to its initial state."""
        self.maze = [list(row) for row in self.initial_maze]
        self.create_maze_grid()
        self.stats_label.configure(text="Steps: 0\nStatus: Ready")
        self.actions_box.configure(state="normal")
        self.actions_box.delete("0.0", "end")
        self.actions_box.insert("0.0", "Actions will appear here after solving...")
        self.actions_box.configure(state="disabled")

    def solve_maze_algo(self):
        """Standard BFS algorithm implementation."""
        # Clean up any existing path stars before recalculating
        maze_copy = [row.replace('*', '.') for row in ["".join(r) for r in self.maze]]
        
        rows, cols = len(maze_copy), len(maze_copy[0])
        start = goal = None
        for r in range(rows):
            for c in range(cols):
                if maze_copy[r][c] == 'S':
                    start = (r, c)
                elif maze_copy[r][c] == 'G':
                    goal = (r, c)

        moves = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]
        frontier = [start]
        parent = {start: (None, None)}
        
        while frontier:
            r, c = frontier.pop(0)
            if (r, c) == goal:
                cells, actions = [], []
                cur = goal
                while cur is not None:
                    cells.append(cur)
                    prev, act = parent[cur]
                    if act:
                        actions.append(act)
                    cur = prev
                return cells[::-1], actions[::-1]
                
            for dr, dc, name in moves:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols
                        and maze_copy[nr][nc] != '#' and (nr, nc) not in parent):
                    parent[(nr, nc)] = ((r, c), name)
                    frontier.append((nr, nc))
                    
        return None, None

if __name__ == "__main__":
    app = MazeApp()
    app.mainloop()