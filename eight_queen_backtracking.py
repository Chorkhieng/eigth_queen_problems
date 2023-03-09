import time


def is_safe(board, row, col):
    """Check if it is safe to place a queen at board[row][col]"""
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # If it passes all the checks, return True
    return True


def solve(board, col, steps):
    """Solve 8-Queens problem with backtracking"""
    steps[0] += 1 # increment step counter
    # Base case: If all queens are placed, return True
    if col >= len(board):
        return True
    # Recursive case
    for row in range(len(board)):
        if is_safe(board, row, col):
            # Place the queen at board[row][col]
            board[row][col] = 1
            # Recurse to place the rest of the queens
            if solve(board, col+1, steps):
                return True
            # Backtrack: remove the queen and try the next row
            board[row][col] = 0
    # If no solution found, return False
    return False


# Main function
if __name__ == '__main__':
    # Create an empty board
    board = [[0 for _ in range(8)] for _ in range(8)]
    # Solve the 8-Queens problem
    steps = [0] # Initialize step counter
    start_time = time.time() # Start timer
    if solve(board, 0, steps):
        # Print the solution and steps
        print("Solution:")
        for row in board:
            print(row)
        print(f"Number of steps: {steps[0]}")
    else:
        print("No solution found")
    end_time = time.time() # End timer
    print(f"Runtime: {end_time - start_time} seconds")
