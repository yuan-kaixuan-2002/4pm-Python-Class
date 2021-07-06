class Board:
    key= [" ","o","x"]

    
    board = [[" "," "," "],
             [" "," "," "],
             [" "," ",""]]

    def printBoard(self):
        b = self.board


        print("   1   2   3")
        print("a|",b[0][0],"|",b[0][1],"|",b[0][2],"|")
        print("b|",b[1][0],"|",b[1][1],"|",b[1][2],"|")
        print("c|",b[2][0],"|",b[2][1],"|",b[2][2],"|")


    def checkWin(self):
        b = board
        if(b.get("a1")==b.get("a2"))
