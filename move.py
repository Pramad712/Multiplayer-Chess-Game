import chess
from constants import *
from special_moves import *

def move_piece(board_interpretation, original_square, resulting_square, pieces, captured_pieces):
    # updating board interpretation

    capture = False
    # Indexs, selection
    file_n = files.index(original_square[0])
    rank_n = 7 - ranks.index(original_square[1])

    moved_file_n = files.index(resulting_square[0])
    moved_rank_n = 7 - ranks.index(resulting_square[1])
    piece = board_interpretation[rank_n][file_n]
    place_moved = board_interpretation[moved_rank_n][moved_file_n]

    if place_moved != None:  # Capture
        capture = True
        location = pieces.index(place_moved)
        del pieces[location]
        captured_pieces.append(place_moved)

    board_interpretation[rank_n][file_n] = None
    board_interpretation[moved_rank_n][moved_file_n] = piece

    return capture

def update_board(board, original_square, resulting_square, piece_promoted):
    # update board from/using chess module
    move = original_square + resulting_square + piece_promoted
    move = chess.Move.from_uci(move)
    board.push(move)

