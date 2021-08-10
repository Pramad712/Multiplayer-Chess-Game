# Castling, En Passant, Promotions
import numpy
from constants import *
from promotion import promotion_menu

def detect_special_moves(board_interpretation, piece, original_square, resulting_square):
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

        try:
            # White Pieces (move up)
            if board_interpretation[up][left] == None and left == moved_file_n and up == 7 - moved_rank_n:
                en_passant = True

            elif board_interpretation[up][right] == None and right == moved_file_n and up == 7 - moved_rank_n:
                en_passant = True

            # Black Pieces (move down)
            elif board_interpretation[down][left] == None and left == moved_file_n and down == 7 - moved_rank_n:
                en_passant = True

            elif board_interpretation[down][right] == None and right == moved_file_n and down == 7 - moved_rank_n:
                en_passant = True

        except:
            pass

    # Promotions
    promotion = False

    if piece.type == "pawn" and (moved_rank_n == 0 or moved_rank_n == 7):
        promotion = True

    return castling, en_passant, promotion

def move_castling(board_interpretation, original_square, resulting_square):
    def get_location(board_interpretation, king, rook):
        # Locations
        king_location = numpy.where(board_interpretation == king)
        rook_location = numpy.where(board_interpretation == rook)
        return king_location, rook_location

    file_n = files.index(original_square[0])
    rank_n = ranks.index(original_square[1])
    moved_file_n = files.index(resulting_square[0])
    moved_rank_n = ranks.index(resulting_square[1])

    rook = None
    king_location, rook_location = [], []

    # Searching for king being used for castling
    king = board_interpretation[7 - rank_n][file_n]

    # Changing Position of Pieces
    # Place Pieces

    # Finding which side to castle
    if files.index(original_square[0]) < files.index(resulting_square[0]): # Kingside Castling
        # Find Rook
        rook = board_interpretation[7 - moved_rank_n][moved_file_n + 1]

        # Locations
        king_location, rook_location = get_location(board_interpretation, king, rook)

        # Placing Pieces
        board_interpretation[king_location[0][0]][king_location[1][0] + 2] = king
        board_interpretation[rook_location[0][0]][rook_location[1][0] - 2] = rook

    elif files.index(original_square[0]) > files.index(resulting_square[0]): # Queenside Castling
        # Find Rook
        rook = board_interpretation[7 - moved_rank_n][moved_file_n - 2]

        # Locations
        king_location, rook_location = get_location(board_interpretation, king, rook)

        board_interpretation[king_location[0][0]][king_location[1][0] - 2] = king
        board_interpretation[rook_location[0][0]][rook_location[1][0] + 3] = rook

    # Removing Pieces
    board_interpretation[king_location] = None
    board_interpretation[rook_location] = None

    return board_interpretation

def move_en_passant(board_interpretation, pieces, captured_pieces, original_square, resulting_square):
    # Find the captured piece
    file_n = files.index(original_square[0])
    rank_n = 7 - ranks.index(original_square[1])
    moved_file_n = files.index(resulting_square[0])
    moved_rank_n = 7 - ranks.index(resulting_square[1])
    piece_captured = None

    # En Passants for white
    if rank_n > moved_rank_n:
        piece_captured = board_interpretation[moved_rank_n + 1][moved_file_n]

    # En Passants for black:
    elif rank_n < moved_rank_n:
        piece_captured = board_interpretation[moved_rank_n - 1][moved_file_n]

    # Delete Piece from pieces list, and add it to captured_pieces
    location = pieces.index(piece_captured)
    del pieces[location]
    captured_pieces.append(piece_captured)

    # Delete Piece
    location = numpy.where(board_interpretation == piece_captured)
    board_interpretation[location] = None

    # Move Piece
    piece = board_interpretation[rank_n][file_n]
    board_interpretation[rank_n][file_n] = None
    board_interpretation[moved_rank_n][moved_file_n] = piece
