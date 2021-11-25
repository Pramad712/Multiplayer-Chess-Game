import chess
from numpy import ndarray
from constants import *
from special_moves import *

def move_piece_normally(board_interpretation: numpy.ndarray, original_square: str, resulting_square: str, pieces: list, captured_pieces: list) -> bool:
    capture = False

    past_file_n = files.index(original_square[0])
    past_rank_n = 7 - ranks.index(original_square[1])
    moved_file_n = files.index(resulting_square[0])
    moved_rank_n = 7 - ranks.index(resulting_square[1])

    piece = board_interpretation[past_rank_n][past_file_n]
    place_moved = board_interpretation[moved_rank_n][moved_file_n]

    if place_moved != None:  # Capture
        capture = True
        location = pieces.index(place_moved)
        del pieces[location]
        captured_pieces.append(place_moved)

    board_interpretation[past_rank_n][past_file_n] = None
    board_interpretation[moved_rank_n][moved_file_n] = piece

    return capture

def update_board(board: chess.Board, original_square: str, resulting_square: str, piece_promoted: str) -> None:
    move = original_square + resulting_square + piece_promoted
    move = chess.Move.from_uci(move)
    board.push(move)

