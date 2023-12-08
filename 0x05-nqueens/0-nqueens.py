#!/usr/bin/python3
"""N Queens"""
import sys


def print_board(board, n):
    """Print allocated positions of the queens on the board"""
    positions = []

    for i in range(n):
        queen_row = i
        queen_column = board[i]
        positions.append([queen_row, queen_column])

    print(positions)

def is_position_safe(board, row, column, n):
    """Check if the position is safe for a queen"""
    for i in range(row):
        if board[i] == column or board[i] - i == column - row or board[i] + i == column + row:
            return False
    return True

