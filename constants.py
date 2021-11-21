import pygame

pygame.font.init()

# Screen, dimensions
DIF_BOARD = 40 # The Difference of the bottum of the buttons, to the bottum of of the screen,
# and the distance from the left of the board (where the white line is) to the left of the screen.
WIDTH, HEIGHT = 560, 750
option_width, option_height = WIDTH, 110
button_width, button_height = 150, 70
timer_width, timer_height = WIDTH, 80
rows = 8
columns = 8
square_width = (WIDTH - DIF_BOARD) // rows
square_height = (HEIGHT - option_height - DIF_BOARD - timer_height) // columns
piece_size = (square_width, square_height)

# Board
Font = pygame.font.SysFont("comicsans", 36)
resign_font = pygame.font.SysFont("comicsans", 27)
take_back_font = pygame.font.SysFont("comicsans", 21)
ranks = ["1", "2", "3", "4", "5", "6", "7", "8"]
files = ["a", "b", "c", "d", "e", "f", "g", "h"]
color_square = (0, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (127.5, 127.5, 127.5)
RED = (230, 0, 0)
GREEN = (0, 230, 0)
CYAN = (0, 230, 230)
pieces = []
captured_pieces = []
colors = ["white", "black"]

# Time Control
time_font = resign_font
white_time = 900
black_time = 900
increment = 10

# Rect for clearing time control, and then draw it again
clear_time = pygame.Rect((0, 0), (WIDTH, timer_height))

# Images
# White's Pieces
white_pawn = pygame.transform.scale(pygame.image.load("white_pawn.png"), piece_size)
white_knight = pygame.transform.scale(pygame.image.load("white_knight.png"), piece_size)
white_bishop = pygame.transform.scale(pygame.image.load("white_bishop.png"), piece_size)
white_rook = pygame.transform.scale(pygame.image.load("white_rook.png"), piece_size)
white_queen = pygame.transform.scale(pygame.image.load("white_queen.png"), piece_size)
white_king = pygame.transform.scale(pygame.image.load("white_king.png"), piece_size)

# Black's Pieces
black_pawn = pygame.transform.scale(pygame.image.load("black_pawn.png"), piece_size)
black_knight = pygame.transform.scale(pygame.image.load("black_knight.png"), piece_size)
black_bishop = pygame.transform.scale(pygame.image.load("black_bishop.png"), piece_size)
black_rook = pygame.transform.scale(pygame.image.load("black_rook.png"), piece_size)
black_queen = pygame.transform.scale(pygame.image.load("black_queen.png"), piece_size)
black_king = pygame.transform.scale(pygame.image.load("black_king.png"), piece_size)

# Button Images
resign = pygame.transform.scale(pygame.image.load("resign.png"), (int(piece_size[0] * 3/4), int(piece_size[1] * 3/4)))
take_back = pygame.transform.scale(pygame.image.load("take_back.png"), (int(piece_size[0] * 2/3), int(piece_size[1] * 2/3)))

# Promotion Variables
white_majors_directories = ["white_queen.png", "white_rook.png", "white_bishop.png", "white_knight.png"]
black_majors_directories = ["black_queen.png", "black_rook.png", "black_bishop.png", "black_knight.png"]
