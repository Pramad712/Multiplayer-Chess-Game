# Modules
import chess
import pygame
import numpy
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import time
import sys
from constants import *
from legal_moves import *
from board import *
from move import *
from special_moves import *
from promotion import *

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

# Draw Chess Board
draw_button, resign_button, take_back_button = Chess_Board(WN, board_interpretation, pieces, int(white_time), int(black_time))
pygame.display.update()

# Chess Board for Chess Module
board = chess.Board()
# Winner Message
class winner_message_box:
    def __init__(self):
        self.execute = True

    def stop(self):
        self.execute = False

    def draw_message(self, title, text):
        # Setup Message Box
        wn = QApplication(sys.argv)
        message_box = QMessageBox()
        message_box.setWindowTitle(title)
        message_box.setText(text)
        message_box.setIcon(QMessageBox.Information)
        ok_button = message_box.addButton(QMessageBox.Ok)
        ok_button.clicked.connect(self.stop)

        wn.aboutToQuit.connect(self.stop)
        # Display Message Box
        message_box.show()
        message_box.exec_()

        if self.execute:
            sys.exit(wn.exec_())


# Question Message if the Take Back or Draw Button is Clicked
class button_message_box:
    def __init__(self):
        self.execute = True

    # Button Messages
    def button_pressed(self, button):
        if button.text() == "&Yes":
            self.button_clicked = "Yes"

        elif button.text() == "&No":
            self.button_clicked = "No"

        self.execute = False

    def draw_button_message(self, title, text):
        # Setup Message Box
        wn = QApplication(sys.argv)
        message_box = QMessageBox()
        message_box.setWindowTitle(title)
        message_box.setText(text)
        message_box.setIcon(QMessageBox.Question)
        yes_button = message_box.addButton(QMessageBox.Yes)
        no_button = message_box.addButton(QMessageBox.No)

        # Detect Button Clicked Events
        yes_button.clicked.connect(lambda: self.button_pressed(yes_button))
        no_button.clicked.connect(lambda: self.button_pressed(no_button))

        # X button is same as the no button
        wn.aboutToQuit.connect(lambda: self.button_pressed(no_button))

        # Display Message Box
        message_box.show()
        message_box.exec_()

        if self.execute:
            wn.exec_()

# Game
legal_squares = []
squares_pressed = []
moves = []
color = "white"
count = -1
turn = 1
start_time = time.time()

while True:
    start_time = time.time()
    move_not_played = True

    while move_not_played:
        time_gone = time.time() - start_time

        if turn == 1:
            white_time -= time_gone

        elif turn == 2:
            black_time -= time_gone

        start_time = time.time()

        # Not calling chess_board, and doing WN.fill(BLACK) because then legal_moves will show up, and then be gone. We want them to stay.
        pygame.draw.rect(WN, BLACK, clear_time)
        draw_time_control(WN, int(white_time), int(black_time))

        # Check for Timeout
        if turn == 1 and white_time <= 0:
            message = winner_message_box()
            text = "Timeout! BLACK WON!!"

            if not player_cant_win("black", pieces):
                text = "Draw by Insufficient Material vs Timeout! This is when a player runs out of time, but their opponent can't possibily win, so the game becomes a draw!"

            message.draw_message("WINNER!!",  text)
            sys.exit()

        elif turn == 2 and black_time <= 0:
            message = winner_message_box()
            text = "Timeout! WHITE WON!!"

            if player_cant_win("white", pieces):
                text = "Draw by Insufficient Material vs Timeout! This is when a player runs out of time, but their opponent can't possibily win, so the game becomes a draw!"

            message.draw_message("WINNER!!",  text)
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Find what was Clicked
                mx, my = pygame.mouse.get_pos()

                if mx >= DIF_BOARD and my > timer_height and my <= timer_height + HEIGHT - option_height - DIF_BOARD:
                    WN.fill(BLACK)
                    draw_button, resign_button, take_back_button = Chess_Board(WN, board_interpretation, pieces, int(white_time), int(black_time))
                    # Finding piece, and square pressed
                    square = get_square(mx, my)
                    update = True

                    squares_pressed.append(square)
                    file_n = files.index(square[0])
                    rank_n = ranks.index(square[1])
                    piece = board_interpretation[7 - rank_n][file_n]

                    count += 1

                    # Capture/Moving Pieces
                    if square in legal_squares:
                        # Weird letter definitions in each element of the moves list: e - en passant, p - promotion,
                        # " " - nothing special, x - capture, and xp - promotion, and capture.
                        capture = False

                        piece = get_piece(board_interpretation, squares_pressed[count - 1])
                        castling, en_passant, promotion = detect_special_moves(board_interpretation, piece,
                                                                               squares_pressed[count - 1], square)

                        if castling:
                            move_castling(board_interpretation, squares_pressed[count - 1], square)

                        elif en_passant:
                            move_en_passant(board_interpretation, pieces, captured_pieces, squares_pressed[count - 1], square)
                            moves.append(squares_pressed[count - 1] + "e" + square)

                        elif promotion:
                            promotion = promotion_menu(piece)
                            promotion.draw_menu()
                            if promotion.promote:
                                capture = move_piece(board_interpretation, squares_pressed[count - 1], square, pieces, captured_pieces)

                                if capture:
                                    moves.append(squares_pressed[count - 1] + "xp" + square)

                                else:
                                    moves.append(squares_pressed[count - 1] + "p" + square)

                                capture = False

                            else:
                                update = False

                        else:
                            capture = move_piece(board_interpretation, squares_pressed[count - 1], square, pieces, captured_pieces)
                            moves.append(squares_pressed[count - 1] + " " + square)

                        if update:
                            update_board(board, squares_pressed[count - 1], square, piece.promotion_letter)
                            WN.fill(BLACK)
                            draw_button, resign_button, take_back_button = Chess_Board(WN, board_interpretation, pieces, int(white_time), int(black_time))
                            move_not_played = False

                        if capture:
                            moves.append(squares_pressed[count - 1] + "x" + square)


                    # Drawing Legal Moves
                    elif piece != None:
                        # If piece clicked is not a capture
                        color_pressed = piece.color
                        legal_squares = draw_legal_moves(WN, square, color_pressed, board, turn)

                    if piece == None:
                        legal_squares = []

                if mx >= draw_button.x and mx <= draw_button.x + button_width and my >= draw_button.y and my <= draw_button.y + button_height:
                    button_message = button_message_box()
                    button_message.draw_button_message("Draw Offer?", color[0].upper() + color[1:] + " has offered a draw. Does " + colors[-1 * turn][0].upper() + colors[-1 * turn][1:] + " want to accept it?")

                    if button_message.button_clicked == "Yes":
                        winner_message = winner_message_box()
                        winner_message.draw_message("ITS A TIE!", "Draw by Agreement!")
                        sys.exit()

                elif mx >= resign_button.x and mx <= resign_button.x + button_width and my >= resign_button.y and my <= resign_button.y + button_height:
                    winner_message = winner_message_box()
                    winner_message.draw_message("WINNER!!", "Resignation!! " + colors[-1 * turn].upper() + " WON!!")
                    sys.exit()

                elif mx >= take_back_button.x and mx <= take_back_button.x + button_width and my >= take_back_button.y and my <= take_back_button.y + button_height:
                    button_message = button_message_box()
                    button_message.draw_button_message("Take Back Offer?", color[0].upper() + color[1:] + " has offered a take back. Is " + colors[-1 * turn][0].upper() + colors[-1 * turn][1:] + " nice enough to accept it?")

                    if button_message.button_clicked == "Yes":
                        # The exception is if the current position is the original board.
                        # Used e, p, x, px, " " in the move list so it will be easier to detect if the move is a special move.
                        try:
                            # repeating things twice because doing it once will undo the previous turn, not move. 2 turns = 1 move.
                            board.pop()
                            board.pop()

                            # Undo move for board_interpretation
                            for i in range(2):
                                move = moves[len(moves) - 1]

                                if move[2:4] == "xp":
                                    # Names are reversed because it is undoing, not playing moves.
                                    # Likewise, Original_square, and resulting square parameters for the move_piece() function
                                    # also look weird because the move is supposed to be reversed, so then it will undo, not play moves.
                                    past_rank_n = 7 - ranks.index(move[5])
                                    past_file_n = files.index(move[4])
                                    moved_rank_n = 7 - ranks.index(move[1])
                                    moved_file_n = files.index(move[0])

                                    piece = get_piece(board_interpretation, move[4:6])
                                    piece.type = "pawn"
                                    piece.promotion_letter = ""

                                    if piece.color == "white":
                                        piece.image = white_pawn

                                    elif piece.color == "black":
                                        piece.image = black_pawn

                                    capture = move_piece(board_interpretation, move[4:6], move[0:2], pieces, captured_pieces)
                                    captured_piece = captured_pieces[len(captured_pieces) - 1]
                                    board_interpretation[past_rank_n][past_file_n] = captured_piece
                                    pieces.append(captured_piece)

                                elif move[2] == "x":
                                    past_rank_n = 7 - ranks.index(move[4])
                                    past_file_n = files.index(move[3])
                                    moved_rank_n = 7 - ranks.index(move[1])
                                    moved_file_n = files.index(move[0])
                                    move_piece(board_interpretation, move[3:5], move[0:2], pieces, captured_pieces)
                                    captured_piece = captured_pieces[len(captured_pieces) - 1]
                                    board_interpretation[past_rank_n][past_file_n] = captured_piece
                                    pieces.append(captured_piece)
                                    undid_capture = True

                                elif move[2] == "e":
                                    past_rank_n = 7 - ranks.index(move[4])
                                    past_file_n = files.index(move[3])
                                    moved_rank_n = 7 - ranks.index(move[1])
                                    moved_file_n = files.index(move[0])

                                    capture = move_piece(board_interpretation, move[3:5], move[0:2], pieces, captured_pieces)
                                    captured_piece = captured_pieces[len(captured_pieces) - 1]
                                    board_interpretation[past_rank_n + 1][past_file_n] = captured_piece
                                    pieces.append(captured_piece)

                                elif move[2] == "p":
                                    piece = get_piece(board_interpretation, move[3:5])
                                    piece.type = "pawn"
                                    piece.promotion_letter = ""

                                    if piece.color == "white":
                                        piece.image = white_pawn

                                    elif piece.color == "black":
                                        piece.image = black_pawn

                                    capture = move_piece(board_interpretation, move[3:5], move[0:2], pieces, captured_pieces)

                                elif move[2] == " ":
                                    capture = move_piece(board_interpretation, move[3:5], move[0:2], pieces, captured_pieces)

                                moves.pop()
                                WN.fill(BLACK)
                                draw_button, resign_button, take_back_button = Chess_Board(WN, board_interpretation, pieces, int(white_time), int(black_time))


                        except:
                            pass


            if move_not_played == False:
                if turn == 1:
                    white_time += increment

                elif turn == 2:
                    black_time += increment

                pygame.draw.rect(WN, BLACK, clear_time)
                draw_time_control(WN, int(white_time), int(black_time))

    # Checking for a win, and a draw by using the Chess Module
    if board.can_claim_threefold_repetition():
        message = winner_message_box()
        message.draw_message("IT'S A TIE!", "Draw by threefold repetition! Threefold Repetition is when the same position has occurred 3 times in the game.")
        sys.exit()

    elif board.can_claim_fifty_moves():
        message = winner_message_box()
        message.draw_message("IT'S A TIE!", "Draw by the Fifty Move Rule! Fifty Move Rule is when no pawns have moved, and no captures have been made for 50 moves in a row.")
        sys.exit()

    elif board.is_stalemate():
        message = winner_message_box()
        message.draw_message("IT'S A TIE!", "Draw by Stalemate! Stalemate is when a player can not make any legal moves - usually made by a blunder from the player with more material.")
        sys.exit()

    elif board.is_insufficient_material():
        message = winner_message_box()
        message.draw_message("IT'S A TIE!", "Draw by Insufficient Material! Insufficient Material is when it is not possible to checkmate for both sides with the amount of material they have.")
        sys.exit()

    elif board.is_game_over():
        if turn == 1:
            message = winner_message_box()
            message.draw_message("WINNER!", "Checkmate!! WHITE WON!!!")

        if turn == 2:
            message = winner_message_box()
            message.draw_message("WINNER!", "Checkmate!! BLACK WON!!!")

        sys.exit()


    legal_squares = []

    turn += 1
    turn %= 2

    if turn == 0:
        turn = 2

    color = colors[turn - 1]

