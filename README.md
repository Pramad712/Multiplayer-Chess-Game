# Multiplayer Chess Program

# Dependencies 
Note: Latest versions at the time of creation

• Python 3.9.5

• Chess Module 1.6.1 for finding legal moves, and win detection

• Pygame 2.0.2.dev4 for the main program

• PyQt5 5.15.4 for the message boxes, and promotions, as pygame doesn't support multiple windows being open at the same time yet (when I made the game).

• Numpy 1.21.1 as a replacement for lists
 
# How to Play
You can play by clicking on a piece, and then it shows the legal moves for it. Then you must click on one of the legal squares for the piece to move to (invalid moves have no effect). For Promotions, there is a window that pops up, and you select the piece you want to promote to. There is also en passant, and castling, which follow the same rule for selecting. This is not touch move, so you can click on multiple pieces every turn. The other features are a takeback button, resign button, draw button, and time control. For the takeback button, your opponent has to accept by clicking "Yes" on the message box. If the opponent agrees, then it will undo both players' move. Same applies for the draw offer button, except it will give another pop-up message saying the game is a draw. The resign button, however, will just give another message box that says the winner by resignation. The time control is 15|10, so each player has 15 minutes in total to play their moves, and they gain 10 seconds after each move is played. Of course, if your time runs out, then you lose the game, but if the opponent can't theoretically checkmate, it's a draw. Win detection does not only include checkmate, but also stalemate, insuffient material, and the fifty move rule. 

# Known Issues
• When ever a pop-up message is displayed, the main window (where the chess game is going on) will shrink, but it still has the same dimensions in pixels! I think it's because I am using two modules for graphics (Pygame and PyQt5).

• Very rarely, the legal moves are wrong. If you click on the "valid move circles," (which would be considered illegal) it will give an error (I've only seen it occur twice). This is due to the chess module.

• Captures and instant moves after a takeback may cause errors because of the chess module too.

# Enjoy!
https://github.com/Pramad712/Multiplayer-Chess-Game/releases/tag/v1.0

Note: Images are from ChessKid. They looked funny and unique (kinda cringe though ...) so why not give it a try?
