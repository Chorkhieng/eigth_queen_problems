import random
import math
import time


def is_attacking(row1, col1, row2, col2):
    """Check if two queens are attacking each other"""
    return row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2)


def count_attacking_pairs(board):
    """Count the number of attacking pairs of queens on the board"""
    count = 0
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            if is_attacking(i, board[i], j, board[j]):
                count += 1
    return count


def get_random_move(board):
    """Generate a random move to change the current board state"""
    col = random.randint(0, len(board)-1)
    row = random.randint(0, len(board)-1)
    return col, row


def get_best_move(board, temperature):
    """Find the best move to improve the current board state, based on the temperature"""
    current_score = count_attacking_pairs(board)
    best_moves = []
    for col in range(len(board)):
        for row in range(len(board)):
            if board[row] != col:
                board_copy = board.copy()
                board_copy[col] = row
                new_score = count_attacking_pairs(board_copy)
                if new_score < current_score:
                    best_moves = [(row, col)]
                    current_score = new_score
                elif new_score == current_score:
                    best_moves.append((row, col))
                else:
                    # calculate probability of selecting worse move
                    delta_E = new_score - current_score
                    probability = math.exp(-delta_E / temperature)
                    if random.random() < probability:
                        best_moves.append((row, col))
    if len(best_moves) > 0:
        return random.choice(best_moves)
    else:
        return None


def solve(board, max_temperature, cooling_rate):
    """Solve 8-Queens problem with Simulated Annealing"""
    steps = 0
    temperature = max_temperature
    while temperature > 0:
        steps += 1
        move = get_best_move(board, temperature)
        if move is None:
            break
        board[move[1]] = move[0]
        temperature *= cooling_rate
        if count_attacking_pairs(board) == 0:
            return board, steps
    return None


# Main function
if __name__ == '__main__':
    # Create an empty board
    board = [random.randint(0, 7) for _ in range(8)]
    # Solve the 8-Queens problem with Simulated Annealing
    start_time = time.time() # Start timer
    solution, steps = solve(board, max_temperature=100, cooling_rate=0.95)
    end_time = time.time() # End timer
    if solution is not None:
        # Convert the solution to a list of lists
        solution_matrix = [[0 for _ in range(len(solution))] for _ in range(len(solution))]
        for i in range(len(solution)):
            solution_matrix[solution[i]][i] = 1
        # Print the solution and steps
        print("Solution:")
        for row in solution_matrix:
            print(row)
        print(f"Number of steps: {steps}")
    else:
        print("No solution found")
    print(f"Runtime: {(end_time - start_time) * 1000} miliseconds")
