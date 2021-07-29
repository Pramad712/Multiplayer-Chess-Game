# Modules
import chess
import pygame
import numpy
from constants import *
from legal_moves import *
from board import *
from move import *
from special_moves import *
import tkinter as tk
from tkinter import messagebox

pygame.font.init()

# Screen
WN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

# Objects

# White Pieces

piece_white_rook_1 = Piece(white_rook, "white", "rook", pieces)
piece_white_knight_1 = Piece(white_knight, "white", "knight", pieces)
piece_white_bishop_1 = Piece(white_bishop, "white", "bishop", pieces)
piece_white_queen = Piece(white_queen, "white", "queen", pieces)
piece_white_king = Piece(white_king, "white", "king", pieces)
piece_white_bishop_2 = Piece(white_bishop, "white", "bishop", pieces)
piece_white_knight_2 = Piece(white_knight, "white", "knight", pieces)
piece_white_rook_2 = Piece(white_rook, "white", "rook", pieces)
piece_white_pawn_1 = Piece(white_pawn, "white", "pawn", pieces)
piece_white_pawn_2 = Piece(white_pawn, "white", "pawn", pieces)
piece_white_pawn_3 = Piece(white_pawn, "white", "pawn", pieces)
piece_white_pawn_4 = Piece(white_pawn, "white", "pawn", pieces)
piece_white_pawn_5 = Piece(white_pawn, "white", "pawn", pieces)
piece_white_pawn_6 = Piece(white_pawn, "white", "pawn", pieces)
piece_white_pawn_7 = Piece(white_pawn, "white", "pawn", pieces)
piece_white_pawn_8 = Piece(white_pawn, "white", "pawn", pieces)

# Black Pieces
piece_black_rook_1 = Piece(black_rook, "black", "rook", pieces)
piece_black_knight_1 = Piece(black_knight, "black", "knight", pieces)
piece_black_bishop_1 = Piece(black_bishop, "black", "bishop", pieces)
piece_black_queen = Piece(black_queen, "black", "queen", pieces)
piece_black_king = Piece(black_king, "black", "king", pieces)
piece_black_bishop_2 = Piece(black_bishop, "black", "bishop", pieces)
piece_black_knight_2 = Piece(black_knight, "black", "knight", pieces)
piece_black_rook_2 = Piece(black_rook, "black", "rook", pieces)
piece_black_pawn_1 = Piece(black_pawn, "black", "pawn", pieces)
piece_black_pawn_2 = Piece(black_pawn, "black", "pawn", pieces)
piece_black_pawn_3 = Piece(black_pawn, "black", "pawn", pieces)
piece_black_pawn_4 = Piece(black_pawn, "black", "pawn", pieces)
piece_black_pawn_5 = Piece(black_pawn, "black", "pawn", pieces)
piece_black_pawn_6 = Piece(black_pawn, "black", "pawn", pieces)
piece_black_pawn_7 = Piece(black_pawn, "black", "pawn", pieces)
piece_black_pawn_8 = Piece(black_pawn, "black", "pawn", pieces)

# Board Interpretation
board_interpretation = numpy.array(
    [(piece_black_rook_1, piece_black_knight_1, piece_black_bishop_1, piece_black_queen, piece_black_king, piece_black_bishop_2, piece_black_knight_2, piece_black_rook_2),
     (piece_black_pawn_1, piece_black_pawn_2, piece_black_pawn_3, piece_black_pawn_4, piece_black_pawn_5, piece_black_pawn_6, piece_black_pawn_7, piece_black_pawn_8),
     (None, None, None, None, None, None, None, None),
     (None, None, None, None, None, None, None, None),
     (None, None, None, None, None, None, None, None),
     (None, None, None, None, None, None, None, None),
     (piece_white_pawn_1, piece_white_pawn_2, piece_white_pawn_3, piece_white_pawn_4, piece_white_pawn_5, piece_white_pawn_6, piece_white_pawn_7, piece_white_pawn_8),
     (piece_white_rook_1, piece_white_knight_1, piece_white_bishop_1, piece_white_queen, piece_white_king, piece_white_bishop_2, piece_white_knight_2, piece_white_rook_2)])

# Chess Board
Chess_Board(WN, board_interpretation, pieces)

# Chess Module
board = chess.Board()

# Winner Text
def message(title, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(title, content)

    try:
        root.destroy()

    except:
        pass

# Game
legal_squares = []
squares_pressed = []
count = -1
turn = 1
game_is_not_over = True

while game_is_not_over:
    move_not_played = True
    while move_not_played:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                game_is_not_over = False
                break

            elif event.type == pygame.MOUSEBUTTONUP:
                count += 1
                # Draw board again to cover previous legal moves
                WN.fill(BLACK)
                Chess_Board(WN, board_interpretation, pieces)

                # Finding piece, and square pressed
                mx, my = pygame.mouse.get_pos()
                if mx >= DIF_BOARD:
                    square = get_square(mx, my)
                    squares_pressed.append(square)
                    file_n = files.index(square[0])
                    rank_n = ranks.index(square[1])
                    piece = board_interpretation[7 - rank_n][file_n]

                elif mx < DIF_BOARD:
                    square = None
                    piece = None

                # Captures/Moving Pieces
                if square in legal_squares:
                    update_board_not_called = True

                    try:
                        piece = get_piece(board_interpretation, squares_pressed[count - 1])
                        castling, en_passant, promotion = detect_special_moves(board_interpretation, piece, squares_pressed[count - 1], square)

                        if castling:
                            board_interpretation = move_castling(board_interpretation, squares_pressed[count - 1], square)

                        elif en_passant:
                            move_en_passant(board_interpretation, pieces, squares_pressed[count - 1], square)

                        elif promotion:
                            move_promotion(board_interpretation, pieces, squares_pressed[count - 1], square)
                            update_board(board, squares_pressed[count - 1], square, piece.promotion_letter)
                            Chess_Board(WN, board_interpretation, pieces)
                            update_board_not_called = False


                        else:
                            move_piece(board_interpretation, squares_pressed[count - 1], square, pieces)

                        if update_board_not_called:
                            update_board(board, squares_pressed[count - 1], square, piece.promotion_letter)
                            Chess_Board(WN, board_interpretation, pieces)

                        move_not_played = False

                    except:
                        pass


                # Drawing Legal Moves
                elif piece != None:
                    # If piece cicked is not a capture
                    image_pressed = piece.image
                    color_pressed = piece.color
                    type_pressed = piece.type
                    legal_squares = draw_legal_moves(WN, square, color_pressed, board, turn)



            if move_not_played == False:
                break


    # Checking for a win, and a draw by using chess module
    if board.can_claim_threefold_repetition():
        message("IT'S A TIE!", "Draw by threefold repetition! Threefold Repetition is when the same position has occurred 3 times in the game.")
        game_is_not_over = False

    if board.can_claim_fifty_moves():
        message("IT'S A TIE!", "Draw by the Fifty Move Rule! Fifty Move Rule is when no pawns have moved, and no captures have been made in 50 moves.")
        game_is_not_over = False

    if board.is_stalemate():
        message("IT'S A TIE!", "Draw by Stalemate! Stalemate is when a player can not make any legal moves.")
        game_is_not_over = False

    if board.is_insufficient_material():
        message("IT'S A TIE!", "Draw by Insufficient Material! Insufficient Material is when it is not possible to checkmate for both sides with the amount of material they have.")
        game_is_not_over = False

    if board.is_game_over():
        if turn == 1:
            message("WINNER!", "Checkmate! WHITE WON!!!")

        if turn == 2:
            message("WINNER!", "Checkmate! BLACK WON!!!")

        game_is_not_over = False


    legal_squares = []

    turn += 1
    turn %= 2

    if turn == 0:
        turn = 2


