import pygame
import numpy
from constants import *

ranks = [1, 2, 3, 4, 5, 6, 7, 8]  # String version is not wanted for Chess_Board, and get_square functions.
ranks_str = ["1", "2", "3", "4", "5", "6", "7", "8"]  # Wanted for get_piece function


# Drawing board
def Chess_Board(WN: pygame.Surface, board_interpretation: numpy.ndarray, pieces: list, white_time: int, black_time: int) -> tuple[pygame.Rect, pygame.Rect, pygame.Rect]:
    # Chess Board
    for r in range(0, rows):  # Files of Chess Board
        for c in range(0, columns):  # Ranks of Chess Board
            # Draw Square
            square = pygame.Rect((DIF_BOARD + c * square_width, timer_height + r * square_height),
                                 (square_width, square_height))

            # Color of Square
            if r % 2 != c % 2:  # formula for color
                color_square = BLACK

            elif r % 2 == c % 2:
                color_square = WHITE

            # Draw Square
            pygame.draw.rect(WN, color_square, square)

    # Board Coordinate Plane
    # Ranks
    for r in ranks:
        rank_number = 7 - ranks.index(r)
        rank_text = Font.render(str(r), 1, WHITE)
        WN.blit(rank_text, ((DIF_BOARD / 2 - rank_text.get_width() / 2),
                            timer_height + (rank_number + 0.5) * square_height - rank_text.get_height() / 2))

    # Files
    for c in files:
        file_number = files.index(c)
        file_text = Font.render(str(c), 1, WHITE)
        WN.blit(file_text, (DIF_BOARD + (file_number + 0.5) * square_width - file_text.get_width() / 2,
                            HEIGHT - option_height - (DIF_BOARD / 2 + file_text.get_height() / 2)))

    # Pieces
    # Get Positions and Display Pieces:
    for piece in pieces:
        piece.get_pos(board_interpretation)
        WN.blit(piece.image, (piece.x, piece.y))

    # Lines
    pygame.draw.line(WN, WHITE, (DIF_BOARD, timer_height), (WIDTH, timer_height), 1)
    pygame.draw.line(WN, WHITE, (WIDTH - 1, timer_height), (WIDTH - 1, (HEIGHT - option_height - DIF_BOARD)), 1)
    pygame.draw.line(WN, WHITE, (WIDTH, (HEIGHT - option_height - DIF_BOARD)),
                     (DIF_BOARD, (HEIGHT - option_height - DIF_BOARD)), 1)
    pygame.draw.line(WN, WHITE, (DIF_BOARD, (HEIGHT - option_height - DIF_BOARD)), (DIF_BOARD, timer_height), 1)

    # Buttons (resign, draw offer, and offer take back)
    # Draw Offer Button
    # Rectangle
    draw_button = pygame.Rect((WIDTH / 2 - button_width / 2, HEIGHT - option_height / 2 - button_height / 2),
                              (button_width, button_height))
    pygame.draw.rect(WN, WHITE, draw_button)

    # Text ("½ Draw")
    text = "½ Draw"
    text = Font.render(text, 1, GREY)
    WN.blit(text, (draw_button.x + (draw_button.width - text.get_width()) / 2,
                   draw_button.y + (draw_button.height - text.get_height()) / 2))

    # Resign Button
    # Rectangle
    resign_button = pygame.Rect((WIDTH / 6 - button_width / 2, HEIGHT - option_height / 2 - button_height / 2),
                                (button_width, button_height))
    pygame.draw.rect(WN, RED, resign_button)

    # Image (a flag)
    WN.blit(resign, (resign_button.x, resign_button.y + (resign_button.height - resign.get_height()) / 2))

    # Text (Resign)
    text = "Resign"
    text = resign_font.render(text, 1, WHITE)
    WN.blit(text, (
    resign_button.x + resign.get_width() + (resign_button.width - resign.get_width() - text.get_width()) / 2,
    resign_button.y + resign_button.height / 2 - text.get_height() / 2))

    # Take back Offer Button
    # Rectangle
    take_back_button = pygame.Rect((5 * WIDTH / 6 - button_width / 2, HEIGHT - option_height / 2 - button_height / 2),
                                   (button_width, button_height))
    pygame.draw.rect(WN, GREEN, take_back_button)

    # Image
    WN.blit(take_back,
            (take_back_button.x, take_back_button.y + (take_back_button.height - take_back.get_height()) / 2))

    # Text
    text = "Take Back"
    text = take_back_font.render(text, 1, WHITE)
    WN.blit(text, (take_back_button.x + take_back.get_width() + (
                take_back_button.width - take_back.get_width() - text.get_width()) / 2 - 1,
                   take_back_button.y + take_back_button.height / 2 - text.get_height() / 2))

    draw_time_control(WN, white_time, black_time)

    return draw_button, resign_button, take_back_button


def draw_time_control(WN: pygame.Surface, white_time: int, black_time: int) -> None:
    # Time Control Text
    # White
    white_min = str(white_time // 60)
    white_sec = white_time % 60

    if white_sec < 10:
        white_sec = f"0{str(white_sec)}"

    white_sec = str(white_sec)

    text = f"White Time: {white_min}:{white_sec}"
    text = time_font.render(text, 1, GREY)
    WN.blit(text, (WIDTH / 4 - text.get_width() / 2, timer_height / 2 - text.get_height() / 2))

    # Black
    black_min = str(black_time // 60)
    black_sec = black_time % 60

    if black_sec < 10:
        black_sec = f"0{str(black_sec)}"

    black_sec = str(black_sec)

    text = f"Black Time: {black_min}:{black_sec}"
    text = time_font.render(text, 1, GREY)
    WN.blit(text, (3 * WIDTH / 4 - text.get_width() / 2, timer_height / 2 - text.get_height() / 2))

    pygame.display.update()


# Piece functions
class Piece:
    # Initializing Variables
    def __init__(self, image: pygame.Surface, color: str, type: str, pieces: list) -> None:
        self.image = image
        self.color = color
        self.type = type
        pieces.append(self)

        if self.type == "pawn":
            if self.color == "white":
                self.promotion_pieces_directories = white_majors_directories

            elif self.color == "black":
                self.promotion_pieces_directories = black_majors_directories

        self.promotion_letter = ""

    # Return Position of the Piece
    def get_pos(self, board_interpretation: numpy.ndarray) -> None:
        try:
            location = numpy.where(board_interpretation == self)
            self.x = DIF_BOARD + location[1][0] * square_width
            self.y = timer_height + location[0][0] * square_height

        except:
            pass

    # Representation
    def __repr__(self) -> str:
        return f"{self.color} {self.type}"


# receiving board features based on x, y or square
# receiving square

def get_square(x: int, y: int) -> str:
    file_n = (x - DIF_BOARD) // square_width
    rank_n = 7 - (y - timer_height) // square_height
    file = files[file_n]
    rank = ranks[rank_n]
    square = file + str(rank)
    return square


# receiving piece
def get_piece(board_interpretation: numpy.ndarray, square: str) -> Piece:
    file = files.index(square[0])
    rank = ranks_str.index(square[1])
    piece = board_interpretation[7 - rank][file]

    return piece


def player_cant_win(player: str, pieces: list):
    players_pieces = []

    for piece in pieces:
        if piece.color == player:
            players_pieces.append(piece)

    if len(players_pieces) == 1:
        return True

    else:
        return False

