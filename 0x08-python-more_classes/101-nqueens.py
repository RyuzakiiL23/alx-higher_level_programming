#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at the specified position (row, col)
    on the board.
    """

    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col):
    """
    Solve the N Queens problem using backtracking.
    """
    if col >= N:
        print_solution(board)
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1

            solve_nqueens(board, col + 1)

            board[i][col] = 0


def print_solution(board):
    """
    Print a valid solution for the N Queens problem.
    """
    solution = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

chessboard = [[0 for _ in range(N)] for _ in range(N)]

solve_nqueens(chessboard, 0)
