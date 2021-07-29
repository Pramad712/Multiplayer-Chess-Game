from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from constants import *
import sys
import os

# Clicked Functions
def queen_clicked(menu, piece):
    if piece.color == "white":
        piece.image = white_queen

    elif piece.color == "black":
        piece.image = black_queen

    piece.promotion_letter = "q"
    menu.close()

def rook_clicked(menu, piece):
    if piece.color == "white":
        piece.image = white_rook

    elif piece.color == "black":
        piece.image = black_rook

    piece.promotion_letter = "r"
    menu.close()

def bishop_clicked(menu, piece):
    if piece.color == "white":
        piece.image = white_bishop

    elif piece.color == "black":
        piece.image = black_bishop

    piece.promotion_letter = "b"
    menu.close()

def knight_clicked(menu, piece):
    if piece.color == "white":
        piece.image = white_knight

    elif piece.color == "black":
        piece.image = black_knight

    piece.promotion_letter = "n"
    menu.close()

def promotion_menu(piece):
    try:
        # Using PyQt5 as Pygame 2.0 doesn't support multiple windows yet.
        # A list of the pieces the user can promote their pawn to
        wn = QApplication(sys.argv)

        # Centering the menu in the middle of my screen (my screen is 1920 x 1080 pixels)
        menu = QMainWindow()
        menu.setGeometry(960 - 2 * square_width, 540 - square_height / 2, 4 * square_width, square_height)

        # Dawing the Buttons
        queen_button = QPushButton(menu)
        queen_button.setIcon(QIcon(piece.promotion_pieces_directories[0]))
        queen_button.setIconSize(QSize(square_width, square_height))
        queen_button.setGeometry(0, 0, square_width, square_height)
        rook_button = QPushButton(menu)
        rook_button.setIcon(QIcon(piece.promotion_pieces_directories[1]))
        rook_button.setIconSize(QSize(square_width, square_height))
        rook_button.setGeometry(85, 0, square_width, square_height)
        bishop_button = QPushButton(menu)
        bishop_button.setIcon(QIcon(piece.promotion_pieces_directories[2]))
        bishop_button.setIconSize(QSize(square_width, square_height))
        bishop_button.setGeometry(170, 0, square_width, square_height)
        knight_button = QPushButton(menu)
        knight_button.setIcon(QIcon(piece.promotion_pieces_directories[3]))
        knight_button.setIconSize(QSize(square_width, square_height))
        knight_button.setGeometry(255, 0, square_width, square_height)

        # Effect when a button is clicked
        queen_button.clicked.connect(lambda: queen_clicked(menu, piece))
        rook_button.clicked.connect(lambda: rook_clicked(menu, piece))
        bishop_button.clicked.connect(lambda: bishop_clicked(menu, piece))
        knight_button.clicked.connect(lambda: knight_clicked(menu, piece))

        # Display Screen
        menu.show()
        wn.exec_()


    except:
        pass
