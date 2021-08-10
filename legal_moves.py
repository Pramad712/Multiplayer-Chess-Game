import pygame
from constants import *

def draw_legal_moves(WN, square, color, board, turn):
    # Using chess module to find legal moves based on chess.Board.legal_moves
    squares = []

    if colors.index(color) + 1 == turn:
        for move in board.legal_moves:
            move = str(move)  # Can't not do this because move isn't type string, but type chess.Move
            if square in move:
                legal_square = move.replace(square, "")
                if len(legal_square) == 3:
                    legal_square = legal_square.replace(legal_square[2], "")

                squares.append(legal_square)


    for square in squares:
        try:
            x = DIF_BOARD + (files.index(square[0]) + 0.5) * square_width
            y = (8 - ranks.index(square[1]) - 0.5) * square_height + timer_height
            pygame.draw.circle(WN, CYAN, (x, y), ((square_width + square_height)/6))
            pygame.display.update()

        except:
            pass

    return squares

