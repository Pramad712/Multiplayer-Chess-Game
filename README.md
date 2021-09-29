# Multiplayer Chess Program
 
Two Player Chess Program

# Dependencies (the Program is in Python)
• Chess Module 1.6.1 for finding legal moves, and win detection

• Pygame 2.0.1 for the main program

• PyQt5 5.15.4 for the message boxes, and promotions, as pygame doesn't support multiple windows being open at the same yet (when I made the game).

• Numpy 1.21.1 for lists
 
# How to Play
You can play by clicking on a piece, and then it shows the legal moves for it. Then you must click on one of the legal squares, and it will move. For Promotions, there is a window that pops up, and you select the piece you are going to promote to. There is also en passant, and castling, which follow the same rule for selecting. This is not touch move, so you can click on as many pieces as you like. There are also other features, which are a takeback button, a resign button, a draw button, and time control. For the takeback button, your opponent has to accept by clicking "Yes" on the message box. If their opponent agrees, then it will undo the opponent's move, and then their turn. Same as the draw offer button. Of the two, only the draw button gives another messages which says that the game is a draw. The resign button, however, will just give another message box that says the winner by resignation. The time control is 15 + 10, so each player has 15 minutes in total to play their moves, and they gain 10 seconds after each move is played. Off course, if your time runs out, then you lose the game. Win detection does not only include checkmate, but also stalemate, insuffient material, and fifty move rule. 

# Enjoy!

