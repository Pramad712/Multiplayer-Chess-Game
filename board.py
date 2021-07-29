import pygame
import numpy
from constants import *

ranks = [1, 2, 3, 4, 5, 6, 7, 8] # String version is not wanted for Chess_Board, and get_square functions.
ranks_str = ["1", "2", "3", "4", "5", "6", "7", "8"] # Wanted for get_piece function

# Drawing board
def Chess_Board(WN, board_interpretation, pieces):
    # Chess Board
    for r in ranks:  # Files of Chess Board
        for c in files:  # Ranks of Chess Board
            # Draw Square
            square = pygame.Rect((DIF_BOARD + files.index(c) * square_width, ranks.index(r) * square_height), (square_width, square_height))

            # Color of Square
            if r % 2 != (files.index(c) + 1) % 2:  # formula for color
                color_square = WHITE

            else:
                color_square = BLACK

            # Draw Square
            pygame.draw.rect(WN, color_square, square)

    # Board Coordinate Plane
    # Ranks
    for r in ranks:
        rank_number = 7 - ranks.index(r)
        text = ANNOTATION_FONT.render(str(r), 1, WHITE)
        WN.blit(text, ((DIF_BOARD/2 - text.get_width()/2), (rank_number + 0.5) * square_height - text.get_height()/2))

    # Files
    for c in files:
        file_number = files.index(c)
        text = ANNOTATION_FONT.render(str(c), 1, WHITE)
        WN.blit(text, (DIF_BOARD + (file_number + 0.5) * square_width - text.get_width()/2, HEIGHT - (DIF_BOARD/2 + text.get_height()/2)))

    # Pieces

    # Get Positions and Display Pieces:
    draw_piece(WN, pieces, board_interpretation)

    # Lines

    pygame.draw.line(WN, WHITE, (DIF_BOARD, (HEIGHT - DIF_BOARD)), (WIDTH, (HEIGHT - DIF_BOARD)), 1)
    pygame.draw.line(WN, WHITE, (DIF_BOARD, (HEIGHT - DIF_BOARD)), (DIF_BOARD, (0)), 1)

    pygame.display.update()

# drawing pieces
def draw_piece(WN, pieces, board_interpretation):
    # Get Positions and Display Pieces:
    for piece in pieces:
        piece.get_pos(board_interpretation)
        WN.blit(piece.image, (piece.x, piece.y))

    pygame.display.update()

# Piece functions
class Piece:
    # Initializing Variables
    def __init__(self, image, color, type, pieces):
        self.image = image
        self.color = color
        self.type = type
        pieces.append(self)

        if self.color == "white" and self.type == "pawn":
            self.promotion_pieces_directories = white_majors_directories

        elif self.color == "black" and self.type == "pawn":
            self.promotion_pieces_directories = black_majors_directories

        self.promotion_letter = ""

    # Return Position of the Piece
    def get_pos(self, board_interpretation):
        try:
            location = numpy.where(board_interpretation == self)
            self.x = DIF_BOARD + location[1][0] * square_width
            self.y = location[0][0] * square_height

        except:
            pass

# reciving board features based on x, y or square
# reciving square
def get_square(x, y):
    file_n = (x - DIF_BOARD) // square_width
    rank_n = 7 - y // square_height
    file = files[file_n]
    rank = ranks[rank_n]
    square = file + str(rank)

    return square

# reciving piece
def get_piece(board_interpretation, square):
    file = files.index(square[0])
    rank = ranks_str.index(square[1])
    piece = board_interpretation[7 - rank][file]

    return piece