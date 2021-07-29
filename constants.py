import pygame

pygame.font.init()

# Screen
DIF_BOARD = 40
WIDTH, HEIGHT = 720, 720 # Didn't the want screen to be too big!

# Board
ANNOTATION_FONT = pygame.font.SysFont("comics", 40)
ranks = ["1", "2", "3", "4", "5", "6", "7", "8"]
files = ["a", "b", "c", "d", "e", "f", "g", "h"]
color_square = (0, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
rows = 8
columns = 8
square_width = (WIDTH - DIF_BOARD) // rows
square_height = (HEIGHT - DIF_BOARD) // columns
piece_size = (square_width, square_height)
pieces = []
colors = ["white", "black"]

# Images

# White's Pieces

# Upload White's Pieces
white_pawn = pygame.transform.scale(pygame.image.load("white_pawn.png"), piece_size)
white_knight = pygame.transform.scale(pygame.image.load("white_knight.png"), piece_size)
white_bishop = pygame.transform.scale(pygame.image.load("white_bishop.png"), piece_size)
white_rook = pygame.transform.scale(pygame.image.load("white_rook.png"), piece_size)
white_queen = pygame.transform.scale(pygame.image.load("white_queen.png"), piece_size)
white_king = pygame.transform.scale(pygame.image.load("white_king.png"), piece_size)

# Upload Black's Pieces
black_pawn = pygame.transform.scale(pygame.image.load("black_pawn.png"), piece_size)
black_knight = pygame.transform.scale(pygame.image.load("black_knight.png"), piece_size)
black_bishop = pygame.transform.scale(pygame.image.load("black_bishop.png"), piece_size)
black_rook = pygame.transform.scale(pygame.image.load("black_rook.png"), piece_size)
black_queen = pygame.transform.scale(pygame.image.load("black_queen.png"), piece_size)
black_king = pygame.transform.scale(pygame.image.load("black_king.png"), piece_size)

# Promotion Variables
white_majors_directories = ["C:/Chess/white_queen.png", "C:/Chess/white_rook.png", "C:/Chess/white_bishop.png", "C:/Chess/white_knight.png"]
black_majors_directories = ["C:/Chess/black_queen.png", "C:/Chess/black_rook.png", "C:/Chess/black_bishop.png", "C:/Chess/black_knight.png"]
