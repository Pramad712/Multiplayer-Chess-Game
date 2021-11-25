# Castling, En Passant, Promotions
import numpy
from constants import *
from board import Piece

def detect_special_moves(board_interpretation: numpy.ndarray, piece: Piece, original_square: str, resulting_square: str) -> tuple[bool, bool, bool]:
    moved_file_n = files.index(resulting_square[0])
    moved_rank_n = ranks.index(resulting_square[1])

    # Detecting Special Moves
    # Castling
    castling = False

    # There is an exception which is if the rook and king are of different colors, but the king would be in check.
    if piece.type == "king" and (files.index(resulting_square[0]) - files.index(original_square[0]) == 2 or files.index(resulting_square[0]) - files.index(original_square[0]) == -2) and original_square[1] == resulting_square[1]:
        castling = True


    # En Passant
    en_passant = False

    # Logic: If the piece selected was a pawn, the piece one square diagonally is empty, but it still moved there (the only way this can happen is by en passant)
    if piece.type == "pawn":
        location = numpy.where(board_interpretation == piece)
        up = location[0][0] - 1
        down = location[0][0] + 1
        left = location[1][0] - 1
        right = location[1][0] + 1

        if piece.color == "white":
            try:
                if board_interpretation[up][left] == None and left == moved_file_n and up == 7 - moved_rank_n:
                    en_passant = True

            except:
                pass

            try:
                if board_interpretation[up][right] == None and right == moved_file_n and up == 7 - moved_rank_n:
                    en_passant = True

            except:
                pass

        if piece.color == "black":
            try:
                if board_interpretation[down][left] == None and left == moved_file_n and down == 7 - moved_rank_n:
                    en_passant = True

            except:
                pass

            try:
                if board_interpretation[down][right] == None and right == moved_file_n and down == 7 - moved_rank_n:
                    en_passant = True

            except:
                pass

    # Promotions
    promotion = False

    if piece.type == "pawn" and (moved_rank_n == 0 or moved_rank_n == 7):
        promotion = True

    return castling, en_passant, promotion

def move_castling(board_interpretation: numpy.ndarray, original_square: str, resulting_square: str) -> None:
    past_file_n = files.index(original_square[0])
    past_rank_n = 7 - ranks.index(original_square[1])
    moved_file_n = files.index(resulting_square[0])
    moved_rank_n = 7 - ranks.index(resulting_square[1])

    # Move the King
    board_interpretation[moved_rank_n][moved_file_n] = board_interpretation[past_rank_n][past_file_n]
    board_interpretation[past_rank_n][past_file_n] = None

    # Move the Rook
    if moved_file_n > past_file_n:  # Kingside Castling
        board_interpretation[moved_rank_n][5] = board_interpretation[moved_rank_n][7]
        board_interpretation[moved_rank_n][7] = None

    if moved_file_n < past_file_n:  # Queenside Castling
        board_interpretation[moved_rank_n][3] = board_interpretation[moved_rank_n][0]
        board_interpretation[moved_rank_n][0] = None

def move_en_passant(board_interpretation: numpy.ndarray, pieces: list, captured_pieces: list, original_square: str, resulting_square: str) -> None:
    # Find the captured piece
    past_file_n = files.index(original_square[0])
    past_rank_n = 7 - ranks.index(original_square[1])
    moved_file_n = files.index(resulting_square[0])
    moved_rank_n = 7 - ranks.index(resulting_square[1])

    piece_captured = board_interpretation[past_rank_n][moved_file_n]

    # Delete Piece from pieces list, and add it to captured_pieces
    location = pieces.index(piece_captured)
    del pieces[location]
    captured_pieces.append(piece_captured)

    # Delete Piece
    location = numpy.where(board_interpretation == piece_captured)
    board_interpretation[location] = None

    # Move Piece
    piece = board_interpretation[past_rank_n][past_file_n]
    board_interpretation[past_rank_n][past_file_n] = None
    board_interpretation[moved_rank_n][moved_file_n] = piece
