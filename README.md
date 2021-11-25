# Multiplayer Chess Program

# Dependencies 
• Python 3.9.5

• Chess Module 1.6.1 for finding legal moves, and win detection

• Pygame 2.0.2.dev4 for the main program

• PyQt5 5.15.4 for the message boxes, and promotions, as pygame doesn't support multiple windows being open at the same time yet (when I made the game).

• Numpy 1.21.1 as a replacement for lists
 
# How to Play
You can play by clicking on a piece, and then it shows the legal moves for it. Then you must click on one of the legal squares, and it will move. For Promotions, there is a window that pops up, and you select the piece you are going to promote to. There is also en passant, and castling, which follow the same rule for selecting. This is not touch move, so you can click on as many pieces as you like. The other features are a takeback button, resign button, draw button, and time control. For the takeback button, your opponent has to accept by clicking "Yes" on the message box. If their opponent agrees, then it will undo the opponent's move, and then their turn. Same as the draw offer button. Of the two, only the draw button gives another messages which says that the game is a draw. The resign button, however, will just give another message box that says the winner by resignation. The time control is 15|10, so each player has 15 minutes in total to play their moves, and they gain 10 seconds after each move is played. Of course, if your time runs out, then you lose the game. Win detection does not only include checkmate, but also stalemate, insuffient material, and fifty move rule. 

# Known Issues
• When ever a pop-up message is displayed, the main window (where the chess game is going on) will shrink, but it still has the same dimension in pixels! I think the reason is that I am using two modules for graphics (Pygame and PyQt5).

• Very rarely, the legal moves are wrong. If you click on the "invalid move circles," it will give an error (I've only seen it twice).

# Enjoy!

