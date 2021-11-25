from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from constants import *
import sys
from board import Piece

width, height = 100, 100

class promotion_menu:
    # Cancel Text
    def __init__(self, piece: Piece) -> None:
        self.piece = piece

    # Clicked Functions
    def exit_clicked(self, menu: QMainWindow) -> None:
        self.close(menu)

        if self.piece.type == "pawn":
            self.promote = False

    def close(self, menu: QMainWindow) -> None:
        menu.close()

    def queen_clicked(self, menu: QMainWindow) -> None:
        if self.piece.color == "white":
            self.piece.image = white_queen

        elif self.piece.color == "black":
            self.piece.image = black_queen

        self.piece.promotion_letter = "q"
        self.piece.type = "queen"
        self.promote = True
        self.close(menu)

    def rook_clicked(self, menu: QMainWindow) -> None:
        if self.piece.color == "white":
            self.piece.image = white_rook

        elif self.piece.color == "black":
            self.piece.image = black_rook

        self.piece.promotion_letter = "r"
        self.piece.type = "rook"
        self.promote = True
        self.close(menu)

    def bishop_clicked(self, menu: QMainWindow) -> None:
        if self.piece.color == "white":
            self.piece.image = white_bishop

        elif self.piece.color == "black":
            self.piece.image = black_bishop

        self.piece.promotion_letter = "b"
        self.piece.type = "bishop"
        self.promote = True
        self.close(menu)

    def knight_clicked(self, menu: QMainWindow) -> None:
        if self.piece.color == "white":
            self.piece.image = white_knight

        elif self.piece.color == "black":
            self.piece.image = black_knight

        self.piece.promotion_letter = "n"
        self.piece.type = "knight"
        self.promote = True
        self.close(menu)

    def draw_menu(self) -> None:
        # A list of the self.pieces the user can promote their pawn to
        wn = QApplication(sys.argv)

        menu = QMainWindow()
        menu.setWindowTitle("Your Pawn Promotes to a ...")
        menu.setFixedSize(4 * width, height) # Makes it not resizable

        # Drawing the Buttons
        # Promotion Buttons
        # Queen Button
        queen_button = QPushButton(menu)
        queen_button.setStyleSheet("background: rgb(127.5, 127.5, 127.5)")
        queen_button.setIcon(QIcon(self.piece.promotion_pieces_directories[0]))
        queen_button.setIconSize(QSize(width, height))
        queen_button.setGeometry(0, 0, width, height)


        # Knight Button
        knight_button = QPushButton(menu)
        knight_button.setStyleSheet("background: rgb(127.5, 255, 127.5)")
        knight_button.setIcon(QIcon(self.piece.promotion_pieces_directories[3]))
        knight_button.setIconSize(QSize(width, height))
        knight_button.setGeometry(width, 0, width, height)

        # Rook Button
        rook_button = QPushButton(menu)
        rook_button.setStyleSheet("background: rgb(0, 255, 127.5)")
        rook_button.setIcon(QIcon(self.piece.promotion_pieces_directories[1]))
        rook_button.setIconSize(QSize(width, height))
        rook_button.setGeometry(2 * width, 0, width, height)

        # Bishop Button
        bishop_button = QPushButton(menu)
        bishop_button.setStyleSheet("background: rgb(0, 176, 169)")
        bishop_button.setIcon(QIcon(self.piece.promotion_pieces_directories[2]))
        bishop_button.setIconSize(QSize(width, height))
        bishop_button.setGeometry(3 * width, 0, width, height)

        # Effect when a button is clicked
        queen_button.clicked.connect(lambda: self.queen_clicked(menu))
        rook_button.clicked.connect(lambda: self.rook_clicked(menu))
        bishop_button.clicked.connect(lambda: self.bishop_clicked(menu))
        knight_button.clicked.connect(lambda: self.knight_clicked(menu))

        # Close Button
        wn.aboutToQuit.connect(lambda: self.exit_clicked(menu))

        # Display Screen
        menu.show()
        wn.exec_()
