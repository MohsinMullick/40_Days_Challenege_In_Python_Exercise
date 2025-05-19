"""
8. Game of Life (Hard)
a. Description: Implement Conway’s Game of Life on an m x n board using
for loops.
b. Example: Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]] →
Output: Next state
c. Relevance: Tests grid processing with loops.
"""
def game_of_life(board):
    rows = len(board)
    cols = len(board[0])

    # Create a copy of the board to store the next state
    next_state = [[0 for _ in range(cols)] for _ in range(rows)]

    # Directions for the 8 neighbors
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for r in range(rows):
        for c in range(cols):
            live_neighbors = 0

            # Count live neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] == 1:
                        live_neighbors += 1

            # Apply the Game of Life rules
            if board[r][c] == 1:
                if live_neighbors == 2 or live_neighbors == 3:
                    next_state[r][c] = 1  # Survives
                else:
                    next_state[r][c] = 0  # Dies
            else:
                if live_neighbors == 3:
                    next_state[r][c] = 1  # Reproduction

    # Copy next_state back to board (in-place update)
    for r in range(rows):
        for c in range(cols):
            board[r][c] = next_state[r][c]

            game_of_life(board)

            print(board)
