import time

def is_valid_solution(board):
    for i in range(8):
        for j in range(i + 1, 8):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                return False
    return True
    
def brute_force():
    start_time = time.time()
    steps = 0
    for i in range(8):
        for j in range(8):
            for k in range(8):
                for l in range(8):
                    for m in range(8):
                        for n in range(8):
                            for o in range(8):
                                for p in range(8):
                                    board = [i, j, k, l, m, n, o, p]
                                    steps += 1
                                    if is_valid_solution(board):
                                        end_time = time.time()
                                        print(f"Runtime: {(end_time - start_time) * 1000} miliseconds")
                                        print(f"Number of steps: {steps}")
                                        print("Solution:")
                                        for row in range(8):
                                            print([1 if board[row] == col else 0 for col in range(8)])
                                        return board
    print("No solution found.")
    return None
    
if __name__ == "__main__":
    brute_force()