from Board import Board

board = Board()

board.printBoard()

while(True):
    while(True):
        pxr = (int)(input("Choose a row, Player X:"))
        pxc = (int)(input("Choose a column, Player X:"))
        if(board.checkMove(pxr,pxc)==True):
            board.makeMove(pxr,pxc,"x")
            break

    board.printBoard()
    if(board.checkWin()== 1):
        print("Player X wins!")
        break

    while(True):
        pyr = (int)(input("Choose a row, Player O:"))
        pyc = (int)(input("Choose a column, Player O:"))
        if(board.checkMove(pyr,pyc)==True):
            board.makeMove(pyr,pyc,"o")
            break

    board.printBoard()
    if(board.checkWin()==1):
        print("Player O wins!")
        break
