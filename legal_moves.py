import pygame
import chess
from constants import *

def draw_legal_moves(WN: pygame.Surface, square: str, color: str, board: chess.Board, turn: int) -> list:
    # Using chess module to find legal moves based on chess.Board.legal_moves
    squares = []
    print(colors, color, turn)

    for move in board.legal_moves:
        move = str(move)  # Can't not do this because move isn't type string, but type chess.Move

        if square in move:
            print(move, end=" ")
            legal_square = move[2:]

            if len(legal_square) > 2:
                legal_square = legal_square[:2]

            squares.append(legal_square)
            print(legal_square)

    for square in squares:
        print(square, end=" ")
        x = DIF_BOARD + (files.index(square[0]) + 0.5) * square_width
        y = (8 - ranks.index(square[1]) - 0.5) * square_height + timer_height
        pygame.draw.circle(WN, CYAN, (x, y), ((square_width + square_height)/6))
        pygame.display.update()

    return squares
