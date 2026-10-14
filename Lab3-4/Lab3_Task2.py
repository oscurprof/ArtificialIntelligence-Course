# Lab 3 - Lab Task 2: Boggle (find all dictionary words on the board)
board = [
    ['M', 'S', 'E', 'F'],
    ['R', 'A', 'T', 'D'],
    ['L', 'O', 'N', 'E'],
    ['K', 'A', 'F', 'B'],
]
dictionary = ["START", "NOTE", "SAND", "STONED"]

def boggle(board, words):
    rows, cols = len(board), len(board[0])
    word_set = set(words)
    prefixes = {w[:i] for w in words for i in range(1, len(w) + 1)}
    found = set()
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def dfs(r, c, current, used):
        current += board[r][c]
        if current not in prefixes:
            return
        if current in word_set:
            found.add(current)
        used.add((r, c))
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in used:
                dfs(nr, nc, current, used)
        used.remove((r, c))

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, "", set())
    return found

print("Valid words:", sorted(boggle(board, dictionary)))
