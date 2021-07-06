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
    if(board.checkWin()==1):
        print("Player X wins!")
        break

    while(True):
        pyr = (int)(input("Choose a row, Player Y:"))
        pyc = (int)(input("Choose a column, Player Y:"))
        if(board.checkMove(pyr,pyc)==True):
            board.makeMove(pyr,pyc,"y")
            break

    board.printBoard()
    if(board.checkWin()==1):
        print("Player Y wins!")
        break
