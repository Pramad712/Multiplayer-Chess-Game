import chess
from constants import *
from special_moves import *

def move_piece(board_interpretation, original_square, resulting_square, pieces):
    # updating board interpretation
    # Indexs, selection
    file_n = files.index(original_square[0])
    rank_n = 7 - ranks.index(original_square[1])

    moved_file_n = files.index(resulting_square[0])
    moved_rank_n = 7 - ranks.index(resulting_square[1])
    piece = board_interpretation[rank_n][file_n]
    place_moved = board_interpretation[moved_rank_n][moved_file_n]

    if place_moved != None:  # Capture
        location = pieces.index(place_moved)
        del pieces[location]

    board_interpretation[rank_n][file_n] = None
    board_interpretation[moved_rank_n][moved_file_n] = piece


def update_board(board, original_square, resulting_square, piece_promoted):
    try:
        # update board from chess module
        move = original_square + resulting_square + piece_promoted
        move = chess.Move.from_uci(move)
        board.push(move)

    except:
        pass
